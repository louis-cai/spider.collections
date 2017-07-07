# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

import scrapy
import json
import datetime

from ..items import ShellerInfoItem


class JDSpider(scrapy.Spider):
    name = "jd_spider_o"

    def start_requests(self):

        data1 = [
            {
                "category": "o.理财.理财.票据理财",
                "url": "http://bill.jr.jd.com/buy/list.htm"
            },
            {
                "category": "o.理财.理财.基金理财",
                "url": "http://list.jd.com/list.html?cat=list.jr.jd.com/fundlist/1-11-112.htm&go=0"
            },
            {
                "category": "o.理财.白条.京东金采",
                "url": "http://jincai.jd.com/apply/list.html"
            }
        ]

        for data in data1:
            category = data['category']
            url = data['url']
            request = scrapy.Request(url, self.parse)
            request.meta['category'] = category
            yield request

    def parse(self, response):
        category = response.meta["category"]

        for gl_item in response.xpath('//div[@class="gl-i-wrap j-sku-item"]'):
            # is_jd_self = gl_item.xpath('.//div[@class="p-shop hide"]/span/em[@class="u-jd"]/text()')
            # if is_jd_self:
            #     continue
            url = 'http:' + gl_item.xpath('.//div[@class="p-img"]/a/@href').extract_first()
            # print "detail: ", url
            request = scrapy.Request(url, callback=self.parse_item_detail)
            request.meta["category"] = category
            yield request

        next_page = response.xpath('//a[@class="pn-next"]/@href')
        if next_page:
            url = response.urljoin(next_page.extract_first())
            # print "next page: ", url
            request = scrapy.Request(url, self.parse)
            request.meta["category"] = category
            yield request

    def parse_item_detail(self, response):
        category = response.meta["category"]
        # is_jd_self = response.xpath('//em[@class="u-jd"]/text()').extract_first()

        # if is_jd_self:
        #     print is_jd_self
        #     return

        sheller_info_item = ShellerInfoItem()
        sheller_info_item["category"] = category
        sheller_info_item["sheller_name"] = response.xpath("//div[@class='seller-infor']/a/@title").extract_first()
        sheller_info_item["sheller_url"] = "http:" + str(
            response.xpath("//div[@class='seller-infor']/a/@href").extract_first())
        sheller_info_item["shop_name"] = response.xpath('//span[@class="text J-shop-name"]/text()').extract_first()
        sheller_info_item["shop_address"] = response.xpath(
            '//span[@class="text J-shop-address"]/text()').extract_first()
        sheller_info_item['sheller_phone'] = response.xpath('//div[@class="seller-phone"]/text()').extract_first()
        sheller_info_item['insert_time'] = datetime.datetime.now().strftime('%Y-%m-%d')
        yield sheller_info_item

    def parse_store_detail(self, response):
        pass
