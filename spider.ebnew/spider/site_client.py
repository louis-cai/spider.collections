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

    def get_search_list(self):
        url = "http://www.ebnew.com/tradingIndex.view"
        payload = {
            'keywords': '',
            'infoType': '(0108 2903 3203 3303 3403 3503)',
            'bidModel': '',
            'fundSourceCodes': '',
            'zone': '',
            'normIndustry': '',
            'sortMethod': '',
            'timeType': '',
            'pubDateBegin': '',
            'pubDateEnd': '',
        }
        response = self._verify_post(url, data=payload)
        return response

    def get_next(self, url):
        response = self._verify_get(url)
        return response
        pass

    def get_detail(self, url):
        response = self._verify_get(url)
        return response
