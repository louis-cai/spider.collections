# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

from mongo import ProxyDB


class GetProxy(object):
    def __init__(self):
        self._proxy_cur = None
        self.refresh_proxy()
        pass

    def refresh_proxy(self):
        self._proxy_cur = ProxyDB.get_all()

    def get_proxy(self):
        try:
            item = self._proxy_cur.next()
            return item['ip'], item['port'], u'http'
        except Exception, e:
            self.refresh_proxy()
            return self.get_proxy()
