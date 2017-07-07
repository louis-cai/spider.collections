# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

import logging

from bs4 import BeautifulSoup
# from mredis import RedisClient
from site_client import SiteClient

# from utils import get_1000_txt
# from get_proxy import GetProxy


# from get_search_key import GetSearchKey


# from config import proxies

from mongo import TjztbDB


class Spider(object):
    def __init__(self):
        self._site_client = SiteClient(proxies={})
        pass

    def run(self):
        try:
            self.get_search(50)
        except Exception, e:
            logging.exception(e)

    def run_crontab(self):
        try:
            self.get_search(5)
        except Exception, e:
            logging.exception(e)

    def get_search(self, max_page):
        for i in range(max_page):
            try:
                if i == 0:
                    url = "http://www.tjztb.gov.cn/zbgg1/index.shtml"
                else:
                    url = "http://www.tjztb.gov.cn/zbgg1/index_%s.shtml" % i
                response = self._site_client.get_search_list(url)
                self.parse_search_list(response)
            except Exception, e:
                logging.exception(e)

    def parse_search_list(self, response):
        logging.info("parse_search_list..........")

        soup = BeautifulSoup(response.content, 'lxml')

        a_list = soup.select('div[class="list_1_right_list"] ul li a')
        logging.info("+++++++++++++++++a_list len=%s+++++++++++++++++++" % len(a_list))
        for a in a_list:
            try:
                href = a["href"]
                url = "http://www.tjztb.gov.cn/zbgg1" + href[1:]
                self.get_company(url)
            except Exception, e:
                logging.exception(e)

    def get_company(self, url):
        logging.info("get_company.....%s........" % url)
        if TjztbDB.find_one(url):
            return
        company = {
            'url': url
        }
        response = self._site_client.get_detail(url)
        # logging.debug(response.content)
        soup = BeautifulSoup(response.content, 'lxml')
        right_fbz = soup.select_one('div[class="text_right_fbz"]').getText()
        logging.debug(right_fbz)
        company.update({
            "author": right_fbz.split()[0].split('：')[1],  # 发布者
            "from": right_fbz.split()[1].split('：')[1],  # 来源
            "date": right_fbz.split()[2].split('：')[1],  # 日期
        })

        text_bt = soup.select_one('div[class="text_bt"]').getText()
        text_content = soup.select_one('div[class="text_content"]').prettify()
        company.update({
            "title": text_bt,
            "content": text_content
        })

        TjztbDB.upsert_company(company)
        # return company
