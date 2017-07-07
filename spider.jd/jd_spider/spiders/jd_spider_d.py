# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

import scrapy
import json
import datetime

from ..items import ShellerInfoItem


class JDSpider(scrapy.Spider):
    name = "jd_spider_d"

    def start_requests(self):

        data1 = [
            {
                "category": "d.家居.厨具.烹饪锅具",
                "url": "http://list.jd.com/list.html?cat=6196-6197&go=0"
            },
            {
                "category": "d.家居.厨具.刀剪菜板",
                "url": "http://list.jd.com/list.html?cat=6196-6198&go=0"
            },
            {
                "category": "d.家居.厨具.厨房配件",
                "url": "http://list.jd.com/list.html?cat=6196-6214&go=0"
            },
            {
                "category": "d.家居.厨具.水具酒具",
                "url": "http://list.jd.com/list.html?cat=6196-6219&go=0"
            },
            {
                "category": "d.家居.厨具.餐具",
                "url": "http://list.jd.com/list.html?cat=6196-6227&go=0"
            },
            {
                "category": "d.家居.厨具.茶具/咖啡具",
                "url": "http://list.jd.com/list.html?cat=6196-11143&go=0"
            },
            {
                "category": "d.家居.家装建材.灯饰照明",
                "url": "http://list.jd.com/list.html?cat=9855-9856&go=0"
            },
            {
                "category": "d.家居.家装建材.厨房卫浴",
                "url": "http://list.jd.com/list.html?cat=9855-9857&go=0"
            },
            {
                "category": "d.家居.家装建材.五金工具",
                "url": "http://list.jd.com/list.html?cat=9855-9858&go=0"
            },
            {
                "category": "d.家居.家装建材.电工电料",
                "url": "http://list.jd.com/list.html?cat=9855-9859&go=0"
            },
            {
                "category": "d.家居.家装建材.墙地面材料",
                "url": "http://list.jd.com/list.html?cat=9855-9860&go=0"
            },
            {
                "category": "d.家居.家装建材.装饰材料",
                "url": "http://list.jd.com/list.html?cat=9855-9861&go=0"
            },
            {
                "category": "d.家居.家装建材.装修服务",
                "url": "http://list.jd.com/list.html?cat=9855-9862&go=0"
            },
            {
                "category": "d.家居.家装建材.吸顶灯",
                "url": "http://list.jd.com/list.html?cat=9855-9856-9904&go=0"
            },
            {
                "category": "d.家居.家装建材.淋浴花洒",
                "url": "http://list.jd.com/list.html?cat=9855-9857-9907&go=0"
            },
            {
                "category": "d.家居.家装建材.开关插座",
                "url": "http://list.jd.com/list.html?cat=9855-9859-9926&go=0"
            },
            {
                "category": "d.家居.家装建材.油漆涂料",
                "url": "http://list.jd.com/list.html?cat=9855-9860-9931&go=0"
            },
            {
                "category": "d.家居.家装建材.龙头",
                "url": "http://list.jd.com/list.html?cat=9855-9857-9909&go=0"
            },
            {
                "category": "d.家居.家纺.床品套件",
                "url": "http://list.jd.com/list.html?cat=1620-1621-1626&go=0"
            },
            {
                "category": "d.家居.家纺.被子",
                "url": "http://list.jd.com/list.html?cat=1620-1621-1627&go=0"
            },
            {
                "category": "d.家居.家纺.枕芯",
                "url": "http://list.jd.com/list.html?cat=1620-1621-1628&go=0"
            },
            {
                "category": "d.家居.家纺.蚊帐",
                "url": "http://list.jd.com/list.html?cat=1620-1621-1632&go=0"
            },
            {
                "category": "d.家居.家纺.凉席",
                "url": "http://list.jd.com/list.html?cat=1620-1621-11963&go=0"
            },
            {
                "category": "d.家居.家纺.毛巾浴巾",
                "url": "http://list.jd.com/list.html?cat=1620-1621-1634&go=0"
            },
            {
                "category": "d.家居.家纺.床单被罩",
                "url": "http://list.jd.com/list.html?cat=1620-1621-1629&go=0"
            },
            {
                "category": "d.家居.家纺.床垫/床褥",
                "url": "http://list.jd.com/list.html?cat=1620-1621-1631&go=0"
            },
            {
                "category": "d.家居.家纺.毯子",
                "url": "http://list.jd.com/list.html?cat=1620-1621-1630&go=0"
            },
            {
                "category": "d.家居.家纺.抱枕靠垫",
                "url": "http://list.jd.com/list.html?cat=1620-1621-1633&go=0"
            },
            {
                "category": "d.家居.家纺.窗帘/窗纱",
                "url": "http://list.jd.com/list.html?cat=1620-1621-4952&go=0"
            },
            {
                "category": "d.家居.家纺.电热毯",
                "url": "http://list.jd.com/list.html?cat=1620-1621-2688&go=0"
            },
            {
                "category": "d.家居.家纺.布艺软饰",
                "url": "http://list.jd.com/list.html?cat=1620-1621-11962&go=0"
            },
            {
                "category": "d.家居.家具.卧室家具",
                "url": "http://list.jd.com/list.html?cat=9847-9848&go=0"
            },
            {
                "category": "d.家居.家具.客厅家具",
                "url": "http://list.jd.com/list.html?cat=9847-9849&go=0"
            },
            {
                "category": "d.家居.家具.餐厅家具",
                "url": "http://list.jd.com/list.html?cat=9847-9850&go=0"
            },
            {
                "category": "d.家居.家具.书房家具",
                "url": "http://list.jd.com/list.html?cat=9847-9851&go=0"
            },
            {
                "category": "d.家居.家具.储物家具",
                "url": "http://list.jd.com/list.html?cat=9847-9852&go=0"
            },
            {
                "category": "d.家居.家具.阳台/户外",
                "url": "http://list.jd.com/list.html?cat=9847-9853&go=0"
            },
            {
                "category": "d.家居.家具.商业办公",
                "url": "http://list.jd.com/list.html?cat=9847-9854&go=0"
            },
            {
                "category": "d.家居.家具.床",
                "url": "http://list.jd.com/list.html?cat=9847-9848-9863&go=0"
            },
            {
                "category": "d.家居.家具.床垫",
                "url": "http://list.jd.com/list.html?cat=9847-9848-9864&go=0"
            },
            {
                "category": "d.家居.家具.沙发",
                "url": "http://list.jd.com/list.html?cat=9847-9849-9870&go=0"
            },
            {
                "category": "d.家居.家具.电脑椅",
                "url": "http://list.jd.com/list.html?cat=9847-9851-9882&go=0"
            },
            {
                "category": "d.家居.家具.衣柜",
                "url": "http://list.jd.com/list.html?cat=9847-9848-11972&go=0"
            },
            {
                "category": "d.家居.家具.茶几",
                "url": "http://list.jd.com/list.html?cat=9847-9849-9872&go=0"
            },
            {
                "category": "d.家居.家具.电视柜",
                "url": "http://list.jd.com/list.html?cat=9847-9849-9873&go=0"
            },
            {
                "category": "d.家居.家具.餐桌",
                "url": "http://list.jd.com/list.html?cat=9847-9850-9877&go=0"
            },
            {
                "category": "d.家居.家具.电脑桌",
                "url": "http://list.jd.com/list.html?cat=9847-9851-11973&go=0"
            },
            {
                "category": "d.家居.家具.鞋架/衣帽架",
                "url": "http://list.jd.com/list.html?cat=9847-9852-9885&go=0"
            },
            {
                "category": "d.家居.灯具.台灯",
                "url": "http://list.jd.com/list.html?cat=1620-1623-1648&go=0"
            },
            {
                "category": "d.家居.灯具.吸顶灯",
                "url": "http://list.jd.com/list.html?cat=1620-1623-4954&go=0"
            },
            {
                "category": "d.家居.灯具.筒灯射灯",
                "url": "http://list.jd.com/list.html?cat=1620-1623-11971&go=0"
            },
            {
                "category": "d.家居.灯具.LED灯",
                "url": "http://list.jd.com/list.html?cat=1620-1623-4955&go=0"
            },
            {
                "category": "d.家居.灯具.节能灯",
                "url": "http://list.jd.com/list.html?cat=1620-1623-1649&go=0"
            },
            {
                "category": "d.家居.灯具.落地灯",
                "url": "http://list.jd.com/list.html?cat=1620-1623-1653&go=0"
            },
            {
                "category": "d.家居.灯具.五金电器",
                "url": "http://list.jd.com/list.html?cat=1620-1623-4956&go=0"
            },
            {
                "category": "d.家居.灯具.应急灯/手电",
                "url": "http://list.jd.com/list.html?cat=1620-1623-1654&go=0"
            },
            {
                "category": "d.家居.灯具.装饰灯",
                "url": "http://list.jd.com/list.html?cat=1620-1623-1650&go=0"
            },
            {
                "category": "d.家居.灯具.吊灯",
                "url": "http://list.jd.com/list.html?cat=1620-1623-1651&go=0"
            },
            {
                "category": "d.家居.灯具.氛围照明",
                "url": "http://list.jd.com/list.html?cat=1620-1623-6861&go=0"
            },
            {
                "category": "d.家居.生活日用.收纳用品",
                "url": "http://list.jd.com/list.html?cat=1620-1624-1655&go=0"
            },
            {
                "category": "d.家居.生活日用.雨伞雨具",
                "url": "http://list.jd.com/list.html?cat=1620-1624-1656&go=0"
            },
            {
                "category": "d.家居.生活日用.净化除味",
                "url": "http://list.jd.com/list.html?cat=1620-1624-1661&go=0"
            },
            {
                "category": "d.家居.生活日用.浴室用品",
                "url": "http://list.jd.com/list.html?cat=1620-1624-1657&go=0"
            },
            {
                "category": "d.家居.生活日用.洗晒/熨烫",
                "url": "http://list.jd.com/list.html?cat=1620-1624-1660&go=0"
            },
            {
                "category": "d.家居.生活日用.缝纫/针织用品",
                "url": "http://list.jd.com/list.html?cat=1620-1624-1658&go=0"
            },
            {
                "category": "d.家居.生活日用.清洁工具",
                "url": "http://list.jd.com/list.html?cat=1620-1625-1667&go=0"
            },
            {
                "category": "d.家居.家装软饰.桌布/罩件",
                "url": "http://list.jd.com/list.html?cat=1620-11158-11159&go=0"
            },
            {
                "category": "d.家居.家装软饰.地毯地垫",
                "url": "http://list.jd.com/list.html?cat=1620-11158-11160&go=0"
            },
            {
                "category": "d.家居.家装软饰.沙发垫套/椅垫",
                "url": "http://list.jd.com/list.html?cat=1620-11158-11161&go=0"
            },
            {
                "category": "d.家居.家装软饰.装饰字画",
                "url": "http://list.jd.com/list.html?cat=1620-11158-11163&go=0"
            },
            {
                "category": "d.家居.家装软饰.装饰摆件",
                "url": "http://list.jd.com/list.html?cat=1620-11158-11166&go=0"
            },
            {
                "category": "d.家居.家装软饰.手工/十字绣",
                "url": "http://list.jd.com/list.html?cat=1620-11158-11165&go=0"
            },
            {
                "category": "d.家居.家装软饰.相框/照片墙",
                "url": "http://list.jd.com/list.html?cat=1620-11158-11162&go=0"
            },
            {
                "category": "d.家居.家装软饰.墙贴/装饰贴",
                "url": "http://list.jd.com/list.html?cat=1620-11158-11965&go=0"
            },
            {
                "category": "d.家居.家装软饰.花瓶花艺",
                "url": "http://list.jd.com/list.html?cat=1620-11158-11967&go=0"
            },
            {
                "category": "d.家居.家装软饰.香薰蜡烛",
                "url": "http://list.jd.com/list.html?cat=1620-11158-11968&go=0"
            },
            {
                "category": "d.家居.家装软饰.节庆饰品",
                "url": "http://list.jd.com/list.html?cat=1620-11158-11164&go=0"
            },
            {
                "category": "d.家居.家装软饰.钟饰",
                "url": "http://list.jd.com/list.html?cat=1620-11158-11966&go=0"
            },
            {
                "category": "d.家居.家装软饰.帘艺隔断",
                "url": "http://list.jd.com/list.html?cat=1620-11158-11964&go=0"
            },
            {
                "category": "d.家居.家装软饰.创意家居",
                "url": "http://list.jd.com/list.html?cat=1620-11158-11969&go=0"
            },
            {
                "category": "d.家居.家装软饰.保暖防护",
                "url": "http://list.jd.com/list.html?cat=1620-11158-11167&go=0"
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
