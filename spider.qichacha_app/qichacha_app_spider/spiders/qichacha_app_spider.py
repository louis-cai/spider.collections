# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

import scrapy
from ..utils import get_gb2312_txt
import json
import urllib

# from ..items import CompanyInfoItem


class QichachaSpider(scrapy.Spider):
    name = "qichacha_app_spider"

    def start_requests(self):

        txt = get_gb2312_txt()
        for i, element in enumerate(txt):
            if i % 2 == 0:
                search_key = txt[i:2]
                print "search_key: ", search_key
                search_key = u"乐游乐动"
                print "search_key: ", search_key
                url = "http://app.qichacha.com/enterprises/new/advancedSearch?searchIndex=default&pageIndex=1&token=61205bba56b250e989176f4619a34ac3&deviceId=V00IG%2FC%2F9fsDAFLGppYaSufx&sortField=&version=8.6.7&user=574d2af0a86c280043000228&startDateEnd=&industryCode=&province=&startDateBegin=&pageSize=10&isSortAsc=true&registCapiEnd=&registCapiBegin=&cityCode=&searchKey=" + urllib.quote(
                    search_key.encode('utf-8')) + "&subIndustryCode=&deviceType=android"
                print url
                # request = scrapy.Request(
                #     url,
                #     callback=self.parse
                # )
                # # request.meta['item_category'] = item['category']
                # # request.meta['item_category_num'] = item['category'][0:1]
                # yield request
                break

    def parse(self, response):
        print "response.body: ", response.body
        res_json = json.loads(response.body)

    def parse_company(self, response):
        pass
