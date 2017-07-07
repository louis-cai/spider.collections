# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

import scrapy
import json
import datetime

from ..items import ShellerInfoItem


class JDSpider(scrapy.Spider):
    name = "jd_spider_l"

    def start_requests(self):

        data1 = [
            {
                "category": "l.营养保健.营养健康.调节免疫",
                "url": "http://list.jd.com/list.html?cat=9192-9193-9201&go=0"
            },
            {
                "category": "l.营养保健.营养健康.调节三高",
                "url": "http://list.jd.com/list.html?cat=9192-9193-9203&go=0"
            },
            {
                "category": "l.营养保健.营养健康.缓解疲劳",
                "url": "http://list.jd.com/list.html?cat=9192-9193-12162&go=0"
            },
            {
                "category": "l.营养保健.营养健康.美体塑身",
                "url": "http://list.jd.com/list.html?cat=9192-9193-12163&go=0"
            },
            {
                "category": "l.营养保健.营养健康.美容养颜",
                "url": "http://list.jd.com/list.html?cat=9192-9193-9200&go=0"
            },
            {
                "category": "l.营养保健.营养健康.肝肾养护",
                "url": "http://list.jd.com/list.html?cat=9192-9193-9208&go=0"
            },
            {
                "category": "l.营养保健.营养健康.肠胃养护",
                "url": "http://list.jd.com/list.html?cat=9192-9193-9207&go=0"
            },
            {
                "category": "l.营养保健.营养健康.明目益智",
                "url": "http://list.jd.com/list.html?cat=9192-9193-9205&go=0"
            },
            {
                "category": "l.营养保健.营养健康.骨骼健康",
                "url": "http://list.jd.com/list.html?cat=9192-9193-9202&go=0"
            },
            {
                "category": "l.营养保健.营养健康.改善睡眠",
                "url": "http://list.jd.com/list.html?cat=9192-9193-9209&go=0"
            },
            {
                "category": "l.营养保健.营养健康.抗氧化",
                "url": "http://list.jd.com/list.html?cat=9192-9193-12164&go=0"
            },
            {
                "category": "l.营养保健.营养健康.耐缺氧",
                "url": "http://list.jd.com/list.html?cat=9192-9193-12165&go=0"
            },
            {
                "category": "l.营养保健.营养成分.维生素/矿物质",
                "url": "http://list.jd.com/list.html?cat=9192-9194-9216&go=0"
            },
            {
                "category": "l.营养保健.营养成分.蛋白质",
                "url": "http://list.jd.com/list.html?cat=9192-9194-9215&go=0"
            },
            {
                "category": "l.营养保健.营养成分.鱼油/磷脂",
                "url": "http://list.jd.com/list.html?cat=9192-9194-9221&go=0"
            },
            {
                "category": "l.营养保健.营养成分.螺旋藻",
                "url": "http://list.jd.com/list.html?cat=9192-9194-9222&go=0"
            },
            {
                "category": "l.营养保健.营养成分.番茄红素",
                "url": "http://list.jd.com/list.html?cat=9192-9194-9224&go=0"
            },
            {
                "category": "l.营养保健.营养成分.叶酸",
                "url": "http://list.jd.com/list.html?cat=9192-9194-12171&go=0"
            },
            {
                "category": "l.营养保健.营养成分.葡萄籽",
                "url": "http://list.jd.com/list.html?cat=9192-9194-9227&go=0"
            },
            {
                "category": "l.营养保健.营养成分.左旋肉碱",
                "url": "http://list.jd.com/list.html?cat=9192-9194-9214&go=0"
            },
            {
                "category": "l.营养保健.营养成分.辅酶Q10",
                "url": "http://list.jd.com/list.html?cat=9192-9194-9226&go=0"
            },
            {
                "category": "l.营养保健.营养成分.益生菌",
                "url": "http://list.jd.com/list.html?cat=9192-9194-12172&go=0"
            },
            {
                "category": "l.营养保健.营养成分.玛咖",
                "url": "http://list.jd.com/list.html?cat=9192-9194-12173&go=0"
            },
            {
                "category": "l.营养保健.营养成分.膳食纤维",
                "url": "http://list.jd.com/list.html?cat=9192-9194-12174&go=0"
            },
            {
                "category": "l.营养保健.营养成分.牛初乳",
                "url": "http://list.jd.com/list.html?cat=9192-9194-12177&go=0"
            },
            {
                "category": "l.营养保健.营养成分.胶原蛋白",
                "url": "http://list.jd.com/list.html?cat=9192-9194-9225&go=0"
            },
            {
                "category": "l.营养保健.营养成分.大豆异黄酮",
                "url": "http://list.jd.com/list.html?cat=9192-9194-12175&go=0"
            },
            {
                "category": "l.营养保健.营养成分.芦荟提取",
                "url": "http://list.jd.com/list.html?cat=9192-9194-12176&go=0"
            },
            {
                "category": "l.营养保健.营养成分.酵素",
                "url": "http://list.jd.com/list.html?cat=9192-9194-12178&go=0"
            },
            {
                "category": "l.营养保健.滋补养生.阿胶",
                "url": "http://list.jd.com/list.html?cat=9192-9195-12180&go=0"
            },
            {
                "category": "l.营养保健.滋补养生.蜂蜜/蜂产品",
                "url": "http://list.jd.com/list.html?cat=9192-9195-12186&go=0"
            },
            {
                "category": "l.营养保健.滋补养生.枸杞",
                "url": "http://list.jd.com/list.html?cat=9192-9195-12612&go=0"
            },
            {
                "category": "l.营养保健.滋补养生.燕窝",
                "url": "http://list.jd.com/list.html?cat=9192-9195-12179&go=0"
            },
            {
                "category": "l.营养保健.滋补养生.海参",
                "url": "http://list.jd.com/list.html?cat=9192-9195-12181&go=0"
            },
            {
                "category": "l.营养保健.滋补养生.冬虫夏草",
                "url": "http://list.jd.com/list.html?cat=9192-9195-9229&go=0"
            },
            {
                "category": "l.营养保健.滋补养生.人参/西洋参",
                "url": "http://list.jd.com/list.html?cat=9192-9195-9230&go=0"
            },
            {
                "category": "l.营养保健.滋补养生.三七",
                "url": "http://list.jd.com/list.html?cat=9192-9195-12613&go=0"
            },
            {
                "category": "l.营养保健.滋补养生.鹿茸",
                "url": "http://list.jd.com/list.html?cat=9192-9195-12183&go=0"
            },
            {
                "category": "l.营养保健.滋补养生.雪蛤",
                "url": "http://list.jd.com/list.html?cat=9192-9195-12614&go=0"
            },
            {
                "category": "l.营养保健.滋补养生.青钱柳",
                "url": "http://list.jd.com/list.html?cat=9192-9195-12615&go=0"
            },
            {
                "category": "l.营养保健.滋补养生.石斛/枫斗",
                "url": "http://list.jd.com/list.html?cat=9192-9195-12616&go=0"
            },
            {
                "category": "l.营养保健.滋补养生.灵芝/孢子粉",
                "url": "http://list.jd.com/list.html?cat=9192-9195-12184&go=0"
            },
            {
                "category": "l.营养保健.滋补养生.当归",
                "url": "http://list.jd.com/list.html?cat=9192-9195-12617&go=0"
            },
            {
                "category": "l.营养保健.滋补养生.养生茶饮",
                "url": "http://list.jd.com/list.html?cat=9192-9195-12182&go=0"
            },
            {
                "category": "l.营养保健.滋补养生.药食同源",
                "url": "http://list.jd.com/list.html?cat=9192-9195-12185&go=0"
            },
            {
                "category": "l.营养保健.成人用品.安全避孕",
                "url": "http://list.jd.com/list.html?cat=9192-9196-1502&go=0"
            },
            {
                "category": "l.营养保健.成人用品.验孕测孕",
                "url": "http://list.jd.com/list.html?cat=9192-9196-1503&go=0"
            },
            {
                "category": "l.营养保健.成人用品.人体润滑",
                "url": "http://list.jd.com/list.html?cat=9192-9196-1504&go=0"
            },
            {
                "category": "l.营养保健.成人用品.男用延时",
                "url": "http://list.jd.com/list.html?cat=9192-9196-12609&go=0"
            },
            {
                "category": "l.营养保健.成人用品.男用器具",
                "url": "http://list.jd.com/list.html?cat=9192-9196-1505&go=0"
            },
            {
                "category": "l.营养保健.成人用品.女用器具",
                "url": "http://list.jd.com/list.html?cat=9192-9196-12610&go=0"
            },
            {
                "category": "l.营养保健.成人用品.情趣内衣",
                "url": "http://list.jd.com/list.html?cat=9192-9196-1506&go=0"
            },
            {
                "category": "l.营养保健.保健器械.血压计",
                "url": "http://list.jd.com/list.html?cat=9192-9197-12189&go=0"
            },
            {
                "category": "l.营养保健.保健器械.血糖仪",
                "url": "http://list.jd.com/list.html?cat=9192-9197-12187&go=0"
            },
            {
                "category": "l.营养保健.保健器械.血氧仪",
                "url": "http://list.jd.com/list.html?cat=9192-9197-12587&go=0"
            },
            {
                "category": "l.营养保健.保健器械.体温计",
                "url": "http://list.jd.com/list.html?cat=9192-9197-12588&go=0"
            },
            {
                "category": "l.营养保健.保健器械.体重秤",
                "url": "http://list.jd.com/list.html?cat=9192-9197-12589&go=0"
            },
            {
                "category": "l.营养保健.保健器械.胎心仪",
                "url": "http://list.jd.com/list.html?cat=9192-9197-12590&go=0"
            },
            {
                "category": "l.营养保健.保健器械.呼吸制氧",
                "url": "http://list.jd.com/list.html?cat=9192-9197-12188&go=0"
            },
            {
                "category": "l.营养保健.保健器械.雾化器",
                "url": "http://list.jd.com/list.html?cat=9192-9197-12593&go=0"
            },
            {
                "category": "l.营养保健.保健器械.助听器",
                "url": "http://list.jd.com/list.html?cat=9192-9197-12594&go=0"
            },
            {
                "category": "l.营养保健.保健器械.轮椅",
                "url": "http://list.jd.com/list.html?cat=9192-9197-12595&go=0"
            },
            {
                "category": "l.营养保健.保健器械.拐杖",
                "url": "http://list.jd.com/list.html?cat=9192-9197-12596&go=0"
            },
            {
                "category": "l.营养保健.保健器械.中医保健",
                "url": "http://list.jd.com/list.html?cat=9192-9197-1509&go=0"
            },
            {
                "category": "l.营养保健.保健器械.养生器械",
                "url": "http://list.jd.com/list.html?cat=9192-9197-1508&go=0"
            },
            {
                "category": "l.营养保健.保健器械.理疗仪",
                "url": "http://list.jd.com/list.html?cat=9192%2C9197%2C12591&go=0 "
            },
            {
                "category": "l.营养保健.保健器械.家庭护理",
                "url": "http://list.jd.com/list.html?cat=9192-9197-2687&go=0"
            },
            {
                "category": "l.营养保健.保健器械.智能健康",
                "url": "http://list.jd.com/list.html?cat=9192-9197-12597&go=0"
            },
            {
                "category": "l.营养保健.护理护具.隐形眼镜",
                "url": "http://list.jd.com/list.html?cat=9192-12190-12599&go=0"
            },
            {
                "category": "l.营养保健.护理护具.护理液",
                "url": "http://list.jd.com/list.html?cat=9192-12190-12600&go=0"
            },
            {
                "category": "l.营养保健.护理护具.口罩",
                "url": "http://list.jd.com/list.html?cat=9192-12190-1517&go=0"
            },
            {
                "category": "l.营养保健.护理护具.眼罩/耳塞",
                "url": "http://list.jd.com/list.html?cat=9192-12190-12602&go=0"
            },
            {
                "category": "l.营养保健.护理护具.跌打损伤",
                "url": "http://list.jd.com/list.html?cat=9192-12190-1514&go=0"
            },
            {
                "category": "l.营养保健.护理护具.暖贴",
                "url": "http://list.jd.com/list.html?cat=9192-12190-12604&go=0"
            },
            {
                "category": "l.营养保健.护理护具.鼻喉护理",
                "url": "http://list.jd.com/list.html?cat=9192-12190-12605&go=0"
            },
            {
                "category": "l.营养保健.护理护具.眼部保健",
                "url": "http://list.jd.com/list.html?cat=9192-12190-1518&go=0"
            },
            {
                "category": "l.营养保健.护理护具.美体护理",
                "url": "http://list.jd.com/list.html?cat=9192-12190-12607&go=0"
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
