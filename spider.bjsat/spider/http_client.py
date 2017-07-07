# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

import requests
import time
import random

from config import download_delay, default_headers, download_timeout, USER_AGENTS

import logging

from exception import HttpClientError


class HTTPClient(object):
    def __init__(self, min_time_interval=download_delay, proxies=""):
        self._session = requests.Session()
        self._session.headers.update(default_headers)
        self._session.headers.update({"User-Agent": random.choice(USER_AGENTS)})
        self._min_time_interval = min_time_interval * 1000 + 2 * 1000 * random.random()
        self._last_request_time = -1

        self._current_proxies = {"http": proxies}

        pass

    def _set_last_request_time(self):
        now = time.time()
        if now - self._last_request_time < self._min_time_interval:
            sleep = self._min_time_interval - (now - self._last_request_time)
            time.sleep(sleep / 1000.0)
            pass
        self._last_request_time = time.time()
        pass

    def post(self, url, data=None, json=None):
        self._set_last_request_time()

        logging.info("<POST %s> %s" % (url, data))
        # logging.debug("HEADER %s" % self._session.headers)
        try:
            response = self._session.post(url, data=data, json=json, proxies=self._current_proxies,
                                          timeout=download_timeout)
        except Exception, e:
            logging.error(e.message)
            raise HttpClientError()
        logging.info("<response %d>" % response.status_code)

        return response

    def get(self, url):
        self._set_last_request_time()

        logging.info("<GET %s>" % url)
        # logging.debug("HEADER %s" % self._session.headers)
        try:
            response = self._session.get(url, proxies=self._current_proxies,
                                         timeout=download_timeout)
        except Exception, e:
            logging.error(e.message)
            raise HttpClientError()
        logging.info("<response %d>" % response.status_code)

        return response
