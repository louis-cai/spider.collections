# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

import logging

from bs4 import BeautifulSoup

from exception import Error302, Error403
from mongo import ChinabiddingDB
from site_client import SiteClient


class Spider(object):
    def __init__(self):
        self._client = SiteClient()
        pass

    def _get_company(self, detail_url):

        response = self._client._verify_get(detail_url)

        soup = BeautifulSoup(response.content, 'lxml')

        company = {}

        company.update({
            "title": soup.select_one('h1').text
        })

        detail = soup.select_one('section')

        company.update({
            "detail": detail.prettify()
        })

        return company

    def _get_search(self, current_page):
        logging.info("++++++++%s" % current_page)
        url = "http://www.chinabidding.com/search/proj.htm"

        form_data = {
            "fullText": "",
            "pubDate": "",
            "infoClassCodes": "0108",
            "normIndustry": "",
            "zoneCode": "",
            "fundSourceCodes": "",
            "poClass": "",
            "rangeType": "",
            "currentPage": "%s" % current_page  # 1,...
        }
        response = self._client._verify_post(url, form_data)

        soup = BeautifulSoup(response.content, 'lxml')

        a_list = soup.select('a[class="as-pager-item"]')
        for a in a_list:
            try:

                detail_url = a['href']

                if ChinabiddingDB.get_one(detail_url):
                    continue

                logging.info("detail_url: %s" % detail_url)

                result = {}
                result.update({
                    "detail_url": detail_url
                })
                result.update({
                    "time": a.select_one('h5 span[class="time"]').text
                })
                result.update({
                    "industry": a.select('div[class="as-p-ft"] dl dd span strong')[0].text,
                    "province": a.select('div[class="as-p-ft"] dl dd span strong')[1].text
                })

                company = self._get_company(detail_url)

                result.update(company)

                ChinabiddingDB.upsert_result(result)

            except Exception, e:
                logging.exception("get_company exception, e:->%s" % e)
                pass

    def _run(self):
        for current_page in range(1, 100):
            try:
                self._get_search(current_page)
            except Exception, e:
                logging.exception(e)

    def run(self):
        logging.info("+++++++++++++run++++++++++++++++")
        try:
            self._run()
            logging.info("++++++++++++++success finish!!!++++++++")
        except Error302, err:
            logging.error(err.message)
        except Error403, err:
            logging.error(err.message)
        except Exception, e:
            logging.exception(e.message)
            pass
