# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

import logging

from bs4 import BeautifulSoup
# from mredis import RedisClient
from site_client import SiteClient

from mongo import InnocomDB
import os

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
            self.index()
            # self.get_search()
        except Exception, e:
            logging.exception(e)
            pass
        pass

    def index(self):
        response = self._site_client.index()
        self.parse_search_list(response)
        pass

    def parse_search_list(self, response):
        logging.info("parse_search_list..........")

        content = response.content
        # logging.info(response.content)

        lines = content.split('\n')

        for line in lines:
            # logging.debug(line)
            if line.find('d.add') > 0:
                l = line.split('(')[1].split(')')[0].split(',')
                if len(l) >= 4 and len(l[3].strip()) > 3:
                    try:
                        self.get_detail(l[3][1:-1])
                    except Exception, e:
                        logging.exception(e)

    def get_detail(self, href):
        logging.info("get_company.....%s......" % href)
        url = "http://www.innocom.gov.cn" + href

        response = self._site_client.get_detail(url)

        # logging.debug(response.content)
        soup = BeautifulSoup(response.content, 'lxml')
        a_list = soup.select('div[id="content"] > a')
        for a in a_list:
            try:
                pdf_href = a['href']
                pdf_name = a.getText()
                if pdf_name.strip() != '':
                    pdf_url = url[:-38] + pdf_href
                    self.download_file(pdf_name, pdf_url)
            except Exception, e:
                logging.exception(e)

    def download_file(self, filename, url):
        logging.debug("%s: %s" % (filename, url))
        file_path = "pdfs/"
        l = url.split('gov.cn/')[1].split('/')
        file_path += l[0] + '/' + l[1] + '/' + l[2] + '/' + l[3] + '/' + l[4] + '/'

        response = self._site_client.get_file(url)

        os.makedirs(file_path)

        filename = file_path + filename

        logging.debug(filename)

        with open(filename, "wb") as f:
            f.write(response.content)
            f.close()
