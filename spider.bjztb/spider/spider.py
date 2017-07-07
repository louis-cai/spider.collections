# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

import logging

from bs4 import BeautifulSoup
# from mredis import RedisClient
from site_client import SiteClient

from mongo import BjztbDB


# from utils import get_1000_txt
# from get_proxy import GetProxy


# from get_search_key import GetSearchKey


# from config import proxies


class Spider(object):
    def __init__(self):
        self._site_client = SiteClient(proxies={})
        pass

    def run(self):
        try:
            # self.get_search("zbjg")
            self.get_search("zbjg_2015")
        except Exception, e:
            logging.exception(e)

    def get_search(self, year):
        for i in range(8):
            try:
                if i == 0:
                    url = "http://www.bjztb.gov.cn/%s/index.htm" % year
                else:
                    url = "http://www.bjztb.gov.cn/%s/index_%s.htm" % (year, i)
                response = self._site_client.get_search_list(url)
                self.parse_search_list(response, year)
            except Exception, e:
                logging.exception(e)

    def parse_search_list(self, response, year):
        logging.info("parse_search_list..........")

        soup = BeautifulSoup(response.content, 'lxml')

        a_list = soup.select('td a.bt14')
        logging.info("+++++++++++++++++a_list len=%s+++++++++++++++++++" % len(a_list))
        for a in a_list:
            href = a["href"]
            if href == "http://www.bjztb.gov.cn/zbjg/":
                continue
            url = "http://www.bjztb.gov.cn/" + year + href[1:]
            try:
                self.get_company(url)
            except Exception, e:
                logging.exception(e)

    def get_company(self, url):
        logging.info("get_company.....%s........" % url)
        if BjztbDB.find_one(url):
            return
        company = {
            'url': url
        }
        response = self._site_client.get_detail(url)
        # logging.debug(response.content)
        soup = BeautifulSoup(response.content, 'lxml')
        biaoti = soup.select('td[class="biaoti"]')[1].getText()
        logging.debug(biaoti)
        company.update({
            "biaoti": biaoti
        })

        td_list = soup.select('body > center > table')[2].select('table')[3].select('tr td')

        t_1 = td_list[1].getText().split(u'：')[1]
        t_2 = td_list[3].getText().split(u'：')[1]
        t_3 = td_list[5].getText().split(u'：')[1]

        company.update({
            u"发布日期": t_1,
            u"项目单位": t_2,
            u"招标代理机构": t_3
        })

        td = soup.select('body > center > table')[2].select('table')[4].select_one('table').select('tr')[1].select_one(
            'td')

        company.update({
            "content": td.prettify()
        })

        # p_l = td.select('p')
        # company.update({
        #     "content": p_l[0].getText(),
        # })
        # for p in p_l[1:]:
        #     t = p.getText()
        #     k_v = t.split('：')
        #     company.update({
        #         k_v[0]: k_v[1]
        #     })

        BjztbDB.upsert_company(company)
        # return company
