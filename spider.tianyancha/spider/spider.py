# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

import time
import urllib
import logging
from PIL import Image
from bs4 import BeautifulSoup
from urlparse import urljoin

from mongo import DB
from exception import Error302, Error403, Error400, Error404
from mredis import RedisClient
# from captcha import read_img_file_to_string
from web_driver import new_webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from config import proxy_ip, proxy_port, proxy_type, max_thread_num
import threadpool
from utils import get_1000_txt


class Spider(object):
    def __init__(self):
        self._txt = get_1000_txt()
        self._webdriver = new_webdriver(proxy_ip, proxy_port, proxy_type)
        pass

    def run(self):
        self._run()
        pass

    def _run(self):
        for i in range(0, len(self._txt)):
            if i % 2 == 0:
                j = i + 1
                logging.info("(i, j):->(%s, %s)" % (i, j))
                search_key = self._txt[i] + self._txt[j]

                # if RedisClient.get_search_key(search_key):
                #     continue

                try:
                    self.search(search_key)

                    # RedisClient.set_search_key(search_key)

                except Exception, e:
                    logging.exception("search->%s" % e)

    def search(self, search_key):
        logging.info("search+++++%s" % search_key)
        try:
            url = "http://bj.tianyancha.com/search/p1?key=" + search_key
            self._search(url)
        except Exception, e:
            logging.exception("_search->%s" % e)

    def _search(self, url):

        self._webdriver.get(url)
        WebDriverWait(self._webdriver, 60 * 1).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "search_pager  ng-scope")))
        page_source = self._webdriver.page_source
        self.parse_search(page_source)

        # next page

    def parse_search(self, page_source):
        soup = BeautifulSoup(page_source, 'lxml')
        div_list = soup.select(
            'div[class="b-c-white search_result_container"] div[class="search_result_single ng-scope"]')
        for div in div_list:
            href = div.select_one('div div a')['href']
            company_name = div.select_one('div div a span').text.strip()
            title_list = div.select('div div div[class="title"]')
            legal_representative = title_list[0].select_one('span').text.strip()
            industry = title_list[1].select_one('span').text.strip()
            state = title_list[2].select_one('span').text.strip()
            province = div.select_one(
                'div[class="search_base col-xs-2 search_repadding2 text-right c3 ng-binding"]').text.strip()

            company = {
                "company_name": company_name,
                "url": href,
                "legal_representative": legal_representative,
                "industry": industry,
                "state": state,
                "province": province
            }

            DB.upsert_company(company)
