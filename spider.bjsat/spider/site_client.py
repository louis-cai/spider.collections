# -*- coding:utf-8 -*-
__author__ = 'zhaojm'


import logging
import urllib
import math
import random
from http_client import HTTPClient
from exception import Error302, Error403, Error404, Error502, Error503, ErrorStatusCode, HttpClientError

class SiteClient(object):
    def __init__(self, proxies):
        # self._username = username
        # self._password = password
        self._http_client = HTTPClient(proxies=proxies)

        pass

    def _verify_post(self, url, data=None, json=None, times=0):
        try:
            response = self._http_client.post(url, data, json)
            if response.status_code == 200:
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

        except HttpClientError, err:
            times += 1
            if times < 3:
                return self._verify_post(url, data=data, json=json, times=times)
            else:
                raise err

    def _verify_get(self, url, times=0):
        try:
            response = self._http_client.get(url)
            if response.status_code == 200:
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
        except HttpClientError, err:
            times += 1
            if times < 3:
                return self._verify_get(url, times=times)
            else:
                raise err

    def index_1(self):
        index_1_url = "http://www.bjsat.gov.cn/WSBST/bsdt/swdjzcx/query.jsp"
        response = self._verify_get(index_1_url)
        # soup = BeautifulSoup(response.text, 'lxml')
        # index_2_url = soup.select_one('frame')['src']
        # response = self._http_client.get(index_2_url)
        # soup = BeautifulSoup(response.text, 'lxml')
        # self.credit_ticket = None
        # # credit_ticket

    #
    # def get_verify_img(self):
    #     url = "http://www.bjsat.gov.cn/WSBST/getVFImage"
    #     response = self._http_client.get(url)
    #     return response
    #
    # def refresh_verify_img(self):
    #     url = "qyxy.baic.gov.cn/CheckCodeYunSuan?currentTimeMillis=%s&r=%s" % (get_currentTimeMillis(), random.random())
    #
    # def check_verify_code(self, check_code):
    #     url = "http://qyxy.baic.gov.cn/login/loginAction!checkCode.dhtml?check_code=%s&currentTimeMillis=%s&random=%s" % (
    #         check_code, get_currentTimeMillis(), math.ceil(random.random() * 100000))

    def get_search_list(self, search_key, times=0):
        url = "http://www.bjsat.gov.cn/WSBST/bsdt/swdjzcx/query.jsp?cxtj=2&cxtjvalue=" + urllib.quote(
            search_key.encode('gb2312')) + "&u_vfy=1&x=22&y=12"
        # url = "http://www.bjsat.gov.cn/WSBST/bsdt/swdjzcx/query.jsp"
        # form_data = {
        #     "cxtjvalue": urllib.quote(search_key.encode('gb2312')),
        #     "cxtj": "2",
        #     "u_vfy": "%d" % random.randint(0, 20),
        #     "x": "%d" % random.randint(0, 29),
        #     "y": "%d" % random.randint(0, 29)
        # }

        try:
            # response = self._verify_post(url, form_data)
            response = self._verify_get(url)
            return response
        except Exception, e:
            times += 1
            if times < 5:
                return self.get_search_list(url, times)
            else:
                raise Exception('more times')

    def get_detail(self, url, times=0):
        try:
            # url = "http://www.bjsat.gov.cn/WSBST/bsdt/swdjzcx/queryto.jsp?nsrsbh=91110105MA003TH355"
            response = self._verify_get(url)
            return response
        except Exception, e:
            times += 1
            if times < 5:
                return self.get_detail(url, times)
            else:
                raise Exception('more times')
