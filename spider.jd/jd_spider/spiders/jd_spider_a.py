# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

import scrapy
import json
import datetime

from ..items import ShellerInfoItem


class JDSpider(scrapy.Spider):
    name = "jd_spider_a"

    def start_requests(self):

        data1 = [
            {
                "category": "a.家用电器.大家电.平板电视",
                "url": "http://list.jd.com/list.html?cat=737-794-798&go=0"
            },
            {
                "category": "a.家用电器.大家电.空调",
                "url": "http://list.jd.com/list.html?cat=737-794-870&go=0"
            },
            {
                "category": "a.家用电器.大家电.冰箱",
                "url": "http://list.jd.com/list.html?cat=737-794-878&go=0"
            },
            {
                "category": "a.家用电器.大家电.洗衣机",
                "url": "http://list.jd.com/list.html?cat=737-794-880&go=0"
            },
            {
                "category": "a.家用电器.大家电.家庭影院",
                "url": "http://list.jd.com/list.html?cat=737-794-823&go=0"
            },
            {
                "category": "a.家用电器.大家电.DVD",
                "url": "http://list.jd.com/list.html?cat=737-794-965&go=0"
            },
            {
                "category": "a.家用电器.大家电.迷你音响",
                "url": "http://list.jd.com/list.html?cat=737-794-1199&go=0"
            },
            {
                "category": "a.家用电器.大家电.冷柜/冰吧",
                "url": "http://list.jd.com/list.html?cat=737-794-12392&go=0"
            },
            {
                "category": "a.家用电器.大家电.酒柜",
                "url": "http://list.jd.com/list.html?cat=737-794-12401&go=0"
            },
            {
                "category": "a.家用电器.大家电.家电配件",
                "url": "http://list.jd.com/list.html?cat=737-794-877&go=0"
            },
            {
                "category": "a.家用电器.厨卫大电.油烟机",
                "url": "http://list.jd.com/list.html?cat=737,13297,1300&ev=%402047_584926&go=0&JL=3_%E4%BA%A7%E5%93%81%E7%B1%BB%E5%9E%8B_%E6%B2%B9%E7%83%9F%E6%9C%BA"
            },
            {
                "category": "a.家用电器.厨卫大电.燃气灶",
                "url": "http://list.jd.com/list.html?cat=737-13297-13298&go=0"
            },
            {
                "category": "a.家用电器.厨卫大电.烟灶套装",
                "url": "http://list.jd.com/list.html?cat=737,13297,1300&ev=%402047_15280&go=0&JL=3_%E4%BA%A7%E5%93%81%E7%B1%BB%E5%9E%8B_%E7%83%9F%E7%81%B6%E5%A5%97%E8%A3%85"
            },
            {
                "category": "a.家用电器.厨卫大电.消毒柜",
                "url": "http://list.jd.com/list.html?cat=737-13297-1301&go=0"
            },
            {
                "category": "a.家用电器.厨卫大电.洗碗机",
                "url": "http://list.jd.com/list.html?cat=737-13297-13117&go=0"
            },
            {
                "category": "a.家用电器.厨卫大电.电热水器",
                "url": "http://list.jd.com/list.html?cat=737,13297,1706&ev=%403851_28702&go=0&JL=3_%E4%BA%A7%E5%93%81%E7%B1%BB%E5%9E%8B_%E7%94%B5%E7%83%AD%E6%B0%B4%E5%99%A8"
            },
            {
                "category": "a.家用电器.厨卫大电.燃气热水器",
                "url": "http://list.jd.com/list.html?cat=737,13297,1706&ev=%403851_28703&go=0&JL=3_%E4%BA%A7%E5%93%81%E7%B1%BB%E5%9E%8B_%E7%87%83%E6%B0%94%E7%83%AD%E6%B0%B4%E5%99%A8"
            },
            {
                "category": "a.家用电器.厨卫大电.嵌入式厨电",
                "url": "http://coll.jd.com/list.html?sub=1661"
            },
            {
                "category": "a.家用电器.厨房小电.电饭煲",
                "url": "http://list.jd.com/list.html?cat=737-752-753&go=0"
            },
            {
                "category": "a.家用电器.厨房小电.微波炉",
                "url": "http://list.jd.com/list.html?cat=737-752-758&go=0"
            },
            {
                "category": "a.家用电器.厨房小电.电烤箱",
                "url": "http://list.jd.com/list.html?cat=737-752-759&go=0"
            },
            {
                "category": "a.家用电器.厨房小电.电磁炉",
                "url": "http://list.jd.com/list.html?cat=737-752-757&go=0"
            },
            {
                "category": "a.家用电器.厨房小电.电压力锅",
                "url": "http://list.jd.com/list.html?cat=737-752-881&go=0"
            },
            {
                "category": "a.家用电器.厨房小电.豆浆机",
                "url": "http://list.jd.com/list.html?cat=737-752-756&go=0"
            },
            {
                "category": "a.家用电器.厨房小电.咖啡机",
                "url": "http://list.jd.com/list.html?cat=737-752-761&go=0"
            },
            {
                "category": "a.家用电器.厨房小电.面包机",
                "url": "http://list.jd.com/list.html?cat=737-752-899&go=0"
            },
            {
                "category": "a.家用电器.厨房小电.榨汁机",
                "url": "http://list.jd.com/list.html?cat=737-752-13116&go=0"
            },
            {
                "category": "a.家用电器.厨房小电.料理机",
                "url": "http://list.jd.com/list.html?cat=737-752-755&go=0"
            },
            {
                "category": "a.家用电器.厨房小电.电饼铛",
                "url": "http://list.jd.com/list.html?cat=737-752-882&go=0"
            },
            {
                "category": "a.家用电器.厨房小电.养生壶/煎药壶",
                "url": "http://list.jd.com/list.html?cat=737-752-12397&go=0"
            },
            {
                "category": "a.家用电器.厨房小电.酸奶机",
                "url": "http://list.jd.com/list.html?cat=737-752-762&go=0"
            },
            {
                "category": "a.家用电器.厨房小电.煮蛋器",
                "url": "http://list.jd.com/list.html?cat=737-752-902&go=0"
            },
            {
                "category": "a.家用电器.厨房小电.电水壶/热水瓶",
                "url": "http://list.jd.com/list.html?cat=737-752-760&go=0"
            },
            {
                "category": "a.家用电器.厨房小电.电炖锅",
                "url": "http://list.jd.com/list.html?cat=737-752-9249&go=0"
            },
            {
                "category": "a.家用电器.厨房小电.多用途锅",
                "url": "http://list.jd.com/list.html?cat=737-752-754&go=0"
            },
            {
                "category": "a.家用电器.厨房小电.电烧烤炉",
                "url": "http://list.jd.com/list.html?cat=737-752-13118&go=0"
            },
            {
                "category": "a.家用电器.厨房小电.电热饭盒",
                "url": "http://list.jd.com/list.html?cat=737-752-12398&go=0"
            },
            {
                "category": "a.家用电器.厨房小电.其它厨房电器",
                "url": "http://list.jd.com/list.html?cat=737-752-803&go=0"
            },
            {
                "category": "a.家用电器.生活电器.电风扇",
                "url": "http://list.jd.com/list.html?cat=737-738-751&go=0"
            },
            {
                "category": "a.家用电器.生活电器.冷风扇",
                "url": "http://list.jd.com/list.html?cat=737-738-1278&go=0"
            },
            {
                "category": "a.家用电器.生活电器.吸尘器",
                "url": "http://list.jd.com/list.html?cat=737-738-745&go=0"
            },
            {
                "category": "a.家用电器.生活电器.净化器",
                "url": "http://list.jd.com/list.html?cat=737-738-749&go=0"
            },
            {
                "category": "a.家用电器.生活电器.扫地机器人",
                "url": "http://list.jd.com/list.html?cat=737-738-12394&go=0"
            },
            {
                "category": "a.家用电器.生活电器.加湿器",
                "url": "http://list.jd.com/list.html?cat=737-738-748&go=0"
            },
            {
                "category": "a.家用电器.生活电器.挂烫机/熨斗",
                "url": "http://list.jd.com/list.html?cat=737-738-1279&go=0"
            },
            {
                "category": "a.家用电器.生活电器.取暖电器",
                "url": "http://list.jd.com/list.html?cat=737-738-747&go=0"
            },
            {
                "category": "a.家用电器.生活电器.插座",
                "url": "http://list.jd.com/list.html?cat=737-738-1052&go=0"
            },
            {
                "category": "a.家用电器.生活电器.电话机",
                "url": "http://list.jd.com/list.html?cat=737-738-806&go=0"
            },
            {
                "category": "a.家用电器.生活电器.净水器",
                "url": "http://list.jd.com/list.html?cat=737-738-898&go=0"
            },
            {
                "category": "a.家用电器.生活电器.饮水机",
                "url": "http://list.jd.com/list.html?cat=737-738-750&go=0"
            },
            {
                "category": "a.家用电器.生活电器.除湿机",
                "url": "http://list.jd.com/list.html?cat=737-738-1283&go=0"
            },
            {
                "category": "a.家用电器.生活电器.干衣机",
                "url": "http://list.jd.com/list.html?cat=737-738-12395&go=0"
            },
            {
                "category": "a.家用电器.生活电器.清洁机",
                "url": "http://list.jd.com/list.html?cat=737-738-897&go=0"
            },
            {
                "category": "a.家用电器.生活电器.收录/音机",
                "url": "http://list.jd.com/list.html?cat=737-738-801&go=0"
            },
            {
                "category": "a.家用电器.生活电器.其它生活电器",
                "url": "http://list.jd.com/list.html?cat=737-738-825&go=0"
            },
            {
                "category": "a.家用电器.生活电器.生活电器配件",
                "url": "http://list.jd.com/list.html?cat=737-738-12396&go=0"
            },
            {
                "category": "a.家用电器.个护健康.剃须刀",
                "url": "http://list.jd.com/list.html?cat=737-1276-739&go=0"
            },
            {
                "category": "a.家用电器.个护健康.口腔护理",
                "url": "http://list.jd.com/list.html?cat=737-1276-741&go=0"
            },
            {
                "category": "a.家用电器.个护健康.电吹风",
                "url": "http://list.jd.com/list.html?cat=737-1276-740&go=0"
            },
            {
                "category": "a.家用电器.个护健康.美容器",
                "url": "http://list.jd.com/list.html?cat=737-1276-795&go=0"
            },
            {
                "category": "a.家用电器.个护健康.卷/直发器",
                "url": "http://list.jd.com/list.html?cat=737-1276-12400&go=0"
            },
            {
                "category": "a.家用电器.个护健康.理发器",
                "url": "http://list.jd.com/list.html?cat=737-1276-1287&go=0"
            },
            {
                "category": "a.家用电器.个护健康.剃/脱毛器",
                "url": "http://list.jd.com/list.html?cat=737-1276-742&go=0"
            },
            {
                "category": "a.家用电器.个护健康.足浴盆",
                "url": "http://list.jd.com/list.html?cat=737-1276-963&go=0"
            },
            {
                "category": "a.家用电器.个护健康.健康秤/厨房秤",
                "url": "http://list.jd.com/list.html?cat=737-1276-1289&go=0"
            },
            {
                "category": "a.家用电器.个护健康.按摩器",
                "url": "http://list.jd.com/list.html?cat=737-1276-967&go=0"
            },
            {
                "category": "a.家用电器.个护健康.按摩椅",
                "url": "http://list.jd.com/list.html?cat=737-1276-1291&go=0"
            },
            {
                "category": "a.家用电器.个护健康.血压计",
                "url": "http://list.jd.com/list.html?cat=737-1276-966&go=0"
            },
            {
                "category": "a.家用电器.个护健康.血糖仪",
                "url": "http://list.jd.com/list.html?cat=737-1276-1225&go=0"
            },
            {
                "category": "a.家用电器.个护健康.体温计",
                "url": "http://list.jd.com/list.html?cat=737-1276-1292&go=0"
            },
            {
                "category": "a.家用电器.个护健康.计步器/脂肪检测仪",
                "url": "http://list.jd.com/list.html?cat=737-1276-968&go=0"
            },
            {
                "category": "a.家用电器.个护健康.其它健康电器",
                "url": "http://list.jd.com/list.html?cat=737-1276-1290&go=0"
            },
            {
                "category": "a.家用电器.五金家装.电动工具",
                "url": "http://list.jd.com/list.html?cat=737-1277-934&go=0"
            },
            {
                "category": "a.家用电器.五金家装.手动工具",
                "url": "http://list.jd.com/list.html?cat=737-1277-3979&go=0"
            },
            {
                "category": "a.家用电器.五金家装.仪器仪表",
                "url": "http://list.jd.com/list.html?cat=737-1277-6974&go=0"
            },
            {
                "category": "a.家用电器.五金家装.浴霸/排气扇",
                "url": "http://list.jd.com/list.html?cat=737-1277-900&go=0"
            },
            {
                "category": "a.家用电器.五金家装.灯具",
                "url": "http://list.jd.com/list.html?cat=737-1277-1295&go=0"
            },
            {
                "category": "a.家用电器.五金家装.LED灯",
                "url": "http://list.jd.com/list.html?cat=737-1277-6975&go=0"
            },
            {
                "category": "a.家用电器.五金家装.洁身器",
                "url": "http://list.jd.com/list.html?cat=737-1277-4934&go=0"
            },
            {
                "category": "a.家用电器.五金家装.水槽",
                "url": "http://list.jd.com/list.html?cat=737-1277-5004&go=0"
            },
            {
                "category": "a.家用电器.五金家装.龙头",
                "url": "http://list.jd.com/list.html?cat=737-1277-5005&go=0"
            },
            {
                "category": "a.家用电器.五金家装.淋浴花洒",
                "url": "http://list.jd.com/list.html?cat=737-1277-5006&go=0"
            },
            {
                "category": "a.家用电器.五金家装.厨卫五金",
                "url": "http://list.jd.com/list.html?cat=737-1277-1293&go=0"
            },
            {
                "category": "a.家用电器.五金家装.家具五金",
                "url": "http://list.jd.com/list.html?cat=737-1277-4834&go=0"
            },
            {
                "category": "a.家用电器.五金家装.门铃",
                "url": "http://list.jd.com/list.html?cat=737-1277-1294&go=0"
            },
            {
                "category": "a.家用电器.五金家装.电气开关",
                "url": "http://list.jd.com/list.html?cat=737-1277-6976&go=0"
            },
            {
                "category": "a.家用电器.五金家装.插座",
                "url": "http://list.jd.com/list.html?cat=737-1277-6977&go=0"
            },
            {
                "category": "a.家用电器.五金家装.电工电料",
                "url": "http://list.jd.com/list.html?cat=737-1277-6978&go=0"
            },
            {
                "category": "a.家用电器.五金家装.监控安防",
                "url": "http://list.jd.com/list.html?cat=737-1277-6979&go=0"
            },
            {
                "category": "a.家用电器.五金家装.电线/线缆",
                "url": "http://list.jd.com/list.html?cat=737-1277-1299&go=0"
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
        sheller_info_item["sheller_url"] = "http:" + str(response.xpath("//div[@class='seller-infor']/a/@href").extract_first())
        sheller_info_item["shop_name"] = response.xpath('//span[@class="text J-shop-name"]/text()').extract_first()
        sheller_info_item["shop_address"] = response.xpath(
            '//span[@class="text J-shop-address"]/text()').extract_first()
        sheller_info_item['sheller_phone'] = response.xpath('//div[@class="seller-phone"]/text()').extract_first()
        sheller_info_item['insert_time'] = datetime.datetime.now().strftime('%Y-%m-%d')
        yield sheller_info_item

    def parse_store_detail(self, response):
        pass
