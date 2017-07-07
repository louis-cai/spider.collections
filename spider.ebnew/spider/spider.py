# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

import logging

from bs4 import BeautifulSoup
# from mredis import RedisClient
from site_client import SiteClient

from mongo import EbnewDB


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
        try:
            response = self._site_client.get_search_list()
            self.parse_search_list(response)
        except Exception, e:
            logging.exception(e)
        for i in range(1, 378833):
            logging.info("================%s================" % i)
            try:
                url = "http://www.ebnew.com/tradingIndex.view?key=&pubDateBegin=&pubDateEnd=&infoType=(0108%202903%203203%203303%203403%203503)&fundSourceCodes=&zone=&normIndustry=&bidModel=&timeType=&sortMethod=&currentPage=" + str(
                    i) + "&length=10"
                self.get_next(url)
            except Exception, e:
                logging.exception(e)

    def get_next(self, url):
        response = self._site_client.get_next(url)
        self.parse_search_list(response)

    def parse_search_list(self, response):
        logging.info("parse_search_list..........")

        soup = BeautifulSoup(response.content, 'lxml')
        # logging.info(response.content)

        a_list = soup.select('a[class="sj-blue3"]')
        logging.info("+++++++++++++++++a_list len=%s+++++++++++++++++++" % len(a_list))
        for a in a_list:
            href = a['href']
            url = href
            try:
                self.get_company(url)
            except Exception, e:
                logging.exception(e)
                # raise e

                # next_page_href = soup.select_one('i[class="pagedown"] a')['href']
                # next_page_url = "http://www.ebnew.com/" + next_page_href
                # self.get_next(next_page_url)

    def get_company(self, url):
        logging.info("get_company.....%s........" % url)

        if EbnewDB.find_one(url):
            logging.info("pass......................")
            # return
            exit(0)

        response = self._site_client.get_detail(url)
        # logging.debug(response.content)
        soup = BeautifulSoup(response.content, 'lxml')
        company = {u"url": url}

        tr_list = soup.select('table[class="zb_table"] tr')

        for tr in tr_list:
            th_list = tr.select('th')
            td_list = tr.select('td')
            for i in range(0, len(th_list)):
                th = th_list[i]
                td = td_list[i]
                company.update({
                    th.getText(): td.getText()
                })

        # td_list = tr_list[0].select('td')
        # company.update({u"加入日期": td_list[0].getText()})
        # company.update({u"截至日期": td_list[1].getText()})
        #
        # td_list = tr_list[1].select('td')
        # company.update({u"招标编号": td_list[0].getText()})
        # company.update({u"所属行业": td_list[1].select_one('a').getText()})
        #
        # td_list = tr_list[2].select('td')
        # company.update({u"地区": td_list[0].getText()})
        # company.update({u"采招类型": td_list[1].getText()})
        #
        # td = tr_list[3].select_one('td')
        # company.update({u"招标机构": td.getText()})
        #
        # td = tr_list[4].select_one('td')
        # a_list = td.select('a')
        # keyword_list = []
        # for a in a_list:
        #     keyword_list.append(a.getText())
        # company.update({u"关键词": keyword_list})

        content = soup.select_one('div[class="end_content"]')
        company.update({u"内容": content.prettify()})

        EbnewDB.upsert_company(company)

        # return company
