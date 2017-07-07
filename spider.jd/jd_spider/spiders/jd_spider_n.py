# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

import scrapy
import json
import datetime

from ..items import ShellerInfoItem


class JDSpider(scrapy.Spider):
    name = "jd_spider_n"

    def start_requests(self):

        data1 = [
            {
                "category": "n.彩票.游戏.游戏周边",
                "url": "http://list.jd.com/list.html?cat=4938-9394-9392&go=0"
            },
            {
                "category": "n.彩票.游戏.单机游戏",
                "url": "http://list.jd.com/list.html?cat=4938-9394-9393&go=0"
            },
            {
                "category": "n.彩票.本地生活.健康丽人",
                "url": "http://list.jd.com/list.html?cat=4938-11760-12372&go=0"
            },
            {
                "category": "n.彩票.教育培训.早教幼教",
                "url": "http://list.jd.com/list.html?cat=4938-12316-12317&go=0"
            },
            {
                "category": "n.彩票.教育培训.中小学教育",
                "url": "http://list.jd.com/list.html?cat=4938-12316-13111&go=0"
            },
            {
                "category": "n.彩票.教育培训.语言/留学",
                "url": "http://list.jd.com/list.html?cat=4938-12316-12319&go=0"
            },
            {
                "category": "n.彩票.教育培训.学历教育",
                "url": "http://list.jd.com/list.html?cat=4938-12316-13112&go=0"
            },
            {
                "category": "n.彩票.教育培训.职业技能",
                "url": "http://list.jd.com/list.html?cat=4938-12316-13109&go=0"
            },
            {
                "category": "n.彩票.教育培训.兴趣爱好",
                "url": "http://list.jd.com/list.html?cat=4938-12316-13110&go=0"
            },
            {
                "category": "n.彩票.商旅服务.奖励旅游",
                "url": "http://list.jd.com/list.html?cat=4938-12420-12422&go=0"
            },
            {
                "category": "n.彩票.商旅服务.会议周边",
                "url": "http://list.jd.com/list.html?cat=4938-12420-12423&go=0"
            },
            {
                "category": "n.彩票.出行服务.机场服务",
                "url": "http://list.jd.com/list.html?cat=4938-4939-13234&go=0"
            },
            {
                "category": "n.彩票.签证门票.全球签证",
                "url": "http://list.jd.com/list.html?cat=4938-12300-12301&go=0"
            },

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
