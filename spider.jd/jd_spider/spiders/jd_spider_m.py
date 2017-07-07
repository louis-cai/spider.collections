# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

import scrapy
import json
import datetime

from ..items import ShellerInfoItem


class JDSpider(scrapy.Spider):
    name = "jd_spider_m"

    def start_requests(self):

        data1 = [
            {
                "category": "m.图书.音像.游戏",
                "url": "http://list.jd.com/list.html?cat=mvd.jd.com/theme/4053-7.html&go=0"
            },
            {
                "category": "m.图书.少儿.0-2岁",
                "url": "http://list.jd.com/list.html?cat=book.jd.com/children0-2.html&go=0"
            },
            {
                "category": "m.图书.少儿.3-6岁",
                "url": "http://list.jd.com/list.html?cat=book.jd.com/children3-6.html&go=0"
            },
            {
                "category": "m.图书.少儿.7-10岁",
                "url": "http://list.jd.com/list.html?cat=book.jd.com/children7-10.html&go=0"
            },
            {
                "category": "m.图书.少儿.11-14岁",
                "url": "http://list.jd.com/list.html?cat=book.jd.com/children11-14.html&go=0"
            },
            {
                "category": "m.图书.少儿.儿童文学",
                "url": "http://list.jd.com/list.html?cat=1713-3263-3394&go=0"
            },
            {
                "category": "m.图书.少儿.绘本",
                "url": "http://list.jd.com/list.html?cat=1713-3263-4761&go=0"
            },
            {
                "category": "m.图书.少儿.科普",
                "url": "http://list.jd.com/list.html?cat=1713-3263-3399&go=0"
            },
            {
                "category": "m.图书.少儿.幼儿启蒙",
                "url": "http://list.jd.com/list.html?cat=1713-3263-3395&go=0"
            },
            {
                "category": "m.图书.少儿.手工游戏",
                "url": "http://list.jd.com/list.html?cat=1713-3263-3396&go=0"
            },
            {
                "category": "m.图书.少儿.智力开发",
                "url": "http://list.jd.com/list.html?cat=1713-3263-3398&go=0"
            },
            {
                "category": "m.图书.教育.教材",
                "url": "http://list.jd.com/list.html?cat=1713-11047&go=0"
            },
            {
                "category": "m.图书.教育.中小学教辅",
                "url": "http://list.jd.com/list.html?cat=1713-3289&go=0"
            },
            {
                "category": "m.图书.教育.考试",
                "url": "http://list.jd.com/list.html?cat=1713-3290&go=0"
            },
            {
                "category": "m.图书.教育.外语学习",
                "url": "http://list.jd.com/list.html?cat=1713-3291&go=0"
            },
            {
                "category": "m.图书.教育.字典词典",
                "url": "http://list.jd.com/list.html?cat=1713-3294&go=0"
            },
            {
                "category": "m.图书.文艺.小说",
                "url": "http://list.jd.com/list.html?cat=1713-3258&go=0"
            },
            {
                "category": "m.图书.文艺.文学",
                "url": "http://list.jd.com/list.html?cat=1713-3259&go=0"
            },
            {
                "category": "m.图书.文艺.青春文学",
                "url": "http://list.jd.com/list.html?cat=1713-3260&go=0"
            },
            {
                "category": "m.图书.文艺.传记",
                "url": "http://list.jd.com/list.html?cat=1713-3261&go=0"
            },
            {
                "category": "m.图书.文艺.动漫",
                "url": "http://list.jd.com/list.html?cat=1713-3272&go=0"
            },
            {
                "category": "m.图书.文艺.艺术",
                "url": "http://list.jd.com/list.html?cat=1713-3262&go=0"
            },
            {
                "category": "m.图书.文艺.摄影",
                "url": "http://list.jd.com/list.html?cat=1713-12776&go=0"
            },
            {
                "category": "m.图书.经管励志.管理",
                "url": "http://list.jd.com/list.html?cat=1713-3266&go=0"
            },
            {
                "category": "m.图书.经管励志.金融与投资",
                "url": "http://list.jd.com/list.html?cat=1713-3265&go=0"
            },
            {
                "category": "m.图书.经管励志.经济",
                "url": "http://list.jd.com/list.html?cat=1713-3264&go=0"
            },
            {
                "category": "m.图书.经管励志.励志与成功",
                "url": "http://list.jd.com/list.html?cat=1713-3267&go=0"
            },
            {
                "category": "m.图书.人文社科.历史",
                "url": "http://list.jd.com/list.html?cat=1713-3273&go=0"
            },
            {
                "category": "m.图书.人文社科.心理学",
                "url": "http://list.jd.com/list.html?cat=1713-3279&go=0"
            },
            {
                "category": "m.图书.人文社科.政治/军事",
                "url": "http://list.jd.com/list.html?cat=1713-3276&go=0"
            },
            {
                "category": "m.图书.人文社科.社会科学",
                "url": "http://list.jd.com/list.html?cat=1713-3281&go=0"
            },
            {
                "category": "m.图书.人文社科.法律",
                "url": "http://list.jd.com/list.html?cat=1713-3277&go=0"
            },
            {
                "category": "m.图书.人文社科.文化",
                "url": "http://list.jd.com/list.html?cat=1713-3280&go=0"
            },
            {
                "category": "m.图书.生活.家教与育儿",
                "url": "http://list.jd.com/list.html?cat=1713-3270&go=0"
            },
            {
                "category": "m.图书.生活.孕产",
                "url": "http://list.jd.com/list.html?cat=1713-3270-3509&go=0"
            },
            {
                "category": "m.图书.生活.健身保健",
                "url": "http://list.jd.com/list.html?cat=1713-3269&go=0"
            },
            {
                "category": "m.图书.生活.旅游/地图",
                "url": "http://list.jd.com/list.html?cat=1713-3271&go=0"
            },
            {
                "category": "m.图书.生活.美食",
                "url": "http://list.jd.com/list.html?cat=1713-9278&go=0"
            },
            {
                "category": "m.图书.生活.时尚美妆",
                "url": "http://list.jd.com/list.html?cat=1713-9291&go=0"
            },
            {
                "category": "m.图书.生活.家居",
                "url": "http://list.jd.com/list.html?cat=1713-9301&go=0"
            },
            {
                "category": "m.图书.生活.手工DIY",
                "url": "http://list.jd.com/list.html?cat=1713-9314-9315&go=0"
            },
            {
                "category": "m.图书.生活.两性",
                "url": "http://list.jd.com/list.html?cat=1713-9309&go=0"
            },
            {
                "category": "m.图书.生活.体育",
                "url": "http://list.jd.com/list.html?cat=1713-3288&go=0"
            },
            {
                "category": "m.图书.科技.计算机与互联网",
                "url": "http://list.jd.com/list.html?cat=1713-3287&go=0"
            },
            {
                "category": "m.图书.科技.建筑",
                "url": "http://list.jd.com/list.html?cat=1713-3284&go=0"
            },
            {
                "category": "m.图书.科技.工业技术",
                "url": "http://list.jd.com/list.html?cat=1713-3282&go=0"
            },
            {
                "category": "m.图书.科技.电子/通信",
                "url": "http://list.jd.com/list.html?cat=1713-9351&go=0"
            },
            {
                "category": "m.图书.科技.医学",
                "url": "http://list.jd.com/list.html?cat=1713-3285&go=0"
            },
            {
                "category": "m.图书.科技.科学与自然",
                "url": "http://list.jd.com/list.html?cat=1713-3286&go=0"
            },
            {
                "category": "m.图书.科技.农林",
                "url": "http://list.jd.com/list.html?cat=1713-9368&go=0"
            },
            {
                "category": "m.图书.刊/原版.杂志/期刊",
                "url": "http://list.jd.com/list.html?cat=1713-4758&go=0"
            },
            {
                "category": "m.图书.刊/原版.英文原版书",
                "url": "http://list.jd.com/list.html?cat=1713-4855&go=0"
            },
            {
                "category": "m.图书.刊/原版.港台图书",
                "url": "http://list.jd.com/list.html?cat=1713-6929&go=0"
            },
            {
                "category": "m.图书.电子书.小说",
                "url": "http://list.jd.com/list.html?cat=e.jd.com/products/5272-5278.html&go=0"
            },
            {
                "category": "m.图书.电子书.励志与成功",
                "url": "http://list.jd.com/list.html?cat=e.jd.com/products/5272-5287.html&go=0"
            },
            {
                "category": "m.图书.电子书.经济金融",
                "url": "http://list.jd.com/list.html?cat=e.jd.com/products/5272-12438.html&go=0"
            },
            {
                "category": "m.图书.电子书.文学",
                "url": "http://list.jd.com/list.html?cat=e.jd.com/products/5272-5279.html&go=0"
            },
            {
                "category": "m.图书.电子书.社科",
                "url": "http://list.jd.com/list.html?cat=e.jd.com/products/5272-5301.html&go=0"
            },
            {
                "category": "m.图书.电子书.婚恋两性",
                "url": "http://list.jd.com/list.html?cat=e.jd.com/products/5272-10884.html&go=0"
            },
            {
                "category": "m.图书.电子书.外文原版",
                "url": "http://list.jd.com/list.html?cat=e.jd.com/products/5272-6828.html&go=0"
            },
            {
                "category": "m.图书.电子书.免费",
                "url": "http://list.jd.com/list.html?cat=e.jd.com/products/5272-5276.html&go=0"
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
