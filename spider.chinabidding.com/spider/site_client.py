# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

import json
import random
import time
import logging
from urlparse import urljoin
from captcha import read_body_to_string
from http_client import HTTPClient
import requests

from exception import Error302, Error403, Error404, ErrorStatusCode


class SiteClient(object):
    def __init__(self):
        # self._username = username
        # self._password = password
        self._http_client = HTTPClient()
        pass

    """+++++++++++++++++++login++++++++++++"""

    # def _per_login(self):
    #     login_page_url = "http://center.qianlima.com/login.jsp"
    #     response = self._http_client.get(login_page_url)
    #     return response
    #
    # def _do_login(self):
    #     form_data = {
    #         "username": self._username,
    #         "password": self._password,
    #         "rem_login": "1"
    #     }
    #     login_url = "http://center.qianlima.com/login_post.jsp?re_url=null"
    #     response = self._http_client.post(login_url, form_data)
    #     # logging.debug("text: %s" % response.text)
    #
    #     # try:
    #     #     json_obj = json.loads(response.text)
    #     # except Exception, e:
    #     #     json_obj = {"isSuccess": False, "sMsg": "is html return"}
    #     #     pass
    #     #
    #     # logging.debug("json_obj: %s" % json_obj)
    #     #
    #     # if not json_obj.get("isSuccess"):
    #     #     return False
    #     logging.info("cookie: %s" % response.cookies.get_dict())
    #     return True
    #
    # def login(self):
    #     # print "++++++++++++++login+++++++++++++++++"
    #     self._per_login()
    #     is_success = self._do_login()
    #     return is_success

    def _verify_post(self, url, data=None, json=None, **kwargs):
        # kwargs.setdefault("allow_redirects", False)
        response = self._http_client.post(url, data, json, **kwargs)
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
        else:
            raise ErrorStatusCode()
        return response

    def _verify_get(self, url, **kwargs):
        # kwargs.setdefault("allow_redirects", False)
        response = self._http_client.get(url, **kwargs)
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
        else:
            raise ErrorStatusCode()
        return response

        # def get_company(self, url):
        #     response = self._verify_get(url)
        #     return response
        #
        # def get_search(self, url):
        #     response = self._verify_get(url)
        #     return response
