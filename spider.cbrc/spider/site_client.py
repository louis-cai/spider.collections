# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

import logging

# import time
# import urllib2

from http_client import HTTPClient

from exception import Error302, Error403, Error404, Error502, Error503, ErrorStatusCode, HttpClientError
from config import default_headers
from config import download_timeout


class SiteClient(object):
    def __init__(self):
        self._http_client = HTTPClient()
        pass

    def _verify_post(self, url, data=None, json=None, times=0, headers=default_headers, timeout=download_timeout):

        # headers.update({
        #     'User-Agent': self._user_agent,
        #     # "Proxy-Authorization": self.get_authHeader()
        # })

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
        # headers.update({
        #     'User-Agent': self._user_agent,
        #     # "Proxy-Authorization": self.get_authHeader(refresh_ip)
        # })
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

    def list(self, usetate, start, limit):
        url = "http://xukezheng.cbrc.gov.cn/ilicence/getLicence.do?useState=%s" % usetate
        headers = {
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.6,en-US;q=0.4,en;q=0.2',
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
            # 'Content-Length': '16'
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            # Cookie:_gscu_1997809816=77902611zipovd20; _gscbrs_1997809816=1; JSESSIONID=0000-erR7dwQ4CdB0GOnsAoMjU_:-1
            'Host': 'xukezheng.cbrc.gov.cn',
            'Origin': 'http://xukezheng.cbrc.gov.cn',
            'Pragma': 'no-cache',
            'Referer': 'http://xukezheng.cbrc.gov.cn/ilicence/licence/licenceQuery.jsp',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest',
        }

        payload = {
            "start": '%s' % start,
            "limit": "%s" % limit,
        }

        response = self._verify_post(url, headers=headers, data=payload)
        return response

    def get_detail(self, useState, flowNo):
        url = "http://xukezheng.cbrc.gov.cn/ilicence/showLicenceInfo.do?state=%s&id=%s" % (useState, flowNo)
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate, sdch',
            'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.6,en-US;q=0.4,en;q=0.2',
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
            # Cookie:_gscu_1997809816=77902611zipovd20; _gscbrs_1997809816=1; JSESSIONID=0000-erR7dwQ4CdB0GOnsAoMjU_:-1
            'Host': 'xukezheng.cbrc.gov.cn',
            'Pragma': 'no-cache',
            'Referer': 'http://xukezheng.cbrc.gov.cn/ilicence/licence/licenceQuery.jsp',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'
        }
        response = self._verify_get(url, headers=headers)
        return response
