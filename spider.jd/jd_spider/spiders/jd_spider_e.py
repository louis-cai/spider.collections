# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

import scrapy
import json
import datetime

from ..items import ShellerInfoItem


class JDSpider(scrapy.Spider):
    name = "jd_spider_e"

    def start_requests(self):

        data1 = [
            {
                "category": "e.男装.女装.连衣裙",
                "url": "http://list.jd.com/list.html?cat=1315-1343-9719&go=0"
            },
            {
                "category": "e.男装.女装.T恤",
                "url": "http://list.jd.com/list.html?cat=1315-1343-1355&go=0"
            },
            {
                "category": "e.男装.女装.雪纺衫",
                "url": "http://list.jd.com/list.html?cat=1315-1343-9713&go=0"
            },
            {
                "category": "e.男装.女装.衬衫",
                "url": "http://list.jd.com/list.html?cat=1315-1343-1354&go=0"
            },
            {
                "category": "e.男装.女装.休闲裤",
                "url": "http://list.jd.com/list.html?cat=1315-1343-9717&go=0"
            },
            {
                "category": "e.男装.女装.牛仔裤",
                "url": "http://list.jd.com/list.html?cat=1315-1343-9715&go=0"
            },
            {
                "category": "e.男装.女装.针织衫",
                "url": "http://list.jd.com/list.html?cat=1315-1343-1356&go=0"
            },
            {
                "category": "e.男装.女装.短外套",
                "url": "http://list.jd.com/list.html?cat=1315-1343-9712&go=0"
            },
            {
                "category": "e.男装.女装.卫衣",
                "url": "http://list.jd.com/list.html?cat=1315-1343-9710&go=0"
            },
            {
                "category": "e.男装.女装.小西装",
                "url": "http://list.jd.com/list.html?cat=1315-1343-9711&go=0"
            },
            {
                "category": "e.男装.女装.风衣",
                "url": "http://list.jd.com/list.html?cat=1315-1343-9708&go=0"
            },
            {
                "category": "e.男装.女装.毛呢大衣",
                "url": "http://list.jd.com/list.html?cat=1315-1343-9706&go=0"
            },
            {
                "category": "e.男装.女装.半身裙",
                "url": "http://list.jd.com/list.html?cat=1315-1343-9720&go=0"
            },
            {
                "category": "e.男装.女装.短裤",
                "url": "http://list.jd.com/list.html?cat=1315-1343-11991&go=0"
            },
            {
                "category": "e.男装.女装.吊带/背心",
                "url": "http://list.jd.com/list.html?cat=1315-1343-11988&go=0"
            },
            {
                "category": "e.男装.女装.打底衫",
                "url": "http://list.jd.com/list.html?cat=1315-1343-11985&go=0"
            },
            {
                "category": "e.男装.女装.打底裤",
                "url": "http://list.jd.com/list.html?cat=1315-1343-9716&go=0"
            },
            {
                "category": "e.男装.女装.正装裤",
                "url": "http://list.jd.com/list.html?cat=1315-1343-9718&go=0"
            },
            {
                "category": "e.男装.女装.马甲",
                "url": "http://list.jd.com/list.html?cat=1315-1343-9714&go=0"
            },
            {
                "category": "e.男装.女装.大码女装",
                "url": "http://list.jd.com/list.html?cat=1315-1343-9722&go=0"
            },
            {
                "category": "e.男装.女装.中老年女装",
                "url": "http://list.jd.com/list.html?cat=1315-1343-9721&go=0"
            },
            {
                "category": "e.男装.女装.真皮皮衣",
                "url": "http://list.jd.com/list.html?cat=1315-1343-9707&go=0"
            },
            {
                "category": "e.男装.女装.皮草",
                "url": "http://list.jd.com/list.html?cat=1315-1343-11993&go=0"
            },
            {
                "category": "e.男装.女装.羊毛衫",
                "url": "http://list.jd.com/list.html?cat=1315-1343-11999&go=0"
            },
            {
                "category": "e.男装.女装.羊绒衫",
                "url": "http://list.jd.com/list.html?cat=1315-1343-11989&go=0"
            },
            {
                "category": "e.男装.女装.棉服",
                "url": "http://list.jd.com/list.html?cat=1315-1343-9705&go=0"
            },
            {
                "category": "e.男装.女装.羽绒服",
                "url": "http://list.jd.com/list.html?cat=1315-1343-3983&go=0"
            },
            {
                "category": "e.男装.女装.仿皮皮衣",
                "url": "http://list.jd.com/list.html?cat=1315-1343-11998&go=0"
            },
            {
                "category": "e.男装.女装.加绒裤",
                "url": "http://list.jd.com/list.html?cat=1315-1343-11987&go=0"
            },
            {
                "category": "e.男装.女装.婚纱",
                "url": "http://list.jd.com/list.html?cat=1315-1343-9723&go=0"
            },
            {
                "category": "e.男装.女装.旗袍/唐装",
                "url": "http://list.jd.com/list.html?cat=1315-1343-11986&go=0"
            },
            {
                "category": "e.男装.女装.礼服",
                "url": "http://list.jd.com/list.html?cat=1315-1343-11996&go=0"
            },
            {
                "category": "e.男装.女装.设计师/潮牌",
                "url": "http://list.jd.com/list.html?cat=1315-1343-12000&go=0"
            },
            {
                "category": "e.男装.男装.衬衫",
                "url": "http://list.jd.com/list.html?cat=1315-1342-1348&go=0"
            },
            {
                "category": "e.男装.男装.T恤",
                "url": "http://list.jd.com/list.html?cat=1315-1342-1349&go=0"
            },
            {
                "category": "e.男装.男装.牛仔裤",
                "url": "http://list.jd.com/list.html?cat=1315-1342-9735&go=0"
            },
            {
                "category": "e.男装.男装.休闲裤",
                "url": "http://list.jd.com/list.html?cat=1315-1342-9736&go=0"
            },
            {
                "category": "e.男装.男装.卫衣",
                "url": "http://list.jd.com/list.html?cat=1315-1342-9732&go=0"
            },
            {
                "category": "e.男装.男装.针织衫",
                "url": "http://list.jd.com/list.html?cat=1315-1342-1350&go=0"
            },
            {
                "category": "e.男装.男装.西服",
                "url": "http://list.jd.com/list.html?cat=1315-1342-9731&go=0"
            },
            {
                "category": "e.男装.男装.西裤",
                "url": "http://list.jd.com/list.html?cat=1315-1342-9737&go=0"
            },
            {
                "category": "e.男装.男装.POLO衫",
                "url": "http://list.jd.com/list.html?cat=1315-1342-9733&go=0"
            },
            {
                "category": "e.男装.男装.羽绒服",
                "url": "http://list.jd.com/list.html?cat=1315-1342-3982&go=0"
            },
            {
                "category": "e.男装.男装.西服套装",
                "url": "http://list.jd.com/list.html?cat=1315-1342-9738&go=0"
            },
            {
                "category": "e.男装.男装.真皮皮衣",
                "url": "http://list.jd.com/list.html?cat=1315-1342-12001&go=0"
            },
            {
                "category": "e.男装.男装.夹克",
                "url": "http://list.jd.com/list.html?cat=1315-1342-9730&go=0"
            },
            {
                "category": "e.男装.男装.风衣",
                "url": "http://list.jd.com/list.html?cat=1315-1342-9728&go=0"
            },
            {
                "category": "e.男装.男装.卫裤/运动裤",
                "url": "http://list.jd.com/list.html?cat=1315-1342-12003&go=0"
            },
            {
                "category": "e.男装.男装.短裤",
                "url": "http://list.jd.com/list.html?cat=1315-1342-12004&go=0"
            },
            {
                "category": "e.男装.男装.仿皮皮衣",
                "url": "http://list.jd.com/list.html?cat=1315-1342-9725&go=0"
            },
            {
                "category": "e.男装.男装.棉服",
                "url": "http://list.jd.com/list.html?cat=1315-1342-9724&go=0"
            },
            {
                "category": "e.男装.男装.马甲/背心",
                "url": "http://list.jd.com/list.html?cat=1315-1342-9734&go=0"
            },
            {
                "category": "e.男装.男装.毛呢大衣",
                "url": "http://list.jd.com/list.html?cat=1315-1342-9729&go=0"
            },
            {
                "category": "e.男装.男装.羊毛衫",
                "url": "http://list.jd.com/list.html?cat=1315-1342-12089&go=0"
            },
            {
                "category": "e.男装.男装.羊绒衫",
                "url": "http://list.jd.com/list.html?cat=1315-1342-9726&go=0"
            },
            {
                "category": "e.男装.男装.大码男装",
                "url": "http://list.jd.com/list.html?cat=1315-1342-9739&go=0"
            },
            {
                "category": "e.男装.男装.中老年男装",
                "url": "http://list.jd.com/list.html?cat=1315-1342-9740&go=0"
            },
            {
                "category": "e.男装.男装.工装",
                "url": "http://list.jd.com/list.html?cat=1315-1342-9742&go=0"
            },
            {
                "category": "e.男装.男装.设计师/潮牌",
                "url": "http://list.jd.com/list.html?cat=1315-1342-12005&go=0"
            },
            {
                "category": "e.男装.男装.唐装/中山装",
                "url": "http://list.jd.com/list.html?cat=1315-1342-9741&go=0"
            },
            {
                "category": "e.男装.男装.加绒裤",
                "url": "http://list.jd.com/list.html?cat=1315-1342-12002&go=0"
            },
            {
                "category": "e.男装.内衣.文胸",
                "url": "http://list.jd.com/list.html?cat=1315-1345-1364&go=0"
            },
            {
                "category": "e.男装.内衣.睡衣/家居服",
                "url": "http://list.jd.com/list.html?cat=1315-1345-1371&go=0"
            },
            {
                "category": "e.男装.内衣.男式内裤",
                "url": "http://list.jd.com/list.html?cat=1315-1345-9744&go=0"
            },
            {
                "category": "e.男装.内衣.女式内裤",
                "url": "http://list.jd.com/list.html?cat=1315-1345-9743&go=0"
            },
            {
                "category": "e.男装.内衣.塑身美体",
                "url": "http://list.jd.com/list.html?cat=1315-1345-9747&go=0"
            },
            {
                "category": "e.男装.内衣.文胸套装",
                "url": "http://list.jd.com/list.html?cat=1315-1345-12008&go=0"
            },
            {
                "category": "e.男装.内衣.情侣睡衣",
                "url": "http://list.jd.com/list.html?cat=1315-1345-12006&go=0"
            },
            {
                "category": "e.男装.内衣.吊带/背心",
                "url": "http://list.jd.com/list.html?cat=1315-1345-1365&go=0"
            },
            {
                "category": "e.男装.内衣.少女文胸",
                "url": "http://list.jd.com/list.html?cat=1315-1345-12009&go=0"
            },
            {
                "category": "e.男装.内衣.休闲棉袜",
                "url": "http://list.jd.com/list.html?cat=1315-1345-12010&go=0"
            },
            {
                "category": "e.男装.内衣.商务男袜",
                "url": "http://list.jd.com/list.html?cat=1315-1345-9745&go=0"
            },
            {
                "category": "e.男装.内衣.连裤袜/丝袜",
                "url": "http://list.jd.com/list.html?cat=1315-1345-9748&go=0"
            },
            {
                "category": "e.男装.内衣.美腿袜",
                "url": "http://list.jd.com/list.html?cat=1315-1345-9749&go=0"
            },
            {
                "category": "e.男装.内衣.打底裤袜",
                "url": "http://list.jd.com/list.html?cat=1315-1345-12013&go=0"
            },
            {
                "category": "e.男装.内衣.抹胸",
                "url": "http://list.jd.com/list.html?cat=1315-1345-9751&go=0"
            },
            {
                "category": "e.男装.内衣.内衣配件",
                "url": "http://list.jd.com/list.html?cat=1315-1345-12012&go=0"
            },
            {
                "category": "e.男装.内衣.大码内衣",
                "url": "http://list.jd.com/list.html?cat=1315-1345-12011&go=0"
            },
            {
                "category": "e.男装.内衣.打底衫",
                "url": "http://list.jd.com/list.html?cat=1315-1345-12014&go=0"
            },
            {
                "category": "e.男装.内衣.泳衣",
                "url": "http://list.jd.com/list.html?cat=1315-1345-9753&go=0"
            },
            {
                "category": "e.男装.内衣.秋衣秋裤",
                "url": "http://list.jd.com/list.html?cat=1315-1345-12015&go=0"
            },
            {
                "category": "e.男装.内衣.保暖内衣",
                "url": "http://list.jd.com/list.html?cat=1315-1345-1369&go=0"
            },
            {
                "category": "e.男装.内衣.情趣内衣",
                "url": "http://list.jd.com/list.html?cat=1315-1345-1368&go=0"
            },
            {
                "category": "e.男装.配饰.太阳镜",
                "url": "http://list.jd.com/list.html?cat=1315-1346-9790&go=0"
            },
            {
                "category": "e.男装.配饰.光学镜架/镜片",
                "url": "http://list.jd.com/list.html?cat=1315-1346-9789&go=0"
            },
            {
                "category": "e.男装.配饰.男士腰带/礼盒",
                "url": "http://list.jd.com/list.html?cat=1315-1346-12029&go=0"
            },
            {
                "category": "e.男装.配饰.防辐射眼镜",
                "url": "http://list.jd.com/list.html?cat=1315-1346-12019&go=0"
            },
            {
                "category": "e.男装.配饰.老花镜",
                "url": "http://list.jd.com/list.html?cat=1315-1346-12017&go=0"
            },
            {
                "category": "e.男装.配饰.女士丝巾/围巾/披肩",
                "url": "http://list.jd.com/list.html?cat=1315-1346-12021&go=0"
            },
            {
                "category": "e.男装.配饰.男士丝巾/围巾",
                "url": "http://list.jd.com/list.html?cat=1315-1346-12022&go=0"
            },
            {
                "category": "e.男装.配饰.棒球帽",
                "url": "http://list.jd.com/list.html?cat=1315-1346-9792&go=0"
            },
            {
                "category": "e.男装.配饰.遮阳帽",
                "url": "http://list.jd.com/list.html?cat=1315-1346-9794&go=0"
            },
            {
                "category": "e.男装.配饰.鸭舌帽",
                "url": "http://list.jd.com/list.html?cat=1315-1346-12023&go=0"
            },
            {
                "category": "e.男装.配饰.贝雷帽",
                "url": "http://list.jd.com/list.html?cat=1315-1346-12024&go=0"
            },
            {
                "category": "e.男装.配饰.礼帽",
                "url": "http://list.jd.com/list.html?cat=1315-1346-12025&go=0"
            },
            {
                "category": "e.男装.配饰.毛线帽",
                "url": "http://list.jd.com/list.html?cat=1315-1346-9793&go=0"
            },
            {
                "category": "e.男装.配饰.防晒手套",
                "url": "http://list.jd.com/list.html?cat=1315-1346-12028&go=0"
            },
            {
                "category": "e.男装.配饰.真皮手套",
                "url": "http://list.jd.com/list.html?cat=1315-1346-12026&go=0"
            },
            {
                "category": "e.男装.配饰.围巾/手套/帽子套装",
                "url": "http://list.jd.com/list.html?cat=1315-1346-1376&go=0"
            },
            {
                "category": "e.男装.配饰.遮阳伞/雨伞",
                "url": "http://list.jd.com/list.html?cat=1315-1346-12034&go=0"
            },
            {
                "category": "e.男装.配饰.女士腰带/礼盒",
                "url": "http://list.jd.com/list.html?cat=1315-1346-12030&go=0"
            },
            {
                "category": "e.男装.配饰.口罩",
                "url": "http://list.jd.com/list.html?cat=1315-1346-12035&go=0"
            },
            {
                "category": "e.男装.配饰.假领",
                "url": "http://list.jd.com/list.html?cat=1315-1346-12037&go=0"
            },
            {
                "category": "e.男装.配饰.毛线/布面料",
                "url": "http://list.jd.com/list.html?cat=1315-1346-12038&go=0"
            },
            {
                "category": "e.男装.配饰.领带/领结/领带夹",
                "url": "http://list.jd.com/list.html?cat=1315-1346-12039&go=0"
            },
            {
                "category": "e.男装.配饰.耳罩/耳包",
                "url": "http://list.jd.com/list.html?cat=1315-1346-12036&go=0"
            },
            {
                "category": "e.男装.配饰.袖扣",
                "url": "http://list.jd.com/list.html?cat=1315-1346-1378&go=0"
            },
            {
                "category": "e.男装.配饰.钥匙扣",
                "url": "http://list.jd.com/list.html?cat=1315-1346-12033&go=0"
            },
            {
                "category": "e.男装.童装童鞋.套装",
                "url": "http://list.jd.com/list.html?cat=1319-11842-11222&go=0"
            },
            {
                "category": "e.男装.童装童鞋.上衣",
                "url": "http://list.jd.com/list.html?cat=1319-11842-11223&go=0"
            },
            {
                "category": "e.男装.童装童鞋.运动鞋",
                "url": "http://list.jd.com/list.html?cat=1319-11842-11229&go=0"
            },
            {
                "category": "e.男装.童装童鞋.裤子",
                "url": "http://list.jd.com/list.html?cat=1319-11842-11224&go=0"
            },
            {
                "category": "e.男装.童装童鞋.内衣",
                "url": "http://list.jd.com/list.html?cat=1319-11842-11227&go=0"
            },
            {
                "category": "e.男装.童装童鞋.皮鞋/帆布鞋",
                "url": "http://list.jd.com/list.html?cat=1319-11842-11230&go=0"
            },
            {
                "category": "e.男装.童装童鞋.亲子装",
                "url": "http://list.jd.com/list.html?cat=1319-11842-4937&go=0"
            },
            {
                "category": "e.男装.童装童鞋.羽绒服/棉服",
                "url": "http://list.jd.com/list.html?cat=1319-11842-11226&go=0"
            },
            {
                "category": "e.男装.童装童鞋.运动服",
                "url": "http://list.jd.com/list.html?cat=1319-11842-11843&go=0"
            },
            {
                "category": "e.男装.童装童鞋.靴子",
                "url": "http://list.jd.com/list.html?cat=1319-11842-11231&go=0"
            },
            {
                "category": "e.男装.童装童鞋.演出服",
                "url": "http://list.jd.com/list.html?cat=1319-11842-11228&go=0"
            },
            {
                "category": "e.男装.童装童鞋.裙子",
                "url": "http://list.jd.com/list.html?cat=1319-11842-11225&go=0"
            },
            {
                "category": "e.男装.童装童鞋.功能鞋",
                "url": "http://list.jd.com/list.html?cat=1319-11842-11233&go=0"
            },
            {
                "category": "e.男装.童装童鞋.凉鞋",
                "url": "http://list.jd.com/list.html?cat=1319-11842-11232&go=0"
            },
            {
                "category": "e.男装.童装童鞋.配饰",
                "url": "http://list.jd.com/list.html?cat=1319-11842-3977&go=0"
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
