# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

import logging

from bs4 import BeautifulSoup

from mongo import ChinataxDB
from site_client import SiteClient
import json


# from config import proxies

class Spider(object):
    def __init__(self):
        self._site_client = SiteClient()
        pass

    def run(self):
        try:
            # for page in range(1, 51):
            #     response = self._site_client.list_1(page)
            #     self.parse_list_1(response)

            for page in range(67225, 258986):
                try:
                    response = self._site_client.list_2(page, "2015")
                    self.parse_list_2(response)
                    # exit(1)
                except Exception, e:
                    logging.exception(e)
            for page in range(1, 1):
                response = self._site_client.list_2(page, "2014")
                self.parse_list_2(response)
        except Exception, e:
            logging.exception(e)
        pass

    def parse_list_1(self, response):
        logging.info("parse_list_1..........")
        soup = BeautifulSoup(response.content, 'lxml')
        # print response.content
        a_list = soup.select('table tr td[align="center"] a')
        # logging.debug("a list len: %s" % len(a_list))
        for a in a_list:
            href = a['href']
            url = "http://hd.chinatax.gov.cn/xxk/action/" + href
            company = self.get_company_1(url)
            ChinataxDB.upsert_company_1(company)
        pass

    def parse_list_2(self, response):
        logging.info("parse_list_2..........")
        soup = BeautifulSoup(response.content, 'lxml')

        table = soup.select_one('table[bgcolor="#FFFFFF"]')
        # print table
        tr_list = table.select('tr')
        logging.debug("len %s" % len(tr_list))
        for tr in tr_list:
            td_list = tr.select('td')
            assert len(td_list) == 3, "td_list error "
            company = {
                "number": td_list[0].getText(),
                "company_name": td_list[1].getText(),
                "year": td_list[2].getText()
            }
            ChinataxDB.upsert_company_2(company)
        pass

    # -------------company detail----------------
    def get_company_1(self, url):
        logging.info("get_company.....%s....." % url)

        response = self._site_client.get_detail_1(url)
        # logging.debug(response.content)
        soup = BeautifulSoup(response.content, 'lxml')

        company = {"url": url}
        tr_list = soup.select('table tr td table tr')
        # logging.debug("tr list len %s " % len(tr_list))
        for tr in tr_list:
            td_list = tr.select('td')
            # logging.debug(" len: %s" % len(td_list))
            if len(td_list) == 2:
                k = td_list[0].getText().strip()
                v = td_list[1].getText().strip()
                company.update({k: v})
        return company
