# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

import logging

from bs4 import BeautifulSoup
# from mredis import RedisClient
from site_client import SiteClient

from mongo import B2b10086DB


class Spider(object):
    def __init__(self):
        self._site_client = SiteClient(proxies={})
        pass

    def run(self):
        try:
            self.get_search()
        except Exception, e:
            logging.exception(e)
        pass

    def get_search(self):
        for i in range(1, 2880):
            try:
                response = self._site_client.get_search_list(i)
                self.parse_search_list(response)
            except Exception, e:
                logging.exception(e)

    def parse_search_list(self, response):
        logging.info("parse_search_list..........")

        soup = BeautifulSoup(response.content, 'lxml')
        # logging.info(response.content)

        tr_list = soup.select_one('table').select('tr')
        logging.info("+++++++++++++++++tr_list len=%s+++++++++++++++++++" % len(tr_list))
        for tr in tr_list:
            try:
                td_list = tr.select('td')
                company = {
                    u"采购需求单位": td_list[0].getText(),
                    u"公告类型": td_list[1].getText(),
                    # u"标题": td_list[2].getText(), # 标题不全
                    u"时间": td_list[3].getText(),
                }
                onclick = tr['onclick']
                id = onclick.split('\'')[1]  # selectResult('305911')
                url = "https://b2b.10086.cn/b2b/main/viewNoticeContent.html?noticeBean.id=" + id
                if B2b10086DB.find_one(url):
                    return
                company.update({u"url": url})
                company_detail = self.get_company(url)
                company.update(company_detail)
                B2b10086DB.upsert_company(company)

            except Exception, e:
                logging.exception(e)

    def get_company(self, url):
        logging.info("get_company.....%s........" % url)

        response = self._site_client.get_detail(url)
        # logging.debug(response.content)
        soup = BeautifulSoup(response.content, 'lxml')
        company = {u"url": url}

        title = soup.select_one('h1').getText()
        content = soup.select_one('td > div[style="width:90%;"]').prettify()

        company.update({
            u"title": title,
            u"content": content
        })

        return company
