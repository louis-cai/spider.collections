# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

import logging

# import time
# import urllib2

from http_client import HTTPClient
# from utils import get_timeStamp

from exception import Error302, Error403, Error404, Error502, Error503, ErrorStatusCode, HttpClientError
from config import default_headers, USER_AGENTS, download_timeout
import random


class SiteClient(object):
    def __init__(self, proxies):
        self._http_client = HTTPClient(proxies=proxies)
        self._user_agent = random.choice(USER_AGENTS)
        pass

    def _verify_post(self, url, data=None, json=None, times=0, headers=default_headers, timeout=download_timeout):

        headers.update({
            'User-Agent': self._user_agent
        })

        try:
            response = self._http_client.post(url=url, data=data, json=json, headers=headers, timeout=timeout)
            if response.status_code == 200:
                logging.debug(response.headers)
                pass
            elif response.status_code == 302:
                location = response.headers['Location']
                logging.debug("location: %s" % location)
                raise Error302()
            elif response.status_code == 403:
                raise Error403()
            elif response.status_code == 404:
                raise Error404()
            elif response.status_code == 502:
                raise Error502()
            elif response.status_code == 503:
                raise Error503()
            else:
                raise ErrorStatusCode(response.status_code)
            return response
        except Error403, err:
            raise err
        except HttpClientError, err:
            times += 1
            if times < 2:
                return self._verify_post(url, data=data, json=json, times=times, headers=headers, timeout=timeout)
            else:
                raise err

    def _verify_get(self, url, times=0, headers=default_headers, refresh_ip=False, timeout=download_timeout):
        headers.update({
            'User-Agent': self._user_agent
        })
        try:
            response = self._http_client.get(url, headers=headers, timeout=timeout)
            if response.status_code == 200:
                logging.debug(response.headers)
                pass
            elif response.status_code == 302:
                location = response.headers['Location']
                logging.debug("location: %s" % location)
                raise Error302()
            elif response.status_code == 403:
                raise Error403()
            elif response.status_code == 404:
                raise Error404()
            elif response.status_code == 502:
                raise Error502()
            else:
                raise ErrorStatusCode(response.status_code)
            return response
        except Error403, err:
            raise err
        except HttpClientError, err:
            times += 1
            if times < 2:
                return self._verify_get(url, times=times, headers=headers, refresh_ip=refresh_ip, timeout=timeout)
            else:
                raise err

    def get_search_list(self, page):
        url = "https://b2b.10086.cn/b2b/main/listVendorNoticeResult.html?noticeBean.noticeType=7"
        payload = {
            'page.currentPage': '%s' % page,
            'page.perPageSize': '20',
            'noticeBean.sourceCH': '',
            'noticeBean.source': '',
            'noticeBean.title': '',
            'noticeBean.startDate': '',
            'noticeBean.endDate': '',
        }
        headers = {
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.6,en-US;q=0.4,en;q=0.2',
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
            'Content-Length': '138',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            # 'Cookie':'saplb_*=(J2EE204290120)204290150; JSESSIONID=Kaxp-HoLM8Hz9qDC8WgpqnXmf5tNWAFmOC0M_SAPp3WltrLupVsa4zRWu9uVGFDB',
            'Host': 'b2b.10086.cn',
            'Origin': 'https://b2b.10086.cn',
            'Pragma': 'no-cache',
            'Referer': 'https://b2b.10086.cn/b2b/main/listVendorNotice.html?noticeType=2',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest',
        }
        response = self._verify_post(url, data=payload, headers=headers)
        return response

    def get_next(self, url):
        response = self._verify_get(url)
        return response
        pass

    def get_detail(self, url):
        response = self._verify_get(url)
        return response
