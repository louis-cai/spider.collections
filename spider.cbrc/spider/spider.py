# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

import logging

from bs4 import BeautifulSoup

from mongo import CbrcDB
from site_client import SiteClient
import json


# from config import proxies

class Spider(object):
    def __init__(self):
        self._site_client = SiteClient()
        pass

    def run(self):
        response = self._site_client.list(1, 0, 50000)
        self.parse_search_list(response, 1)

        response = self._site_client.list(3, 0, 50000)
        self.parse_search_list(response, 3)
        response = self._site_client.list(3, 50000, 50000)
        self.parse_search_list(response, 3)
        response = self._site_client.list(3, 100000, 50000)
        self.parse_search_list(response, 3)
        response = self._site_client.list(3, 150000, 50000)
        self.parse_search_list(response, 3)
        response = self._site_client.list(3, 200000, 50000)
        self.parse_search_list(response, 3)

        response = self._site_client.list(7, 0, 50000)
        self.parse_search_list(response, 7)

        response = self._site_client.list(9, 0, 50000)
        self.parse_search_list(response, 9)
        pass

    def run_crontab(self):
        response = self._site_client.list(1, 0, 1000)
        self.parse_search_list(response, 1)
        response = self._site_client.list(3, 0, 1000)
        self.parse_search_list(response, 3)
        response = self._site_client.list(7, 0, 1000)
        self.parse_search_list(response, 7)
        response = self._site_client.list(9, 0, 1000)
        self.parse_search_list(response, 9)
        pass

    def parse_search_list(self, response, useState):
        logging.info("parse_search_list..........")
        # logging.debug(response.content)

        # j = json.loads(response.text)
        # root_list = j['root']
        root = u"[" + response.text.split(u'[')[1].split(u']')[0] + u"]"
        # logging.debug(root)
        root_list = json.loads(root, 'utf-8')

        for item in root_list:
            flowNo = item['flowNo']

            if CbrcDB.find_flowNo(flowNo, useState):
                continue
            try:
                company = self.get_company(useState, flowNo)

                if useState == 1:
                    CbrcDB.upsert_company_1(company)  # 近期机构设立情况
                elif useState == 3:
                    CbrcDB.upsert_company_3(company)  # 机构持有列表
                elif useState == 7:
                    CbrcDB.upsert_company_7(company)  # 机构推出列表
                elif useState == 9:
                    CbrcDB.upsert_company_9(company)  # 失控情况
                else:
                    raise Exception("unknonw useState")
            except Exception, e:
                logging.exception(e)
                continue


    # -------------company detail----------------
    def get_company(self, useState, flowNo):
        logging.info("get_company.....%s....%s......" % (useState, flowNo))

        response = self._site_client.get_detail(useState, flowNo)
        # logging.debug(response.content)
        soup = BeautifulSoup(response.content, 'lxml')

        company = {}
        tr_list = soup.select('tr')
        for tr in tr_list:
            td_list = tr.select('td')
            if len(td_list) == 2:
                # logging.debug("i: %s, len: %s" % (i, len(t/d_list)))
                k = td_list[0].getText().strip()[:-1]
                v = td_list[1].getText().strip()
                company.update({k: v})

        return company
