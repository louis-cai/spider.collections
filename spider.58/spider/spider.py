# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

import logging

from bs4 import BeautifulSoup

from exception import Error302, Error403
from site_client import SiteClient

from mongo import Job58DB


class Spider(object):
    def __init__(self):
        self._client = SiteClient(proxies={})
        self._city_list = []
        self._industry_list = []
        pass

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

    def _run(self):
        city = "beijing"
        for page in range(0, 70):
            logging.info("current page .....................%s.........." % page)
            url = "http://bj.58.com/job/pn%s/" % page
            try:
                self.next_page(url, city)
            except Exception, e:
                logging.exception(e)
                pass

    def next_page(self, url, city):
        response = self._client.get_search(url)

        soup = BeautifulSoup(response.content, 'lxml')

        self.parse_search_list(soup, city)

    def parse_search_list(self, soup, city):
        a_list = soup.select('div[id="infolist"] > dl > dt > a')
        for a in a_list:
            href = a['href']

            try:
                self._get_job(href, city)
            except Exception, e:
                logging.exception(e)
                pass
        pass

    def _get_job(self, url, city):
        logging.debug("_get_job...... ")

        response = self._client.get_job(url)

        soup = BeautifulSoup(response.content, 'lxml')

        job_url = response.url.split('?')[0]

        self.parse_job(soup, job_url, city)

    def parse_job(self, soup, url, city):
        job = {u"job_url": url, u"city": city}

        title = soup.select_one('h1').getText()
        job.update({
            u"title": title
        })

        job.update({
            u"薪资待遇": soup.select_one('span[class="salaNum"]').getText()
        })

        job.update({
            u"学历要求": soup.select_one('div[class="xq"] div[class="fl"]')[0].getText().split('：')[1]
        })
        job.update({
            u"招聘职位": soup.select_one('div[class="xq"] div[class="w380"]')[1].getText().split('：')[1]
        })
        job.update({
            u"工作年限": soup.select_one('div[class="xq"] div[class="fl"]')[1].getText().split('：')[1]
        })
        job.update({
            u"工作地址": soup.select_one('div[class="xq"] > ul > li')[2].select('span')[1].getText()
        })

        span_list = soup.select_one('div[class="cbSum"] span')
        sbSum_list = []
        for span in span_list:
            sbSum_list.append(span.getText())

        job.update({
            u"福利待遇": sbSum_list
        })

        job.update({
            u"职位描述": soup.select_one('div[id="zhiwei"] div[class="posMsg borb"]').prettify()
        })

        company_a = soup.select_one('a[class="companyName"]')
        company_name = company_a.getText()
        company_url = company_a['href'].split('?')[0]

        job.update({
            u"公司名称": company_name,
            u"company_url": company_url
        })

        job.update({
            u"公司描述": soup.select_one('div[id="gongsi"]').prettify()
        })

        Job58DB.upsert_job(job)
