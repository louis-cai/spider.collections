# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

import scrapy
import json
import datetime

from ..items import ShellerInfoItem


class JDSpider(scrapy.Spider):
    name = "jd_spider_f"

    def start_requests(self):

        data1 = [
            {
                "category": "f.个护化妆.面部护肤.清洁",
                "url": "http://list.jd.com/list.html?cat=1316-1381-1389&go=0"
            },
            {
                "category": "f.个护化妆.面部护肤.护肤",
                "url": "http://list.jd.com/list.html?cat=1316-1381-1391&go=0"
            },
            {
                "category": "f.个护化妆.面部护肤.面膜",
                "url": "http://list.jd.com/list.html?cat=1316-1381-1392&go=0"
            },
            {
                "category": "f.个护化妆.面部护肤.剃须",
                "url": "http://list.jd.com/list.html?cat=1316-1381-1416&go=0"
            },
            {
                "category": "f.个护化妆.面部护肤.套装",
                "url": "http://list.jd.com/list.html?cat=1316-1381-1396&go=0"
            },
            {
                "category": "f.个护化妆.洗发护发.洗发",
                "url": "http://list.jd.com/list.html?cat=1316-1386-11922&go=0"
            },
            {
                "category": "f.个护化妆.洗发护发.护发",
                "url": "http://list.jd.com/list.html?cat=1316-1386-11923&go=0"
            },
            {
                "category": "f.个护化妆.洗发护发.染发",
                "url": "http://list.jd.com/list.html?cat=1316-1386-11924&go=0"
            },
            {
                "category": "f.个护化妆.洗发护发.造型",
                "url": "http://list.jd.com/list.html?cat=1316-1386-11925&go=0"
            },
            {
                "category": "f.个护化妆.洗发护发.假发",
                "url": "http://list.jd.com/list.html?cat=1316-1386-4699&go=0"
            },
            {
                "category": "f.个护化妆.洗发护发.套装",
                "url": "http://list.jd.com/list.html?cat=1316-1386-6739&go=0"
            },
            {
                "category": "f.个护化妆.身体护肤.沐浴",
                "url": "http://list.jd.com/list.html?cat=1316-1383-1401&go=0"
            },
            {
                "category": "f.个护化妆.身体护肤.润肤",
                "url": "http://list.jd.com/list.html?cat=1316-1383-1404&go=0"
            },
            {
                "category": "f.个护化妆.身体护肤.颈部",
                "url": "http://list.jd.com/list.html?cat=1316-1383-1394&go=0"
            },
            {
                "category": "f.个护化妆.身体护肤.手足",
                "url": "http://list.jd.com/list.html?cat=1316-1383-2562&go=0"
            },
            {
                "category": "f.个护化妆.身体护肤.纤体塑形",
                "url": "http://list.jd.com/list.html?cat=1316-1383-5164&go=0"
            },
            {
                "category": "f.个护化妆.身体护肤.美胸",
                "url": "http://list.jd.com/list.html?cat=1316-1383-11928&go=0"
            },
            {
                "category": "f.个护化妆.身体护肤.套装",
                "url": "http://list.jd.com/list.html?cat=1316-1383-11929&go=0"
            },
            {
                "category": "f.个护化妆.口腔护理.牙膏/牙粉",
                "url": "http://list.jd.com/list.html?cat=1316-1384-1405&go=0"
            },
            {
                "category": "f.个护化妆.口腔护理.牙刷/牙线",
                "url": "http://list.jd.com/list.html?cat=1316-1384-1406&go=0"
            },
            {
                "category": "f.个护化妆.口腔护理.漱口水",
                "url": "http://list.jd.com/list.html?cat=1316-1384-1407&go=0"
            },
            {
                "category": "f.个护化妆.口腔护理.套装",
                "url": "http://list.jd.com/list.html?cat=1316-1384-11930&go=0"
            },
            {
                "category": "f.个护化妆.女性护理.卫生巾",
                "url": "http://list.jd.com/list.html?cat=1316-1385-1408&go=0"
            },
            {
                "category": "f.个护化妆.女性护理.卫生护垫",
                "url": "http://list.jd.com/list.html?cat=1316-1385-1409&go=0"
            },
            {
                "category": "f.个护化妆.女性护理.私密护理",
                "url": "http://list.jd.com/list.html?cat=1316-1385-1410&go=0"
            },
            {
                "category": "f.个护化妆.女性护理.脱毛膏",
                "url": "http://list.jd.com/list.html?cat=1316-1385-5150&go=0"
            },
            {
                "category": "f.个护化妆.香水彩妆.香水",
                "url": "http://list.jd.com/list.html?cat=1316-1387-11932&go=0"
            },
            {
                "category": "f.个护化妆.香水彩妆.底妆",
                "url": "http://list.jd.com/list.html?cat=1316-1387-1420&go=0"
            },
            {
                "category": "f.个护化妆.香水彩妆.腮红",
                "url": "http://list.jd.com/list.html?cat=1316-1387-1421&go=0"
            },
            {
                "category": "f.个护化妆.香水彩妆.眼部",
                "url": "http://list.jd.com/list.html?cat=1316-1387-1422&go=0"
            },
            {
                "category": "f.个护化妆.香水彩妆.唇部",
                "url": "http://list.jd.com/list.html?cat=1316-1387-1425&go=0"
            },
            {
                "category": "f.个护化妆.香水彩妆.美甲",
                "url": "http://list.jd.com/list.html?cat=1316-1387-1428&go=0"
            },
            {
                "category": "f.个护化妆.香水彩妆.美容工具",
                "url": "http://list.jd.com/list.html?cat=1316-1387-1429&go=0"
            },
            {
                "category": "f.个护化妆.香水彩妆.套装",
                "url": "http://list.jd.com/list.html?cat=1316-1387-1426&go=0"
            },
            {
                "category": "f.个护化妆.清洁用品.纸品湿巾",
                "url": "http://list.jd.com/list.html?cat=1316-1625-1671&go=0"
            },
            {
                "category": "f.个护化妆.清洁用品.衣物清洁",
                "url": "http://list.jd.com/list.html?cat=1316-1625-1662&go=0"
            },
            {
                "category": "f.个护化妆.清洁用品.清洁工具",
                "url": "http://list.jd.com/list.html?cat=1316-1625-1667&go=0"
            },
            {
                "category": "f.个护化妆.清洁用品.家庭清洁",
                "url": "http://list.jd.com/list.html?cat=1316-1625-1663&go=0"
            },
            {
                "category": "f.个护化妆.清洁用品.一次性用品",
                "url": "http://list.jd.com/list.html?cat=1316-1625-11970&go=0"
            },
            {
                "category": "f.个护化妆.清洁用品.驱虫用品",
                "url": "http://list.jd.com/list.html?cat=1316-1625-1669&go=0"
            },
            {
                "category": "f.个护化妆.清洁用品.皮具护理",
                "url": "http://list.jd.com/list.html?cat=1316-1625-1670&go=0"
            },
            {
                "category": "f.个护化妆.宠物生活.水族用品",
                "url": "http://list.jd.com/list.html?cat=6994-6998-7023&go=0"
            },
            {
                "category": "f.个护化妆.宠物生活.宠物主粮",
                "url": "http://list.jd.com/list.html?cat=6994-6995&go=0"
            },
            {
                "category": "f.个护化妆.宠物生活.宠物零食",
                "url": "http://list.jd.com/list.html?cat=6994-6996&go=0"
            },
            {
                "category": "f.个护化妆.宠物生活.猫砂/尿布",
                "url": "http://list.jd.com/list.html?cat=6994-6998-7020&go=0"
            },
            {
                "category": "f.个护化妆.宠物生活.洗护美容",
                "url": "http://list.jd.com/list.html?cat=6994-7001&go=0"
            },
            {
                "category": "f.个护化妆.宠物生活.家居日用",
                "url": "http://list.jd.com/list.html?cat=6994-6998&go=0"
            },
            {
                "category": "f.个护化妆.宠物生活.医疗保健",
                "url": "http://list.jd.com/list.html?cat=6994-6997&go=0"
            },
            {
                "category": "f.个护化妆.宠物生活.出行装备",
                "url": "http://list.jd.com/list.html?cat=6994-7000&go=0"
            },
            {
                "category": "f.个护化妆.宠物生活.宠物玩具",
                "url": "http://list.jd.com/list.html?cat=6994-6999&go=0"
            },
            {
                "category": "f.个护化妆.宠物生活.宠物牵引",
                "url": "http://list.jd.com/list.html?cat=6994-7000-7028&go=0"
            },
            {
                "category": "f.个护化妆.宠物生活.宠物驱虫",
                "url": "http://list.jd.com/list.html?cat=6994-6997-7016&go=0"
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
