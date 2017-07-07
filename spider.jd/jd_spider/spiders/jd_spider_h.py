# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

import scrapy
import json
import datetime

from ..items import ShellerInfoItem


class JDSpider(scrapy.Spider):
    name = "jd_spider_h"

    def start_requests(self):

        data1 = [
            {
                "category": "h.运动户外.运动鞋包.休闲鞋",
                "url": "http://list.jd.com/list.html?cat=1318-12099-9754&go=0"
            },
            {
                "category": "h.运动户外.运动鞋包.篮球鞋",
                "url": "http://list.jd.com/list.html?cat=1318-12099-9757&go=0"
            },
            {
                "category": "h.运动户外.运动鞋包.板鞋",
                "url": "http://list.jd.com/list.html?cat=1318-12099-12100&go=0"
            },
            {
                "category": "h.运动户外.运动鞋包.运动包",
                "url": "http://list.jd.com/list.html?cat=1318-12099-9768&go=0"
            },
            {
                "category": "h.运动户外.运动鞋包.足球鞋",
                "url": "http://list.jd.com/list.html?cat=1318-12099-9758&go=0"
            },
            {
                "category": "h.运动户外.运动鞋包.帆布鞋",
                "url": "http://list.jd.com/list.html?cat=1318-12099-9755&go=0"
            },
            {
                "category": "h.运动户外.运动鞋包.乒羽网鞋",
                "url": "http://list.jd.com/list.html?cat=1318-12099-9760&go=0"
            },
            {
                "category": "h.运动户外.运动鞋包.训练鞋",
                "url": "http://list.jd.com/list.html?cat=1318-12099-9759&go=0"
            },
            {
                "category": "h.运动户外.运动鞋包.专项运动鞋",
                "url": "http://list.jd.com/list.html?cat=1318-12099-12101&go=0"
            },
            {
                "category": "h.运动户外.运动鞋包.拖鞋",
                "url": "http://list.jd.com/list.html?cat=1318-12099-9761&go=0"
            },
            {
                "category": "h.运动户外.运动服饰.运动套装",
                "url": "http://list.jd.com/list.html?cat=1318-12102-9767&go=0"
            },
            {
                "category": "h.运动户外.运动服饰.羽绒服",
                "url": "http://list.jd.com/list.html?cat=1318-12102-12104&go=0"
            },
            {
                "category": "h.运动户外.运动服饰.卫衣/套头衫",
                "url": "http://list.jd.com/list.html?cat=1318-12102-9764&go=0"
            },
            {
                "category": "h.运动户外.运动服饰.棉服",
                "url": "http://list.jd.com/list.html?cat=1318-12102-9762&go=0"
            },
            {
                "category": "h.运动户外.运动服饰.运动裤",
                "url": "http://list.jd.com/list.html?cat=1318-12102-9766&go=0"
            },
            {
                "category": "h.运动户外.运动服饰.夹克/风衣",
                "url": "http://list.jd.com/list.html?cat=1318-12102-9763&go=0"
            },
            {
                "category": "h.运动户外.运动服饰.运动配饰",
                "url": "http://list.jd.com/list.html?cat=1318-12102-12103&go=0"
            },
            {
                "category": "h.运动户外.运动服饰.运动背心",
                "url": "http://list.jd.com/list.html?cat=1318-12102-12108&go=0"
            },
            {
                "category": "h.运动户外.运动服饰.乒羽网服",
                "url": "http://list.jd.com/list.html?cat=1318-12102-12106&go=0"
            },
            {
                "category": "h.运动户外.运动服饰.健身服",
                "url": "http://list.jd.com/list.html?cat=1318-12102-12107&go=0"
            },
            {
                "category": "h.运动户外.运动服饰.毛衫/线衫",
                "url": "http://list.jd.com/list.html?cat=1318-12102-12105&go=0"
            },
            {
                "category": "h.运动户外.运动服饰.T恤",
                "url": "http://list.jd.com/list.html?cat=1318-12102-9765&go=0"
            },
            {
                "category": "h.运动户外.健身训练.跑步机",
                "url": "http://list.jd.com/list.html?cat=1318-1463-1484&go=0"
            },
            {
                "category": "h.运动户外.健身训练.健身车/动感单车",
                "url": "http://list.jd.com/list.html?cat=1318-1463-1483&go=0"
            },
            {
                "category": "h.运动户外.健身训练.哑铃",
                "url": "http://list.jd.com/list.html?cat=1318-1463-12111&go=0"
            },
            {
                "category": "h.运动户外.健身训练.仰卧板/收腹机",
                "url": "http://list.jd.com/list.html?cat=1318-1463-12112&go=0"
            },
            {
                "category": "h.运动户外.健身训练.甩脂机",
                "url": "http://list.jd.com/list.html?cat=1318-1463-12858&go=0"
            },
            {
                "category": "h.运动户外.健身训练.踏步机",
                "url": "http://list.jd.com/list.html?cat=1318-1463-12859&go=0"
            },
            {
                "category": "h.运动户外.健身训练.运动护具",
                "url": "http://list.jd.com/list.html?cat=1318-1463-1487&go=0"
            },
            {
                "category": "h.运动户外.健身训练.瑜伽舞蹈",
                "url": "http://list.jd.com/list.html?cat=1318-1463-12114&go=0"
            },
            {
                "category": "h.运动户外.健身训练.武术搏击",
                "url": "http://list.jd.com/list.html?cat=1318-1463-5153&go=0"
            },
            {
                "category": "h.运动户外.健身训练.综合训练器",
                "url": "http://list.jd.com/list.html?cat=1318-1463-12109&go=0"
            },
            {
                "category": "h.运动户外.健身训练.其他大型器械",
                "url": "http://list.jd.com/list.html?cat=1318-1463-12110&go=0"
            },
            {
                "category": "h.运动户外.健身训练.其他中小型器材",
                "url": "http://list.jd.com/list.html?cat=1318-1463-12113&go=0"
            },
            {
                "category": "h.运动户外.骑行运动.山地车/公路车",
                "url": "http://list.jd.com/list.html?cat=1318-12115-12117&go=0"
            },
            {
                "category": "h.运动户外.骑行运动.折叠车",
                "url": "http://list.jd.com/list.html?cat=1318-12115-12116&go=0"
            },
            {
                "category": "h.运动户外.骑行运动.电动车",
                "url": "http://list.jd.com/list.html?cat=1318-12115-12118&go=0"
            },
            {
                "category": "h.运动户外.骑行运动.平衡车",
                "url": "http://list.jd.com/list.html?cat=1318-12115-12861&go=0"
            },
            {
                "category": "h.运动户外.骑行运动.其他整车",
                "url": "http://list.jd.com/list.html?cat=1318-12115-12119&go=0"
            },
            {
                "category": "h.运动户外.骑行运动.骑行装备",
                "url": "http://list.jd.com/list.html?cat=1318-12115-12121&go=0"
            },
            {
                "category": "h.运动户外.骑行运动.骑行服",
                "url": "http://list.jd.com/list.html?cat=1318-12115-12120&go=0"
            },
            {
                "category": "h.运动户外.体育用品.乒乓球",
                "url": "http://list.jd.com/list.html?cat=1318-1466-1694&go=0"
            },
            {
                "category": "h.运动户外.体育用品.羽毛球",
                "url": "http://list.jd.com/list.html?cat=1318-1466-1695&go=0"
            },
            {
                "category": "h.运动户外.体育用品.篮球",
                "url": "http://list.jd.com/list.html?cat=1318-1466-1698&go=0"
            },
            {
                "category": "h.运动户外.体育用品.足球",
                "url": "http://list.jd.com/list.html?cat=1318-1466-1697&go=0"
            },
            {
                "category": "h.运动户外.体育用品.轮滑滑板",
                "url": "http://list.jd.com/list.html?cat=1318-1466-12122&go=0"
            },
            {
                "category": "h.运动户外.体育用品.网球",
                "url": "http://list.jd.com/list.html?cat=1318-1466-1696&go=0"
            },
            {
                "category": "h.运动户外.体育用品.高尔夫",
                "url": "http://list.jd.com/list.html?cat=1318-1466-1700&go=0"
            },
            {
                "category": "h.运动户外.体育用品.台球",
                "url": "http://list.jd.com/list.html?cat=1318-1466-1701&go=0"
            },
            {
                "category": "h.运动户外.体育用品.排球",
                "url": "http://list.jd.com/list.html?cat=1318-1466-1699&go=0"
            },
            {
                "category": "h.运动户外.体育用品.棋牌麻将",
                "url": "http://list.jd.com/list.html?cat=1318-1466-5155&go=0"
            },
            {
                "category": "h.运动户外.体育用品.其它",
                "url": "http://list.jd.com/list.html?cat=1318-1466-5156&go=0"
            },
            {
                "category": "h.运动户外.户外鞋服.冲锋衣裤",
                "url": "http://list.jd.com/list.html?cat=1318-2628-12123&go=0"
            },
            {
                "category": "h.运动户外.户外鞋服.速干衣裤",
                "url": "http://list.jd.com/list.html?cat=1318-2628-12124&go=0"
            },
            {
                "category": "h.运动户外.户外鞋服.滑雪服",
                "url": "http://list.jd.com/list.html?cat=1318-2628-12125&go=0"
            },
            {
                "category": "h.运动户外.户外鞋服.羽绒服/棉服",
                "url": "http://list.jd.com/list.html?cat=1318-2628-12126&go=0"
            },
            {
                "category": "h.运动户外.户外鞋服.休闲衣裤",
                "url": "http://list.jd.com/list.html?cat=1318-2628-12127&go=0"
            },
            {
                "category": "h.运动户外.户外鞋服.抓绒衣裤",
                "url": "http://list.jd.com/list.html?cat=1318-2628-12128&go=0"
            },
            {
                "category": "h.运动户外.户外鞋服.软壳衣裤",
                "url": "http://list.jd.com/list.html?cat=1318-2628-12129&go=0"
            },
            {
                "category": "h.运动户外.户外鞋服.T恤",
                "url": "http://list.jd.com/list.html?cat=1318-2628-12130&go=0"
            },
            {
                "category": "h.运动户外.户外鞋服.户外风衣",
                "url": "http://list.jd.com/list.html?cat=1318-2628-12131&go=0"
            },
            {
                "category": "h.运动户外.户外鞋服.功能内衣",
                "url": "http://list.jd.com/list.html?cat=1318-2628-12132&go=0"
            },
            {
                "category": "h.运动户外.户外鞋服.军迷服饰",
                "url": "http://list.jd.com/list.html?cat=1318-2628-12133&go=0"
            },
            {
                "category": "h.运动户外.户外鞋服.登山鞋",
                "url": "http://list.jd.com/list.html?cat=1318-2628-12134&go=0"
            },
            {
                "category": "h.运动户外.户外鞋服.徒步鞋",
                "url": "http://list.jd.com/list.html?cat=1318-2628-12136&go=0"
            },
            {
                "category": "h.运动户外.户外鞋服.越野跑鞋",
                "url": "http://list.jd.com/list.html?cat=1318-2628-12137&go=0"
            },
            {
                "category": "h.运动户外.户外鞋服.休闲鞋",
                "url": "http://list.jd.com/list.html?cat=1318-2628-12138&go=0"
            },
            {
                "category": "h.运动户外.户外鞋服.工装鞋",
                "url": "http://list.jd.com/list.html?cat=1318-2628-12139&go=0"
            },
            {
                "category": "h.运动户外.户外鞋服.溯溪鞋",
                "url": "http://list.jd.com/list.html?cat=1318-2628-12140&go=0"
            },
            {
                "category": "h.运动户外.户外鞋服.沙滩/凉拖",
                "url": "http://list.jd.com/list.html?cat=1318-2628-12141&go=0"
            },
            {
                "category": "h.运动户外.户外鞋服.户外袜",
                "url": "http://list.jd.com/list.html?cat=1318-2628-12142&go=0"
            },
            {
                "category": "h.运动户外.户外装备.背包",
                "url": "http://list.jd.com/list.html?cat=1318-1462-1472&go=0"
            },
            {
                "category": "h.运动户外.户外装备.帐篷/垫子",
                "url": "http://list.jd.com/list.html?cat=1318-1462-1473&go=0"
            },
            {
                "category": "h.运动户外.户外装备.睡袋/吊床",
                "url": "http://list.jd.com/list.html?cat=1318-1462-1474&go=0"
            },
            {
                "category": "h.运动户外.户外装备.登山攀岩",
                "url": "http://list.jd.com/list.html?cat=1318-1462-1475&go=0"
            },
            {
                "category": "h.运动户外.户外装备.户外照明",
                "url": "http://list.jd.com/list.html?cat=1318-1462-1476&go=0"
            },
            {
                "category": "h.运动户外.户外装备.野餐烧烤",
                "url": "http://list.jd.com/list.html?cat=1318-1462-1477&go=0"
            },
            {
                "category": "h.运动户外.户外装备.便携桌椅床",
                "url": "http://list.jd.com/list.html?cat=1318-1462-1478&go=0"
            },
            {
                "category": "h.运动户外.户外装备.户外工具",
                "url": "http://list.jd.com/list.html?cat=1318-1462-1479&go=0"
            },
            {
                "category": "h.运动户外.户外装备.望远镜",
                "url": "http://list.jd.com/list.html?cat=1318-1462-1480&go=0"
            },
            {
                "category": "h.运动户外.户外装备.户外仪表",
                "url": "http://list.jd.com/list.html?cat=1318-1462-2631&go=0"
            },
            {
                "category": "h.运动户外.户外装备.旅游用品",
                "url": "http://list.jd.com/list.html?cat=1318-1462-2691&go=0"
            },
            {
                "category": "h.运动户外.户外装备.军迷用品",
                "url": "http://list.jd.com/list.html?cat=1318-1462-5152&go=0"
            },
            {
                "category": "h.运动户外.户外装备.救援装备",
                "url": "http://list.jd.com/list.html?cat=1318-1462-12143&go=0"
            },
            {
                "category": "h.运动户外.户外装备.滑雪装备",
                "url": "http://list.jd.com/list.html?cat=1318-1462-12144&go=0"
            },
            {
                "category": "h.运动户外.户外装备.极限户外",
                "url": "http://list.jd.com/list.html?cat=1318-1462-12145&go=0"
            },
            {
                "category": "h.运动户外.户外装备.冲浪潜水",
                "url": "http://list.jd.com/list.html?cat=1318-1462-12146&go=0"
            },
            {
                "category": "h.运动户外.户外装备.户外配饰",
                "url": "http://list.jd.com/list.html?cat=1318-1462-2629&go=0"
            },
            {
                "category": "h.运动户外.垂钓用品.鱼竿鱼线",
                "url": "http://list.jd.com/list.html?cat=1318-12147-12148&go=0"
            },
            {
                "category": "h.运动户外.垂钓用品.浮漂鱼饵",
                "url": "http://list.jd.com/list.html?cat=1318-12147-12149&go=0"
            },
            {
                "category": "h.运动户外.垂钓用品.钓鱼桌椅",
                "url": "http://list.jd.com/list.html?cat=1318-12147-12150&go=0"
            },
            {
                "category": "h.运动户外.垂钓用品.钓鱼配件",
                "url": "http://list.jd.com/list.html?cat=1318-12147-12151&go=0"
            },
            {
                "category": "h.运动户外.垂钓用品.钓箱鱼包",
                "url": "http://list.jd.com/list.html?cat=1318-12147-12152&go=0"
            },
            {
                "category": "h.运动户外.垂钓用品.其它",
                "url": "http://list.jd.com/list.html?cat=1318-12147-12153&go=0"
            },
            {
                "category": "h.运动户外.游泳用品.泳镜",
                "url": "http://list.jd.com/list.html?cat=1318-12154-12155&go=0"
            },
            {
                "category": "h.运动户外.游泳用品.泳帽",
                "url": "http://list.jd.com/list.html?cat=1318-12154-12156&go=0"
            },
            {
                "category": "h.运动户外.游泳用品.游泳包防水包",
                "url": "http://list.jd.com/list.html?cat=1318-12154-12157&go=0"
            },
            {
                "category": "h.运动户外.游泳用品.男士泳衣",
                "url": "http://list.jd.com/list.html?cat=1318-12154-12159&go=0"
            },
            {
                "category": "h.运动户外.游泳用品.女士泳衣",
                "url": "http://list.jd.com/list.html?cat=1318-12154-12158&go=0"
            },
            {
                "category": "h.运动户外.游泳用品.比基尼",
                "url": "http://list.jd.com/list.html?cat=1318-12154-12160&go=0"
            },
            {
                "category": "h.运动户外.游泳用品.其它",
                "url": "http://list.jd.com/list.html?cat=1318-12154-12161&go=0"
            },
            {
                "category": "h.运动户外.钟表.男表",
                "url": "http://list.jd.com/list.html?cat=5025-5026-12091&go=0"
            },
            {
                "category": "h.运动户外.钟表.女表",
                "url": "http://list.jd.com/list.html?cat=5025-5026-12092&go=0"
            },
            {
                "category": "h.运动户外.钟表.儿童表",
                "url": "http://list.jd.com/list.html?cat=5025-5026-12093&go=0"
            },
            {
                "category": "h.运动户外.钟表.智能手表",
                "url": "http://list.jd.com/list.html?cat=5025-5026-12417&go=0"
            },
            {
                "category": "h.运动户外.钟表.座钟挂钟",
                "url": "http://list.jd.com/list.html?cat=5025-5026-12094&go=0"
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
