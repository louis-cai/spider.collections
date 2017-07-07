# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

import time
import urllib
import logging
from bs4 import BeautifulSoup

from mongo import ZhaopinDB, QianzhanDB

from site_client import SiteClient
from exception import Error302, Error403

from mredis import RedisClient

from config import username, password


class Spider(object):
    def __init__(self):
        self._client = SiteClient(username, password)
        pass

    def _get_company(self, company_url):
        # logging.debug("_get_company.......")
        response = self._client.get_company(company_url)

        soup = BeautifulSoup(response.text, 'lxml')

        company = {}

        logging.debug("company:->%s" % company)

        return company

    def _get_search(self):
        url = "http://search.qianlima.com/qlm_adv_se.jsp?kw1=&kw2=&kw3=&field=0&p_tflt=365&q_time_start=2015-08-16&q_time_end=2016-08-15&iarea=0&area=2&prg=0%3D3&x=64&y=14"

        # if RedisClient.get_search_url_key(url):
        #     return

        response = self._client.get_search(url)

        soup = BeautifulSoup(response.text, 'lxml')
        try:
            try:
                company_url = soup.select_one('td[class="gsmc"] a')['href']
                logging.info("company_url: %s" % company_url)
            except Exception, e:
                return
            if company_url.startswith('http://company.zhaopin.com'):
                # if RedisClient.get_company_url_key(company_url):
                #     return
                company = self._get_company(company_url)
                if company:
                    ZhaopinDB.upsert_company(company)  # upsert company
                    # RedisClient.set_company_url_key(company_url)
        except Error302, err:
            logging.exception("get_company Error302, company_name:->%s, e:->%s" % (search_key, err))
            raise err
        except Error403, err:
            logging.exception("get_company Error403, company_name:->%s, e:->%s" % (search_key, err))
            raise err
        except Exception, e:
            logging.exception("get_company exception, company_name:->%s, e:->%s" % (search_key, e))
            pass

    def run(self):
        logging.info("+++++++++++++run++++++++++++++++")
        try:
            self._client.login()

            # self._get_search()
            logging.info("++++++++++++++success finish!!!++++++++")
        except Error302, err:
            logging.error(err.message)
        except Error403, err:
            logging.error(err.message)
        except Exception, e:
            logging.exception(e.message)
            pass
