# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

import scrapy
from _991144_spider.items import CompanyInfoItem


class _991144Spider(scrapy.Spider):
    name = "_991144_spider"

    def start_requests(self):
        _list = [
            {'sign': "A", 'pageNum': 402},
            {'sign': "B", 'pageNum': 1513},
            {'sign': "C", 'pageNum': 1134},
            {'sign': "D", 'pageNum': 1269},
            {'sign': "E", 'pageNum': 36},
            {'sign': "F", 'pageNum': 819},
            {'sign': "G", 'pageNum': 1793},
            {'sign': "H", 'pageNum': 2211},
            {'sign': "I", 'pageNum': 4},
            {'sign': "J", 'pageNum': 1638},
            {'sign': "K", 'pageNum': 331},
            {'sign': "L", 'pageNum': 1213},
            {'sign': "M", 'pageNum': 348},
            {'sign': "N", 'pageNum': 839},
            {'sign': "O", 'pageNum': 28},
            {'sign': "P", 'pageNum': 217},
            {'sign': "Q", 'pageNum': 673},
            {'sign': "R", 'pageNum': 227},
            {'sign': "S", 'pageNum': 4831},
            {'sign': "T", 'pageNum': 1001},
            {'sign': "U", 'pageNum': 3},
            {'sign': "V", 'pageNum': 2},
            {'sign': "W", 'pageNum': 1123},
            {'sign': "X", 'pageNum': 1267},
            {'sign': "Y", 'pageNum': 1394},
            {'sign': "Z", 'pageNum': 2087},
        ]

        for item in _list:
            sign = item.get('sign')
            pageNum = item.get('pageNum')
            for i in range(1, pageNum):
                url = "http://shop.99114.com/list/pinyin/%s_%d" % (sign, i)
                yield scrapy.Request(url, self.parse)

    def parse(self, response):
        company_list = response.xpath('//a/strong/text()').extract()
        for company_name in company_list:
            company = CompanyInfoItem()
            company['company_name'] = company_name
            yield company
