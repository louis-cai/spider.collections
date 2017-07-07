# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

import scrapy

from ..items import CompanyInfoItem

import time
import json


class NeeqSpider(scrapy.Spider):
    name = "neeq_spider"

    def start_requests(self):
        for i in range(0, 387):
            # url = "http://www.neeq.com.cn/nqhqController/nqhq.do?callback=jQuery183011897954367866181_1467712820587&page=" \
            #       + str(i) \
            #       + "&type=G&zqdm=&sortfield=&sorttype=&xxfcbj=&keyword=&_=" + str(time.time())

            # url = "http://www.neeq.com.cn/nqxxController/nqxx.do?callback=jQuery183023233682723406157_1468566380174&page=" + str(
            #     i) + "&typejb=T&xxzqdm=&xxzrlx=&xxhyzl=&xxssdq=&sortfield=xxzqdm&sorttype=asc&dicXxzbqs=&xxfcbj=&_=" + str(
            #     time.time())

            url = "http://www.neeq.com.cn/nqhqController/nqhq.do?callback=jQuery18308850322845747749_1468810679437&page=" + str(
                i) + "&type=G&zqdm=&sortfield=&sorttype=&xxfcbj=&keyword=&_=" + str(time.time())

            req = scrapy.Request(url=url, callback=self.parse)
            # xxfcbj 字段标识, 1: 创新层; 0: 基础层
            yield req
            # break

    def parse(self, response):
        text = response.body
        text_json = text[42:-2]
        # print text_json
        json_obj = json.loads(text_json)
        content = json_obj['content']
        # print content
        for obj in content:
            url = "http://www.neeq.com.cn/nqhqController/detailCompany.do?callback=jQuery18305602641521534675_1468566896674&zqdm=" + obj.get(
                "hqzqdm") + "&_=" + str(time.time())
            req = scrapy.Request(url=url, callback=self.parse_detail)
            req.meta['listdata'] = obj
            yield req

    def parse_detail(self, response):
        text = response.body
        text_json = text[41:-1]
        json_obj = json.loads(text_json)

        json_obj["listdata"] = response.meta['listdata']

        yield json_obj
