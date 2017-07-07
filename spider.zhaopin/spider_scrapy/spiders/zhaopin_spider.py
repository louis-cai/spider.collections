# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

import scrapy

from ..db.mongo import QianzhanDB
from ..items import CompanyInfoItem
from ..db.mredis import RedisClient
import urllib
import sys, os

class Zhaopinpider(scrapy.Spider):
    name = "zhaopin_spider"

    def start_requests(self):
        cur = QianzhanDB.get_companys()

        for item in cur:
            search_key = item['company_name']
            if RedisClient.get_search_key_key(search_key):
                continue
            # url = "http://sou.zhaopin.com/jobs/searchresult.ashx?kw=%s&sm=0&p=1" % search_key
            url = "http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E5%8C%97%E4%BA%AC&kw=" + urllib.quote(
                search_key.encode('utf-8')) + "&p=1&kt=2&isadv=0"
            request = scrapy.Request(
                url,
                callback=self.parse
            )
            request.meta['search_key'] = search_key
            yield request
            # break

    def parse(self, response):
        url = response.xpath('//td[@class="gsmc"]/a/@href').extract_first()

        companyInfoItem = CompanyInfoItem()
        search_key = response.meta['search_key']

        print "url: %s" % url

        if url and url.startswith('http://company.zhaopin.com'):
            request = scrapy.Request(
                url,
                callback=self.parse_company
            )
            request.meta['item'] = companyInfoItem
            request.meta['search_key'] = search_key
            yield request
        else:
            RedisClient.set_search_key_key(search_key)
            pass

    def parse_company(self, response):
        print "parse_company..."
        # print response.body
        companyInfoItem = response.meta['item']
        search_key = response.meta['search_key']
        print "body: ", response.body
        print response.xpath('//div[@class="mainLeft"]')
        print response.xpath('//div[@class="mainLeft"]/div[1]')
        print response.xpath('//div[@class="mainLeft"]/div[1]/h1[1]')
        print response.xpath('//div[@class="mainLeft"]/div[1]/h1[1]/text()')
        print response.xpath('//div[@class="mainLeft"]/div[1]/h1[1]/text()').extract_first()
        # sys.exit()
        os._exit()
        companyInfoItem['company_name'] = response.xpath('//div[@class="mainLeft"]').xpath(
            './div[1]/h1[1]/text()').extract_first().strip()

        table_sel = response.xpath('//div[@class="mainLeft"]').xpath('./div[1]/table[@class="comTinyDes"]')

        companyInfoItem['business_type'] = table_sel.xpath('./tr[1]/td[2]/span/text()').extract_first()
        companyInfoItem['people_num'] = table_sel.xpath('./tr[2]/td[2]/span/text()').extract_first()
        companyInfoItem['url'] = table_sel.xpath('./tr[3]/td[2]/span/a/text()').extract_first()
        companyInfoItem['business_scope'] = table_sel.xpath('./tr[4]/td[2]/span/text()').extract_first()
        companyInfoItem['business_address'] = table_sel.xpath('./tr[5]/td[2]/span/text()').extract_first()

        companyInfoItem['introduction'] = response.xpath(
            '//div[@class="mainLeft"]/div[@class="part2"]/div[@class="company-content"]').extract_first()

        RedisClient.set_search_key_key(search_key)
        yield companyInfoItem
