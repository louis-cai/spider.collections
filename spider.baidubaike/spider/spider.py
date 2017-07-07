# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

import logging

from bs4 import BeautifulSoup

from mongo import QianzhanDB, BaidubaikeDB
from mredis import RedisClient
from site_client import SiteClient
import time

from exception import Error500, ErrorStatusCode


class Spider(object):
    def __init__(self):
        self._client = SiteClient()

    def run(self):
        cur = QianzhanDB.get_all()
        for item in cur:
            try:
                search_key = item['company_name']
                logging.info("search key.........%s..........." % search_key)
                # search_key = "百度"
                if RedisClient.get_search_key(search_key):
                    continue
                company = self.get_company(search_key)
                if company:
                    BaidubaikeDB.upsert_compnay(company)
                # break
                RedisClient.set_search_key(search_key)
                time.sleep(1)
            except Exception, e:
                logging.info("********************")
                logging.exception(e)
                logging.info("********************")
                continue

    def get_company(self, search_key):
        logging.info("get_company.....%s............" % search_key)
        response = None
        try:
            response = self._client.get_search(search_key)
        except Error500, e:
            logging.error(e.message)
            return False
        except ErrorStatusCode, e:
            logging.error(e.message)
            exit(1)
        except Exception, e:
            logging.exception(e)
            exit(1)
        if not response:
            logging.info("response is None..exit....")
            # exit(1)
            time.sleep(10)
            return False
        logging.debug("++++url: %s+++++++" % response.url)

        if RedisClient.get_url(response.url):
            return False

        if response.url.find("/search/none") > 0:
            logging.info(".........not found company.........")
            RedisClient.set_url(response.url)
            return False
        elif response.url.find("baidu.com/view") > 0:
            logging.info(".........found view.........")
            pass
        elif response.url.find("baidu.com/item") > 0:
            logging.info(".........found item........")
            pass
        elif response.url.find("baidu.com/subview") > 0:
            logging.info(".........found subview........")
            pass
        elif response.url.find("baidu.com/error") > 0:
            logging.info(".........found error........")
            RedisClient.set_url(response.url)
            return False
        else:
            logging.warning("unknown response url:->%s" % response.url)
            exit(1)
            pass

        try:
            soup = BeautifulSoup(response.content, 'lxml')

            main_content = soup.select_one('div[class="main-content"]')
            if not main_content:
                logging.info("not found main_content.......")
                RedisClient.set_url(response.url)
                return False
            main_content_html = main_content.prettify()

            company_name = main_content.select_one('dl dd h1').text
            logging.info(company_name)
            lemma_summary = main_content.select_one('div[class="lemma-summary"]').text

            company = {
                "company_name": company_name,
                "lemma_summary": lemma_summary,
                "main_content": main_content_html,
                "url": response.url
            }

            basic_info = main_content.select_one('div[class="basic-info cmn-clearfix"]')
            if basic_info:
                dt_list = basic_info.select('dl dt')
                dd_list = basic_info.select('dl dd')
                for i in range(0, len(dt_list)):
                    dt = dt_list[i]
                    dd = dd_list[i]
                    company.update({dt.text: dd.text})
            RedisClient.set_url(response.url)
            return company
        except Exception, e:
            logging.exception(e)
            return False
