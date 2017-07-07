# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

from mongo import ProxyDB
import logging
import time


class GetProxy(object):
    def __init__(self):
        self._proxy_cur = None
        self.refresh_proxy()
        pass

    def refresh_proxy(self):
        self._proxy_cur = ProxyDB.get_all()
        if self._proxy_cur.count() == 0:
            logging.info("proxy is empty, sleep 30 * 60s")
            time.sleep(30 * 60)

    def get_proxy(self):
        try:
            item = self._proxy_cur.next()
            return item['ip'], item['port'], u'http'
        except Exception, e:
            self.refresh_proxy()
            return self.get_proxy()

    def remove_proxy(self, ip, port):
        ProxyDB.remove_proxy(ip, port)
