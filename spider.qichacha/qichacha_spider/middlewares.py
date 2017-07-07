# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

import base64
import random
from qichacha_spider.proxy.proxy_helper import ProxyHelper


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

    proxy_items_http = ProxyHelper.get_proxy_items_type_http()

    # proxy_items_https = ProxyHelper.get_proxy_items_jd_type_https()

    def process_request(self, request, spider):

        # if request.url.startswith("https://"):
        #     # TODO 由于https代理验证有问题,这里暂时改为,将https代理替换成http代理
        #     url = request.url.replace("https://", "http://")
        #     print "replace url, ", url
        #     request.replace(url=url)

            # n = ProxyMiddleware.https_n
            # if n >= len(ProxyMiddleware.proxy_items_https):
            #     ProxyMiddleware.proxy_items_https = ProxyHelper.get_proxy_items_jd_type_https()
            #     n = 0
            #
            # request.meta['proxy'] = "https://%s:%d" % (
            #     ProxyMiddleware.proxy_items_http[n]["ip"], int(ProxyMiddleware.proxy_items_http[n]["port"]))
            # ProxyMiddleware.https_n = n + 1

        # Set the location of the proxy
        # if request.url.startswith("http://"):
        proxy_len = len(ProxyMiddleware.proxy_items_http)
        if proxy_len > 0:
            n = ProxyMiddleware.http_n
            if n >= len(ProxyMiddleware.proxy_items_http):
                ProxyMiddleware.proxy_items_http = ProxyHelper.get_proxy_items_type_http()
                n = 0

            request.meta['proxy'] = "http://%s:%d" % (
                ProxyMiddleware.proxy_items_http[n]["ip"], int(ProxyMiddleware.proxy_items_http[n]["port"]))
            ProxyMiddleware.http_n = n + 1
            print request.meta['proxy']

            # # Use the following lines if your proxy requires authentication
            # proxy_user_pass = "USERNAME:PASSWORD"
            # # setup basic authentication for the proxy
            # encoded_user_pass = base64.b64encode(proxy_user_pass)
            # request.headers['Proxy-Authorization'] = 'Basic ' + encoded_user_pass
