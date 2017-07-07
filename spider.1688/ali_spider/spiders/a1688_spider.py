# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

import scrapy
import json
import datetime

from ..items import ShellerInfoItem

from ali_spider.helpers.file_helper import read_json_file


class A1688Spider(scrapy.Spider):
    name = "a1688_spider"

    def start_requests(self):
        # i = 0
        # for file in ["json/1.json", "json/2.json"]:
        #     json_obj = read_json_file(file)
        #     html = json_obj['content']
        #     # print html
        #     sel =scrapy.Selector(text=html)
        #     # print sel
        #
        #     for ul in sel.xpath("//ul"):
        #         for li in ul.xpath("./li"):
        #             category = "%s.%s" % (i, li.xpath('./a/text()').extract_first())
        #             url = "http:" + li.xpath('./a/@href').extract_first()
        #             # print category, url
        #             request = scrapy.Request(url, self.parse)
        #             request.meta['category'] = category
        #             yield request
        #
        #         i += 1
        print "start request"
        yield scrapy.Request(
            "http://s.1688.com/selloffer/offer_search.htm?earseDirect=false&sign2=20&keywords=%B7%FE%D7%B0%B0%FC%D7%B0%B4%FC+%CB%DC%C1%CF&from=marketSearch&n=y&filt=y",
            self.parse)

    def parse(self, response):
        print "parse"
        pass

    def parse_item_detail(self, response):
        pass

    def parse_store_detail(self, response):
        pass
