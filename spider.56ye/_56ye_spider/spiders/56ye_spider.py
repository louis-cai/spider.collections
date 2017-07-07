# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

import scrapy
from _56ye_spider.items import CompanyInfoItem


class _56yeSpider(scrapy.Spider):
    name = "_56ye_spider"

    def start_requests(self):
        for i in range(1, 6251):
            url = "http://qiye.56ye.net/search.php?kw=&vip=0&type=0&catid=0&mode=0&areaid=0&size=0&mincapital=&maxcapital=&x=42&y=11&page=%d" % i
            yield scrapy.Request(url, self.parse)

    def parse(self, response):
        list_sel = response.xpath('//tr[@align="center"]')
        for sel in list_sel:
            company = CompanyInfoItem()
            company['company_name'] = sel.xpath(
                './td[@align="left"]/ul/li[1]/a/span/strong/text()').extract_first()
            company['business_scope'] = sel.xpath('./td[@align="left"]/ul/li[2]/text()').extract_first()
            company['province'] = sel.xpath('./td[@class="f_orange"]/text()').extract_first()

            url = sel.xpath('./td[@align="left"]/ul/li[1]/a/@href').extract_first()
            url += "introduce/"
            req = scrapy.Request(url, self.parse_company)
            req.meta['company'] = company
            yield req

    def parse_company(self, response):
        company = response.meta['company']

        company['introduce'] = response.xpath('//div[@class="main_body"][1]/div/table/tr/td').extract_first()
        company['company_name'] = response.xpath(
            '//div[@class="main_body"][2]/div/table[1]/tr[1]/td[2]/text()').extract_first()
        company['business_type'] = response.xpath(
            '//div[@class="main_body"][2]/div/table[1]/tr[1]/td[4]/text()').extract_first()
        company['city'] = response.xpath('//div[@class="main_body"][2]/div/table[1]/tr[2]/td[2]/text()').extract_first()
        company['people_num'] = response.xpath(
            '//div[@class="main_body"][2]/div/table[1]/tr[2]/td[4]/text()').extract_first()
        company['registered_capital'] = response.xpath(
            '//div[@class="main_body"][2]/div/table[1]/tr[3]/td[2]/text()').extract_first()
        company['register_date'] = response.xpath(
            '//div[@class="main_body"][2]/div/table[1]/tr[3]/td[4]/text()').extract_first()

        company['link_man'] = response.xpath('//div[@class="qy_body"]/div/ul/li[1]/text()').extract_first()

        company['phone'] = response.xpath('//div[@class="qy_body"]/div/ul/li[3]/text()').extract_first()

        yield company
