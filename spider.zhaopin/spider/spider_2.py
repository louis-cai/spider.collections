# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

import time
import urllib
import logging
from bs4 import BeautifulSoup

from mongo import ZhaopinDB

from site_client import SiteClient
from exception import Error302, Error403


class Spider(object):
    def __init__(self):
        self._client = SiteClient(proxies={})
        self._city_list = []
        self._industry_list = []
        pass

    def run(self):
        logging.info("+++++++++++++run++++++++++++++++")
        try:
            self.init()
            self._run()
            logging.info("++++++++++++++success finish!!!++++++++")
        except Error302, err:
            logging.error(err.message)
        except Error403, err:
            logging.error(err.message)
        except Exception, e:
            logging.exception(e.message)

    def init(self):

        response = self._client.get_init()

        soup = BeautifulSoup(response.content, 'lxml')

        city_div = soup.select_one('div[id="city"]')
        city_a_list = city_div.select('a')
        city_list = []
        for city_a in city_a_list:
            city_list.append(city_a['id'])
        self._city_list = city_list

        industry_div = soup.select_one('div[id="industry"]')
        industry_a_list = industry_div.select('a')
        industry_list = []
        for industry_a in industry_a_list:
            industry_list.append(industry_a['id'])
        self._industry_list = industry_list
        logging.info("---------------------------------------")
        logging.info("city_list: %s" % city_list)
        logging.info("industry_list: %s" % industry_list)
        logging.info("---------------------------------------")

    def _run(self):
        for city in self._city_list[18:]:
            for industry in self._industry_list:
                for page in range(0, 101):
                    url = "http://company.zhaopin.com/%s/%s/p%s/" % (city, industry, page)
                    try:
                        ret = self.next_page(url, city)
                        if ret == "break":
                            break
                    except Exception, e:
                        logging.exception(e)
                        pass

    def next_page(self, url, city):
        response = self._client.get_search(url)
        if response.status_code == 404:
            return "break"

        soup = BeautifulSoup(response.content, 'lxml')

        self.parse_search_list(soup, city)

    def parse_search_list(self, soup, city):
        a_list = soup.select('div[class="jobs-list-box"] > div > a')
        for a in a_list:
            href = a['href']
            if href.startswith('http://company.zhaopin.com'):
                company_id = href.split('.')[-2].split('/')[-1]
                if ZhaopinDB.check_have(company_id):
                    logging.debug("pass..................................")
                    continue
                try:
                    self._get_company(company_id, city)
                except Exception, e:
                    logging.exception(e)
                    pass
        pass

    def _get_company(self, company_id, city):
        logging.debug("_get_company.......company_id:%s " % company_id)
        company_url = "http://company.zhaopin.com/%s.htm" % company_id
        response = self._client.get_company(company_url)

        soup = BeautifulSoup(response.content, 'lxml')

        self.parse_company(soup, company_id, city)

    def parse_company(self, soup, company_id, city):
        company = {"company_id": company_id, "city": city}

        main_left_tag = soup.select_one('div[class="mainLeft"]')
        # logging.info(main_left_tag)
        div_tag = main_left_tag.select_one('div')
        # logging.info(div_tag)
        company_name = div_tag.select_one('h1').text.strip()
        company.update({'company_name': company_name})
        tr_list = div_tag.select('table[class="comTinyDes"] tr')
        for tr in tr_list:
            td_list = tr.select('td')
            title = td_list[0].select_one('span').text
            content = td_list[1].select_one('span').text
            if title == "公司性质：":
                company.update({'business_type': content})
                pass
            elif title == "公司规模：":
                company.update({'people_num': content})
                pass
            elif title == "公司行业：":
                company.update({'business_scope': content})
                pass
            elif title == "公司地址：":
                company.update({'business_address': content})
                pass
            elif title == "公司网站：":
                company.update({'site': content})
                pass
            else:
                logging.error("+++++++++++++++except title: %s+++++++++++++++++" % title)
                raise Exception("+++++++++++++++except title: %s+++++++++++++++++" % title)

        company.update({"content": soup.select_one('div[class="company-content"]').prettify()})

        ZhaopinDB.upsert_company(company)



        # def get_job(self, company_id):
        #     url = "http://sou.zhaopin.com/jobs/companysearch.ashx?CompID=%s" % company_id
        #     pass
