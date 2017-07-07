# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

import scrapy
import json
import datetime

from ..items import ShellerInfoItem


class JDSpider(scrapy.Spider):
    name = "jd_spider_k"

    def start_requests(self):

        data1 = [
            {
                "category": "k.食品.中外名酒.白酒",
                "url": "http://list.jd.com/list.html?cat=12259-12260-9435&go=0"
            },
            {
                "category": "k.食品.中外名酒.葡萄酒",
                "url": "http://list.jd.com/list.html?cat=12259-12260-9438&go=0"
            },
            {
                "category": "k.食品.中外名酒.洋酒",
                "url": "http://list.jd.com/list.html?cat=12259-12260-9437&go=0"
            },
            {
                "category": "k.食品.中外名酒.啤酒",
                "url": "http://list.jd.com/list.html?cat=12259-12260-9439&go=0"
            },
            {
                "category": "k.食品.中外名酒.黄酒/养生酒",
                "url": "http://list.jd.com/list.html?cat=12259-12260-9436&go=0"
            },
            {
                "category": "k.食品.中外名酒.收藏酒/陈年老酒",
                "url": "http://list.jd.com/list.html?cat=12259-12260-12261&go=0"
            },
            {
                "category": "k.食品.进口食品.牛奶",
                "url": "http://list.jd.com/list.html?cat=1320-5019-12215&go=0"
            },
            {
                "category": "k.食品.进口食品.饼干蛋糕",
                "url": "http://list.jd.com/list.html?cat=1320-5019-5020&go=0"
            },
            {
                "category": "k.食品.进口食品.糖果/巧克力",
                "url": "http://list.jd.com/list.html?cat=1320-5019-5021&go=0"
            },
            {
                "category": "k.食品.进口食品.休闲零食",
                "url": "http://list.jd.com/list.html?cat=1320-5019-5022&go=0"
            },
            {
                "category": "k.食品.进口食品.冲调饮品",
                "url": "http://list.jd.com/list.html?cat=1320-5019-5023&go=0"
            },
            {
                "category": "k.食品.进口食品.粮油调味",
                "url": "http://list.jd.com/list.html?cat=1320-5019-5024&go=0"
            },
            {
                "category": "k.食品.休闲食品.休闲零食",
                "url": "http://list.jd.com/list.html?cat=1320-1583-1590&go=0"
            },
            {
                "category": "k.食品.休闲食品.坚果炒货",
                "url": "http://list.jd.com/list.html?cat=1320-1583-1591&go=0"
            },
            {
                "category": "k.食品.休闲食品.肉干肉脯",
                "url": "http://list.jd.com/list.html?cat=1320-1583-1592&go=0"
            },
            {
                "category": "k.食品.休闲食品.蜜饯果干",
                "url": "http://list.jd.com/list.html?cat=1320-1583-1593&go=0"
            },
            {
                "category": "k.食品.休闲食品.糖果/巧克力",
                "url": "http://list.jd.com/list.html?cat=1320-1583-1594&go=0"
            },
            {
                "category": "k.食品.休闲食品.饼干蛋糕",
                "url": "http://list.jd.com/list.html?cat=1320-1583-1595&go=0"
            },
            {
                "category": "k.食品.休闲食品.无糖食品",
                "url": "http://list.jd.com/list.html?cat=1320-1583-7121&go=0"
            },
            {
                "category": "k.食品.地方特产.新疆",
                "url": "http://list.jd.com/list.html?cat=1320-1581-1589&go=0"
            },
            {
                "category": "k.食品.地方特产.四川",
                "url": "http://list.jd.com/list.html?cat=1320-1581-2669&go=0"
            },
            {
                "category": "k.食品.地方特产.云南",
                "url": "http://list.jd.com/list.html?cat=1320-1581-2670&go=0"
            },
            {
                "category": "k.食品.地方特产.湖南",
                "url": "http://list.jd.com/list.html?cat=1320-1581-2656&go=0"
            },
            {
                "category": "k.食品.地方特产.内蒙",
                "url": "http://list.jd.com/list.html?cat=1320-1581-2648&go=0"
            },
            {
                "category": "k.食品.地方特产.北京",
                "url": "http://list.jd.com/list.html?cat=1320-1581-2644&go=0"
            },
            {
                "category": "k.食品.地方特产.山西",
                "url": "http://list.jd.com/list.html?cat=1320-1581-2647&go=0"
            },
            {
                "category": "k.食品.地方特产.福建",
                "url": "http://list.jd.com/list.html?cat=1320-1581-2653&go=0"
            },
            {
                "category": "k.食品.地方特产.东北",
                "url": "http://list.jd.com/list.html?cat=1320-1581-4693&go=0"
            },
            {
                "category": "k.食品.地方特产.其他",
                "url": "http://list.jd.com/list.html?cat=1320-1581-12217&go=0"
            },
            {
                "category": "k.食品.茗茶.铁观音",
                "url": "http://list.jd.com/list.html?cat=1320-12202-12203&go=0"
            },
            {
                "category": "k.食品.茗茶.普洱",
                "url": "http://list.jd.com/list.html?cat=1320-12202-12204&go=0"
            },
            {
                "category": "k.食品.茗茶.龙井",
                "url": "http://list.jd.com/list.html?cat=1320-12202-12205&go=0"
            },
            {
                "category": "k.食品.茗茶.绿茶",
                "url": "http://list.jd.com/list.html?cat=1320-12202-12206&go=0"
            },
            {
                "category": "k.食品.茗茶.红茶",
                "url": "http://list.jd.com/list.html?cat=1320-12202-12207&go=0"
            },
            {
                "category": "k.食品.茗茶.乌龙茶",
                "url": "http://list.jd.com/list.html?cat=1320-12202-12208&go=0"
            },
            {
                "category": "k.食品.茗茶.花草茶",
                "url": "http://list.jd.com/list.html?cat=1320-12202-12209&go=0"
            },
            {
                "category": "k.食品.茗茶.花果茶",
                "url": "http://list.jd.com/list.html?cat=1320-12202-12210&go=0"
            },
            {
                "category": "k.食品.茗茶.黑茶",
                "url": "http://list.jd.com/list.html?cat=1320-12202-12212&go=0"
            },
            {
                "category": "k.食品.茗茶.白茶",
                "url": "http://list.jd.com/list.html?cat=1320-12202-12213&go=0"
            },
            {
                "category": "k.食品.茗茶.养生茶",
                "url": "http://list.jd.com/list.html?cat=1320-12202-12211&go=0"
            },
            {
                "category": "k.食品.茗茶.其他茶",
                "url": "http://list.jd.com/list.html?cat=1320-12202-12214&go=0"
            },
            {
                "category": "k.食品.饮料冲调.牛奶乳品",
                "url": "http://list.jd.com/list.html?cat=1320-1585-9434&go=0"
            },
            {
                "category": "k.食品.饮料冲调.饮料",
                "url": "http://list.jd.com/list.html?cat=1320-1585-1602&go=0"
            },
            {
                "category": "k.食品.饮料冲调.饮用水",
                "url": "http://list.jd.com/list.html?cat=1320-1585-10975&go=0"
            },
            {
                "category": "k.食品.饮料冲调.咖啡/奶茶",
                "url": "http://list.jd.com/list.html?cat=1320-1585-3986&go=0"
            },
            {
                "category": "k.食品.饮料冲调.蜂蜜/柚子茶",
                "url": "http://list.jd.com/list.html?cat=1320-1585-12200&go=0"
            },
            {
                "category": "k.食品.饮料冲调.冲饮谷物",
                "url": "http://list.jd.com/list.html?cat=1320-1585-1601&go=0"
            },
            {
                "category": "k.食品.饮料冲调.成人奶粉",
                "url": "http://list.jd.com/list.html?cat=1320-1585-12201&go=0"
            },
            {
                "category": "k.食品.粮油调味.米面杂粮",
                "url": "http://list.jd.com/list.html?cat=1320-1584-2675&go=0"
            },
            {
                "category": "k.食品.粮油调味.食用油",
                "url": "http://list.jd.com/list.html?cat=1320-1584-2676&go=0"
            },
            {
                "category": "k.食品.粮油调味.调味品",
                "url": "http://list.jd.com/list.html?cat=1320-1584-2677&go=0"
            },
            {
                "category": "k.食品.粮油调味.南北干货",
                "url": "http://list.jd.com/list.html?cat=1320-1584-2678&go=0"
            },
            {
                "category": "k.食品.粮油调味.方便食品",
                "url": "http://list.jd.com/list.html?cat=1320-1584-2679&go=0"
            },
            {
                "category": "k.食品.粮油调味.有机食品",
                "url": "http://list.jd.com/list.html?cat=1320-1584-2680&go=0"
            },
            {
                "category": "k.食品.生鲜食品.水果蔬菜",
                "url": "http://list.jd.com/list.html?cat=12218-12221&go=0"
            },
            {
                "category": "k.食品.生鲜食品.海鲜水产",
                "url": "http://list.jd.com/list.html?cat=12218-12222&go=0"
            },
            {
                "category": "k.食品.生鲜食品.海参",
                "url": "http://list.jd.com/list.html?cat=12218-12222-12240&go=0"
            },
            {
                "category": "k.食品.生鲜食品.牛排",
                "url": "http://list.jd.com/list.html?cat=12218-12223-12246&go=0"
            },
            {
                "category": "k.食品.生鲜食品.肉禽蛋奶",
                "url": "http://list.jd.com/list.html?cat=12218-12223&go=0"
            },
            {
                "category": "k.食品.生鲜食品.熟食腊味",
                "url": "http://list.jd.com/list.html?cat=12218-12224&go=0"
            },
            {
                "category": "k.食品.生鲜食品.环球美食",
                "url": "http://list.jd.com/list.html?cat=12218-12220&go=0"
            },
            {
                "category": "k.食品.生鲜食品.产地直供",
                "url": "http://list.jd.com/list.html?cat=12218-12219&go=0"
            },
            {
                "category": "k.食品.食品礼券.大闸蟹",
                "url": "http://list.jd.com/list.html?cat=1320-2641-2643&go=0"
            },
            {
                "category": "k.食品.食品礼券.粽子",
                "url": "http://list.jd.com/list.html?cat=1320-2641-4935&go=0"
            },
            {
                "category": "k.食品.食品礼券.月饼",
                "url": "http://list.jd.com/list.html?cat=1320-2641-2642&go=0"
            },
            {
                "category": "k.食品.食品礼券.卡券",
                "url": "http://list.jd.com/list.html?cat=1320-2641-12216&go=0"
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
