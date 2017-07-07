# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

import logging
import random
import time

from scrapy.http import HtmlResponse
from selenium import webdriver

from ali_spider.helpers.proxy_helper import ProxyHelper


# logger = logging.getLogger('PhantomjsDownloaderMiddleware')


class RandomUserAgentMiddleware(object):
    """Randomly rotate user agents based on a list of predefined ones"""

    def __init__(self, agents):
        self.agents = agents

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler.settings.getlist('USER_AGENTS'))

    def process_request(self, request, spider):
        request.headers.setdefault('User-Agent', random.choice(self.agents))


class ProxyMiddleware(object):
    http_n = 0
    https_n = 0

    proxy_items_http = ProxyHelper.get_proxy_items_jd_type_http()
    proxy_items_https = ProxyHelper.get_proxy_items_jd_type_https()

    def process_request(self, request, spider):

        if request.url.startswith("https://"):
            # TODO 由于https代理验证有问题,这里暂时改为,将https代理替换成http代理
            url = request.url.replace("https://", "http://")
            print "replace url, ", url
            request.replace(url=url)

            # n = ProxyMiddleware.https_n
            # if n >= len(ProxyMiddleware.proxy_items_https):
            #     ProxyMiddleware.proxy_items_https = ProxyHelper.get_proxy_items_jd_type_https()
            #     n = 0
            #
            # request.meta['proxy'] = "https://%s:%d" % (
            #     ProxyMiddleware.proxy_items_http[n]["ip"], int(ProxyMiddleware.proxy_items_http[n]["port"]))
            # ProxyMiddleware.https_n = n + 1

        # Set the location of the proxy
        if request.url.startswith("http://"):
            n = ProxyMiddleware.http_n
            if n >= len(ProxyMiddleware.proxy_items_http):
                ProxyMiddleware.proxy_items_http = ProxyHelper.get_proxy_items_jd_type_http()
                n = 0

            request.meta['proxy'] = "http://%s:%d" % (
                ProxyMiddleware.proxy_items_http[n]["ip"], int(ProxyMiddleware.proxy_items_http[n]["port"]))
            ProxyMiddleware.http_n = n + 1

            # # Use the following lines if your proxy requires authentication
            # proxy_user_pass = "USERNAME:PASSWORD"
            # # setup basic authentication for the proxy
            # encoded_user_pass = base64.b64encode(proxy_user_pass)
            # request.headers['Proxy-Authorization'] = 'Basic ' + encoded_user_pass


class PhantomjsDownloaderMiddleware(object):
    def __init__(self, options, max_sum):
        self.options = options
        self.max_sum = max_sum

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            options=crawler.settings.get('PHANTOMJS_OPTIONS', {}),
            max_sum=crawler.settings.get('PHANTOMJS_MAXSUM', 2)
        )

    def process_request(self, request, spider):
        service_args = ['--load-image=false', '--disk-cache=true']
        if 'proxy' in request.meta:
            service_args.append('--proxy=' + request.meta['proxy'][7:])
        if 'port' in request.meta:
            port = request.meta['port']
        else:
            port = 29842
        try:
            driver = webdriver.PhantomJS(port=port,
                                         desired_capabilities={
                                             'javascriptEnabled': True,
                                             'platform': 'windows',
                                             'browserName': 'Mozilla',
                                             'version': '5.0',
                                             'phantomjs.page.settings.userAgent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.57 Safari/537.36"
                                         })
            driver.get(request.url)
            # time.sleep(10)
            content = driver.page_source.encode('utf-8')
            url = driver.current_url.encode('utf-8')
            driver.quit()
            if content == '<html><head></head><body></body></html>':
                # logger.info('content is empty : 503')
                return HtmlResponse(request.url, encoding='utf-8', status=503, body='')
            else:
                # logger.info('content get success : 200')
                return HtmlResponse(url, encoding='utf-8', status=200, body=content)
        except Exception, e:
            # logger.warning(e)
            # logger.info('Exception content is empty : 503')
            return HtmlResponse(request.url, encoding='utf-8', status=503, body='')
