# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

import scrapy
import json
import datetime

from ..items import ShellerInfoItem


class JDSpider(scrapy.Spider):
    name = "jd_spider_c"

    def start_requests(self):

        data1 = [
            {
                "category": "c.电脑、办公.电脑整机.超极本",
                "url": "http://list.jd.com/list.html?cat=670-671-6864&go=0"
            },
            {
                "category": "c.电脑、办公.电脑整机.游戏本",
                "url": "http://list.jd.com/list.html?cat=670-671-1105&go=0"
            },
            {
                "category": "c.电脑、办公.电脑整机.平板电脑",
                "url": "http://list.jd.com/list.html?cat=670-671-2694&go=0"
            },
            {
                "category": "c.电脑、办公.电脑整机.平板电脑配件",
                "url": "http://list.jd.com/list.html?cat=670-671-5146&go=0"
            },
            {
                "category": "c.电脑、办公.电脑整机.台式机",
                "url": "http://list.jd.com/list.html?cat=670-671-673&go=0"
            },
            {
                "category": "c.电脑、办公.电脑整机.一体机",
                "url": "http://list.jd.com/list.html?cat=670-671-12798&go=0"
            },
            {
                "category": "c.电脑、办公.电脑整机.服务器/工作站",
                "url": "http://list.jd.com/list.html?cat=670-671-674&go=0"
            },
            {
                "category": "c.电脑、办公.电脑整机.笔记本配件",
                "url": "http://list.jd.com/list.html?cat=670-671-675&go=0"
            },
            {
                "category": "c.电脑、办公.电脑配件.CPU",
                "url": "http://list.jd.com/list.html?cat=670-677-678&go=0"
            },
            {
                "category": "c.电脑、办公.电脑配件.主板",
                "url": "http://list.jd.com/list.html?cat=670-677-681&go=0"
            },
            {
                "category": "c.电脑、办公.电脑配件.显卡",
                "url": "http://list.jd.com/list.html?cat=670-677-679&go=0"
            },
            {
                "category": "c.电脑、办公.电脑配件.硬盘",
                "url": "http://list.jd.com/list.html?cat=670-677-683&go=0"
            },
            {
                "category": "c.电脑、办公.电脑配件.SSD固态硬盘",
                "url": "http://list.jd.com/list.html?cat=670-677-11303&go=0"
            },
            {
                "category": "c.电脑、办公.电脑配件.内存",
                "url": "http://list.jd.com/list.html?cat=670-677-680&go=0"
            },
            {
                "category": "c.电脑、办公.电脑配件.机箱",
                "url": "http://list.jd.com/list.html?cat=670-677-687&go=0"
            },
            {
                "category": "c.电脑、办公.电脑配件.电源",
                "url": "http://list.jd.com/list.html?cat=670-677-691&go=0"
            },
            {
                "category": "c.电脑、办公.电脑配件.显示器",
                "url": "http://list.jd.com/list.html?cat=670-677-688&go=0"
            },
            {
                "category": "c.电脑、办公.电脑配件.刻录机/光驱",
                "url": "http://list.jd.com/list.html?cat=670-677-684&go=0"
            },
            {
                "category": "c.电脑、办公.电脑配件.声卡/扩展卡",
                "url": "http://list.jd.com/list.html?cat=670-677-5008&go=0"
            },
            {
                "category": "c.电脑、办公.电脑配件.散热器",
                "url": "http://list.jd.com/list.html?cat=670-677-682&go=0"
            },
            {
                "category": "c.电脑、办公.电脑配件.装机配件",
                "url": "http://list.jd.com/list.html?cat=670-677-5009&go=0"
            },
            {
                "category": "c.电脑、办公.电脑配件.组装电脑",
                "url": "http://list.jd.com/list.html?cat=670-677-11762&go=0"
            },
            {
                "category": "c.电脑、办公.外设产品.鼠标",
                "url": "http://list.jd.com/list.html?cat=670-686-690&go=0"
            },
            {
                "category": "c.电脑、办公.外设产品.键盘",
                "url": "http://list.jd.com/list.html?cat=670-686-689&go=0"
            },
            {
                "category": "c.电脑、办公.外设产品.网络仪表仪器",
                "url": "http://list.jd.com/list.html?cat=670-686-12799&go=0"
            },
            {
                "category": "c.电脑、办公.外设产品.U盘",
                "url": "http://list.jd.com/list.html?cat=670-686-694&go=0"
            },
            {
                "category": "c.电脑、办公.外设产品.移动硬盘",
                "url": "http://list.jd.com/list.html?cat=670-686-693&go=0"
            },
            {
                "category": "c.电脑、办公.外设产品.鼠标垫",
                "url": "http://list.jd.com/list.html?cat=670-686-826&go=0"
            },
            {
                "category": "c.电脑、办公.外设产品.摄像头",
                "url": "http://list.jd.com/list.html?cat=670-686-692&go=0"
            },
            {
                "category": "c.电脑、办公.外设产品.线缆",
                "url": "http://list.jd.com/list.html?cat=670-686-1049&go=0"
            },
            {
                "category": "c.电脑、办公.外设产品.电玩",
                "url": "http://list.jd.com/list.html?cat=670-686-697&go=0"
            },
            {
                "category": "c.电脑、办公.外设产品.手写板",
                "url": "http://list.jd.com/list.html?cat=670-686-698&go=0"
            },
            {
                "category": "c.电脑、办公.外设产品.外置盒",
                "url": "http://list.jd.com/list.html?cat=670-686-695&go=0"
            },
            {
                "category": "c.电脑、办公.外设产品.电脑工具",
                "url": "http://list.jd.com/list.html?cat=670-686-1050&go=0"
            },
            {
                "category": "c.电脑、办公.外设产品.电脑清洁",
                "url": "http://list.jd.com/list.html?cat=670-686-1051&go=0"
            },
            {
                "category": "c.电脑、办公.外设产品.UPS",
                "url": "http://list.jd.com/list.html?cat=670-686-1048&go=0"
            },
            {
                "category": "c.电脑、办公.外设产品.插座",
                "url": "http://list.jd.com/list.html?cat=670-686-1047&go=0"
            },
            {
                "category": "c.电脑、办公.游戏设备.游戏机",
                "url": "http://list.jd.com/list.html?cat=670-12800-12801&go=0"
            },
            {
                "category": "c.电脑、办公.游戏设备.游戏耳机",
                "url": "http://list.jd.com/list.html?cat=670-12800-12802&go=0"
            },
            {
                "category": "c.电脑、办公.游戏设备.手柄/方向盘",
                "url": "http://list.jd.com/list.html?cat=670-12800-12803&go=0"
            },
            {
                "category": "c.电脑、办公.游戏设备.游戏软件",
                "url": "http://list.jd.com/list.html?cat=670-12800-12804&go=0"
            },
            {
                "category": "c.电脑、办公.游戏设备.游戏周边",
                "url": "http://list.jd.com/list.html?cat=670-12800-12805&go=0"
            },
            {
                "category": "c.电脑、办公.网络产品.路由器",
                "url": "http://list.jd.com/list.html?cat=670-699-700&go=0"
            },
            {
                "category": "c.电脑、办公.网络产品.网卡",
                "url": "http://list.jd.com/list.html?cat=670-699-701&go=0"
            },
            {
                "category": "c.电脑、办公.网络产品.交换机",
                "url": "http://list.jd.com/list.html?cat=670-699-702&go=0"
            },
            {
                "category": "c.电脑、办公.网络产品.网络存储",
                "url": "http://list.jd.com/list.html?cat=670-699-983&go=0"
            },
            {
                "category": "c.电脑、办公.网络产品.4G/3G上网",
                "url": "http://list.jd.com/list.html?cat=670-699-1098&go=0"
            },
            {
                "category": "c.电脑、办公.网络产品.网络盒子",
                "url": "http://list.jd.com/list.html?cat=670-699-11304&go=0"
            },
            {
                "category": "c.电脑、办公.网络产品.网络配件",
                "url": "http://list.jd.com/list.html?cat=670-699-12370&go=0"
            },
            {
                "category": "c.电脑、办公.办公设备.投影机",
                "url": "http://list.jd.com/list.html?cat=670-716-722&go=0"
            },
            {
                "category": "c.电脑、办公.办公设备.投影配件",
                "url": "http://list.jd.com/list.html?cat=670-716-5010&go=0"
            },
            {
                "category": "c.电脑、办公.办公设备.多功能一体机",
                "url": "http://list.jd.com/list.html?cat=670-716-720&go=0"
            },
            {
                "category": "c.电脑、办公.办公设备.打印机",
                "url": "http://list.jd.com/list.html?cat=670-716-717&go=0"
            },
            {
                "category": "c.电脑、办公.办公设备.传真设备",
                "url": "http://list.jd.com/list.html?cat=670-716-718&go=0"
            },
            {
                "category": "c.电脑、办公.办公设备.验钞/点钞机",
                "url": "http://list.jd.com/list.html?cat=670-716-725&go=0"
            },
            {
                "category": "c.电脑、办公.办公设备.扫描设备",
                "url": "http://list.jd.com/list.html?cat=670-716-721&go=0"
            },
            {
                "category": "c.电脑、办公.办公设备.复合机",
                "url": "http://list.jd.com/list.html?cat=670-716-719&go=0"
            },
            {
                "category": "c.电脑、办公.办公设备.碎纸机",
                "url": "http://list.jd.com/list.html?cat=670-716-723&go=0"
            },
            {
                "category": "c.电脑、办公.办公设备.考勤机",
                "url": "http://list.jd.com/list.html?cat=670-716-724&go=0"
            },
            {
                "category": "c.电脑、办公.办公设备.收款/POS机",
                "url": "http://list.jd.com/list.html?cat=670-716-7373&go=0"
            },
            {
                "category": "c.电脑、办公.办公设备.会议音频视频",
                "url": "http://list.jd.com/list.html?cat=670-716-7375&go=0"
            },
            {
                "category": "c.电脑、办公.办公设备.保险柜",
                "url": "http://list.jd.com/list.html?cat=670-716-2601&go=0"
            },
            {
                "category": "c.电脑、办公.办公设备.装订/封装机",
                "url": "http://list.jd.com/list.html?cat=670-716-4839&go=0"
            },
            {
                "category": "c.电脑、办公.办公设备.安防监控",
                "url": "http://list.jd.com/list.html?cat=670-716-7374&go=0"
            },
            {
                "category": "c.电脑、办公.办公设备.办公家具",
                "url": "http://list.jd.com/list.html?cat=670-716-11221&go=0"
            },
            {
                "category": "c.电脑、办公.办公设备.白板",
                "url": "http://list.jd.com/list.html?cat=670-716-727&go=0"
            },
            {
                "category": "c.电脑、办公.文具耗材.硒鼓/墨粉",
                "url": "http://list.jd.com/list.html?cat=670-729-730&go=0"
            },
            {
                "category": "c.电脑、办公.文具耗材.墨盒",
                "url": "http://list.jd.com/list.html?cat=670-729-731&go=0"
            },
            {
                "category": "c.电脑、办公.文具耗材.色带",
                "url": "http://list.jd.com/list.html?cat=670-729-733&go=0"
            },
            {
                "category": "c.电脑、办公.文具耗材.纸类",
                "url": "http://list.jd.com/list.html?cat=670-729-736&go=0"
            },
            {
                "category": "c.电脑、办公.文具耗材.办公文具",
                "url": "http://list.jd.com/list.html?cat=670-729-4837&go=0"
            },
            {
                "category": "c.电脑、办公.文具耗材.学生文具",
                "url": "http://list.jd.com/list.html?cat=670-729-1449&go=0"
            },
            {
                "category": "c.电脑、办公.文具耗材.文件管理",
                "url": "http://list.jd.com/list.html?cat=670-729-4840&go=0"
            },
            {
                "category": "c.电脑、办公.文具耗材.本册/便签",
                "url": "http://list.jd.com/list.html?cat=670-729-7371&go=0"
            },
            {
                "category": "c.电脑、办公.文具耗材.计算器",
                "url": "http://list.jd.com/list.html?cat=670-729-728&go=0"
            },
            {
                "category": "c.电脑、办公.文具耗材.笔类",
                "url": "http://list.jd.com/list.html?cat=670-729-2603&go=0"
            },
            {
                "category": "c.电脑、办公.文具耗材.画具画材",
                "url": "http://list.jd.com/list.html?cat=670-729-12376&go=0"
            },
            {
                "category": "c.电脑、办公.文具耗材.财会用品",
                "url": "http://list.jd.com/list.html?cat=670-729-7372&go=0"
            },
            {
                "category": "c.电脑、办公.文具耗材.刻录碟片/附件",
                "url": "http://list.jd.com/list.html?cat=670-729-4838&go=0"
            },
            {
                "category": "c.电脑、办公.服务产品.延保服务",
                "url": "http://list.jd.com/list.html?cat=670-703-10969&go=0"
            },
            {
                "category": "c.电脑、办公.服务产品.上门安装",
                "url": "http://list.jd.com/list.html?cat=670-703-10011&go=0"
            },
            {
                "category": "c.电脑、办公.服务产品.维修保养",
                "url": "http://list.jd.com/list.html?cat=670-703-12429&go=0"
            },
            {
                "category": "c.电脑、办公.服务产品.电脑软件",
                "url": "http://list.jd.com/list.html?cat=670-703-5011&go=0"
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
