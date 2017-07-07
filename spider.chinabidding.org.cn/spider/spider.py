# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

import logging

from bs4 import BeautifulSoup
# from mredis import RedisClient
from site_client import SiteClient

from mongo import ChinabaddingDB


# from utils import get_1000_txt
# from get_proxy import GetProxy


# from get_search_key import GetSearchKey


# from config import proxies


class Spider(object):
    def __init__(self):
        self._site_client = SiteClient(proxies={})
        self.__VIEWSTATE = None
        pass

    def run(self):
        try:
            self.index()
            self.get_search()
        except Exception, e:
            logging.exception(e)
            pass
        pass

    def index(self):
        response = self._site_client.index()
        self.parse_search_list(response)
        pass

    def get_search(self):
        for i in range(99, 45009):
            url = "http://www.chinabidding.org.cn/LuceneSearch.aspx?kwd=&filter=b3-0-0-keyword-30"
            response = self._site_client.get_search_list(url, viewstate=self._VIEWSTATE, page=i)
            self.parse_search_list(response)

    def parse_search_list(self, response):
        logging.info("parse_search_list..........")

        soup = BeautifulSoup(response.content, 'lxml')
        logging.info(response.content)

        self._VIEWSTATE = soup.select_one('input[id="__VIEWSTATE"]')['value']


        tr_list = soup.select('table[id="TableList"] > tr')
        logging.info("+++++++++++++++++tr_list len=%s+++++++++++++++++++" % len(tr_list))
        for tr in tr_list:
            td_list = tr.select('td')
            if len(td_list) == 3:
                number = td_list[0].select_one('font').getText()
                a = td_list[1].select_one('a')
                time = td_list[2].select_one('font').getText()
                href = a["href"]
                url = "http://www.chinabidding.org.cn/" + href
                if ChinabaddingDB.find_one(url):
                    continue

                company = self.get_company(url)
                company.update({
                    "url": url,
                    "number": number,
                    "time": time
                })
                ChinabaddingDB.upsert_company(company)

    def get_company(self, url):
        logging.info("get_company.....%s........" % url)

        response = self._site_client.get_detail(url)
        # logging.debug(response.content)
        soup = BeautifulSoup(response.content, 'lxml')
        doutline = soup.select('div[class="doutline"]')

        company = {}

        title = soup.select_one('span[id="cphMain_tle"]').getText()

        company.update({
            "title": title
        })

        # table = soup.select_one('table[id="dinfo"]')
        # tr_list = table.select('tr')
        # for tr in tr_list:
        #     td_list = tr.select('td')
        #     k = td_list[0].getText()
        #     v = td_list[1].getText()
        #     company.update({
        #         k: v
        #     })

        area = soup.select_one('td[id="dtr"]').getText()  # 地区
        industry = soup.select_one('td[id="dtr"]').getText()  # 行业
        content = soup.select_one('td[id="content"]').prettify()  #

        company.update({
            "area": area,
            "industry": industry,
            "content": content
        })

        return company
