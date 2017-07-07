# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

import logging
# import math
# import random
#
# from bs4 import BeautifulSoup
#
# from http_client import HTTPClient
# from utils import get_timeStamp
#
from exception import Error302, Error403, Error404, Error500, Error502, Error503, ErrorStatusCode, HttpClientError
from config import default_headers, USER_AGENTS
# import random

import requests


class SiteClient(object):
    def __init__(self):
        self._http_client = requests.Session()
        pass

    #
    # def _verify_post(self, url, data=None, json=None, times=0, headers=default_headers):
    #     try:
    #         response = self._http_client.post(url, data, json, headers)
    #         if response.status_code == 200:
    #             pass
    #         elif response.status_code == 302:
    #             location = response.headers['Location']
    #             logging.debug("location: %s" % location)
    #             raise Error302()
    #         elif response.status_code == 403:
    #             raise Error403()
    #         elif response.status_code == 404:
    #             raise Error404()
    #         elif response.status_code == 502:
    #             raise Error502()
    #         elif response.status_code == 503:
    #             raise Error503()
    #         else:
    #             raise ErrorStatusCode(response.status_code)
    #         return response
    #
    #     except HttpClientError, err:
    #         times += 1
    #         if times < 3:
    #             return self._verify_post(url, data=data, json=json, times=times, headers=headers)
    #         else:
    #             raise err
    #
    # def _verify_get(self, url, times=0, headers=default_headers):
    #     try:
    #         response = self._http_client.get(url)
    #         if response.status_code == 200:
    #             pass
    #         elif response.status_code == 302:
    #             location = response.headers['Location']
    #             logging.debug("location: %s" % location)
    #             raise Error302()
    #         elif response.status_code == 403:
    #             raise Error403()
    #         elif response.status_code == 404:
    #             raise Error404()
    #         elif response.status_code == 502:
    #             raise Error502()
    #         else:
    #             raise ErrorStatusCode(response.status_code)
    #         return response
    #     except HttpClientError, err:
    #         times += 1
    #         if times < 3:
    #             return self._verify_get(url, times=times, headers=headers)
    #         else:
    #             raise err


    # -------------right main----------------------------
    # def get_detail(self, company_name):
    #     url = "http://baike.baidu.com/item/" + company_name
    #     # url = "http://baike.baidu.com/item/%E5%9C%A8%E7%BA%BF%E9%80%94%E6%B8%B8%EF%BC%88%E5%8C%97%E4%BA%AC%EF%BC%89%E7%A7%91%E6%8A%80%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8"
    #     try:
    #         response = requests.get(url, timeout=5, allow_redirects=False)
    #         if response.status_code == 200:
    #             return response
    #         else:
    #             raise Exception("response status_code error %s" % response.status_code)
    #     except Exception, e:
    #         logging.info(e.message)
    #         return None

    def get_search(self, company_name):
        url = "http://baike.baidu.com/search/word?word=" + company_name
        try:
            response = requests.get(url, timeout=5)
        except Exception, e:
            logging.info(e.message)
            return None

        if response.status_code == 200:
            return response
        elif response.status_code == 500:
            raise Error500()
        else:
            raise ErrorStatusCode(response.status_code)
