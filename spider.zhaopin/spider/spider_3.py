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
        self._index = 0
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
        while True:
            item = ZhaopinDB.get_one_company_id(self._index)
            company_id = item['company_id']
            if ZhaopinDB.find_company_id_have_crawl_job(company_id):
                logging.info("pass......company_id:%s" % company_id)
                self._index += 1
                continue
            self.job_list(company_id)
            ZhaopinDB.set_company_id_have_crawl_job(company_id)
            self._index += 1
            logging.info("+++++++++++++++++++++++++current index %d++++++++++++++++++++++++++++" % self._index)

    def job_list(self, company_id):
        url = "http://sou.zhaopin.com/jobs/companysearch.ashx?CompID=%s" % company_id
        self.next_job_list(url, company_id)

    def next_job_list(self, url, company_id):
        response = self._client.job_list(url)

        soup = BeautifulSoup(response.content, 'lxml')

        a_list = soup.select('td[class="zwmc"] > div > a')
        for a in a_list:
            href = a['href']
            if href.startswith('http://jobs.zhaopin.com'):
                if ZhaopinDB.check_have_job(href):
                    logging.debug('pass.........................')
                    continue
                try:
                    self.get_job(href, company_id)
                except Exception, e:
                    logging.exception(e)
                    pass

        try:
            next_page_href = soup.select_one('li[class="pagesDown-pos"] a[class="next-page"]')['href']
        except Exception, e:
            next_page_href = None
        if next_page_href:
            self.next_job_list(next_page_href, company_id)


    def get_job(self, url, company_id):
        job = {"url": url, "company_id": company_id}

        response = self._client.get_job(url)

        soup = BeautifulSoup(response.content, 'lxml')

        title = soup.select_one('div[class="top-fixed-box"] h1').getText()
        job.update({"title": title})
        span_list = soup.select_one('div[class="welfare-tab-box"]').select('span')
        tag_list = []
        for span in span_list:
            tag_list.append(span.getText())
        job.update({"tags": tag_list})
        li_list = soup.select_one('ul[class="terminal-ul clearfix"]').select('li')
        for li in li_list:
            span = li.select_one('span').getText().strip()
            strong = li.select_one('strong').getText().strip()
            k = span[:-1]
            v = strong
            job.update({k: v})

        content = soup.select_one('div[class="terminalpage-main clearfix"] div[class="tab-cont-box"]').prettify()

        job.update({"content": content})

        ZhaopinDB.upsert_job(job)
        pass