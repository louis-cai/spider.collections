# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

import random
import time
import logging

from mongo import QyxybaicDB


class GetSearchKey(object):
    def __init__(self):
        # self._search_key_cur = None
        # self.refresh_search_key()
        pass

    # def refresh_search_key(self):
    #     self._search_key_cur = QianzhanDB.get_all()
    #     if self._search_key_cur.count() == 0:
    #         logging.info("search_key is empty, sleep 30 * 60s")
    #         time.sleep(30 * 60)

    def get_reg_bus_ent_id(self):
        # try:
        #     item = self._search_key_cur[random.randint(self._search_key_cur.count())]
        #     return item['company_name']
        # except Exception, e:
        #     self.refresh_search_key()
        #     return self.get_search_key()

        # i = random.randint(1, 19800)
        # item = QyxybaicDB.get_one(i)[0]

        item = QyxybaicDB.get_random_one()
        return item['reg_bus_ent_id']



        # try:
        #     cur = QyxybaicDB.get_all()
        #     return cur.next()
        # except Exception, e:
        #     logging.info("sleep 10s ..........")
        #     time.sleep(10)
        #     return self.get_reg_bus_ent_id()
