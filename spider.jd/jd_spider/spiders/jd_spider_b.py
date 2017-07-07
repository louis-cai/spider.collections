# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

import scrapy
import json
import datetime

from ..items import ShellerInfoItem


class JDSpider(scrapy.Spider):
    name = "jd_spider_b"

    def start_requests(self):

        data1 = [
            {
                "category": "b.手机.手机通讯.手机",
                "url": "http://list.jd.com/list.html?cat=9987-653-655&go=0"
            },
            {
                "category": "b.手机.手机通讯.对讲机",
                "url": "http://list.jd.com/list.html?cat=9987-653-659&go=0"
            },
            {
                "category": "b.手机.运营商.合约机",
                "url": "http://list.jd.com/list.html?cat=9987-6880-6881&go=0"
            },
            {
                "category": "b.手机.运营商.装宽带",
                "url": "http://list.jd.com/list.html?cat=9987,6880,12428"
            },
            {
                "category": "b.手机.手机配件.电池/移动电源",
                "url": "http://list.jd.com/list.html?cat=9987-830-860&go=0"
            },
            {
                "category": "b.手机.手机配件.蓝牙耳机",
                "url": "http://list.jd.com/list.html?cat=9987-830-863&go=0"
            },
            {
                "category": "b.手机.手机配件.充电器/数据线",
                "url": "http://list.jd.com/list.html?cat=9987-830-861&go=0"
            },
            {
                "category": "b.手机.手机配件.手机耳机",
                "url": "http://list.jd.com/list.html?cat=9987-830-862&go=0"
            },
            {
                "category": "b.手机.手机配件.手机支架",
                "url": "http://list.jd.com/list.html?cat=9987-830-12811&go=0"
            },
            {
                "category": "b.手机.手机配件.贴膜",
                "url": "http://list.jd.com/list.html?cat=9987-830-867&go=0"
            },
            {
                "category": "b.手机.手机配件.存储卡",
                "url": "http://list.jd.com/list.html?cat=9987-830-1099&go=0"
            },
            {
                "category": "b.手机.手机配件.保护套",
                "url": "http://list.jd.com/list.html?cat=9987-830-866&go=0"
            },
            {
                "category": "b.手机.手机配件.车载配件",
                "url": "http://list.jd.com/list.html?cat=9987-830-864&go=0"
            },
            {
                "category": "b.手机.手机配件.iPhone配件",
                "url": "http://list.jd.com/list.html?cat=9987-830-5003&go=0"
            },
            {
                "category": "b.手机.手机配件.创意配件",
                "url": "http://list.jd.com/list.html?cat=9987-830-868&go=0"
            },
            {
                "category": "b.手机.手机配件.便携/无线音箱",
                "url": "http://list.jd.com/list.html?cat=9987-830-11301&go=0"
            },
            {
                "category": "b.手机.手机配件.手机饰品",
                "url": "http://list.jd.com/list.html?cat=9987-830-11302&go=0"
            },
            {
                "category": "b.手机.手机配件.拍照配件",
                "url": "http://list.jd.com/list.html?cat=9987-830-12809&go=0"
            },
            {
                "category": "b.手机.摄影摄像.数码相机",
                "url": "http://list.jd.com/list.html?cat=652-654-831&go=0"
            },
            {
                "category": "b.手机.摄影摄像.单电/微单相机",
                "url": "http://list.jd.com/list.html?cat=652-654-5012&go=0"
            },
            {
                "category": "b.手机.摄影摄像.单反相机",
                "url": "http://list.jd.com/list.html?cat=652-654-832&go=0"
            },
            {
                "category": "b.手机.摄影摄像.拍立得",
                "url": "http://list.jd.com/list.html?cat=652-654-7170&go=0"
            },
            {
                "category": "b.手机.摄影摄像.运动相机",
                "url": "http://list.jd.com/list.html?cat=652-654-12342&go=0"
            },
            {
                "category": "b.手机.摄影摄像.摄像机",
                "url": "http://list.jd.com/list.html?cat=652-654-833&go=0"
            },
            {
                "category": "b.手机.摄影摄像.镜头",
                "url": "http://list.jd.com/list.html?cat=652-654-834&go=0"
            },
            {
                "category": "b.手机.摄影摄像.户外器材",
                "url": "http://list.jd.com/list.html?cat=652-654-12343&go=0"
            },
            {
                "category": "b.手机.摄影摄像.影棚器材",
                "url": "http://list.jd.com/list.html?cat=652-654-12344&go=0"
            },
            {
                "category": "b.手机.摄影摄像.冲印服务",
                "url": "http://list.jd.com/list.html?cat=652-654-12415&go=0"
            },
            {
                "category": "b.手机.摄影摄像.数码相框",
                "url": "http://list.jd.com/list.html?cat=652-654-844&go=0"
            },
            {
                "category": "b.手机.数码配件.存储卡",
                "url": "http://list.jd.com/list.html?cat=652-829-845&go=0"
            },
            {
                "category": "b.手机.数码配件.读卡器",
                "url": "http://list.jd.com/list.html?cat=652-829-846&go=0"
            },
            {
                "category": "b.手机.数码配件.支架",
                "url": "http://list.jd.com/list.html?cat=652-829-12810&go=0"
            },
            {
                "category": "b.手机.数码配件.滤镜",
                "url": "http://list.jd.com/list.html?cat=652-829-835&go=0"
            },
            {
                "category": "b.手机.数码配件.闪光灯/手柄",
                "url": "http://list.jd.com/list.html?cat=652-829-836&go=0"
            },
            {
                "category": "b.手机.数码配件.相机包",
                "url": "http://list.jd.com/list.html?cat=652-829-847&go=0"
            },
            {
                "category": "b.手机.数码配件.三脚架/云台",
                "url": "http://list.jd.com/list.html?cat=652-829-848&go=0"
            },
            {
                "category": "b.手机.数码配件.相机清洁/贴膜",
                "url": "http://list.jd.com/list.html?cat=652-829-851&go=0"
            },
            {
                "category": "b.手机.数码配件.机身附件",
                "url": "http://list.jd.com/list.html?cat=652-829-10971&go=0"
            },
            {
                "category": "b.手机.数码配件.镜头附件",
                "url": "http://list.jd.com/list.html?cat=652-829-10972&go=0"
            },
            {
                "category": "b.手机.数码配件.电池/充电器",
                "url": "http://list.jd.com/list.html?cat=652-829-854&go=0"
            },
            {
                "category": "b.手机.数码配件.移动电源",
                "url": "http://list.jd.com/list.html?cat=652-829-1219&go=0"
            },
            {
                "category": "b.手机.影音娱乐.耳机/耳麦",
                "url": "http://list.jd.com/list.html?cat=652-828-842&go=0"
            },
            {
                "category": "b.手机.影音娱乐.音箱/音响",
                "url": "http://list.jd.com/list.html?cat=652-828-841&go=0"
            },
            {
                "category": "b.手机.影音娱乐.收音机",
                "url": "http://list.jd.com/list.html?cat=652-828-12808&go=0"
            },
            {
                "category": "b.手机.影音娱乐.麦克风",
                "url": "http://list.jd.com/list.html?cat=652-828-869&go=0"
            },
            {
                "category": "b.手机.影音娱乐.MP3/MP4",
                "url": "http://list.jd.com/list.html?cat=652-828-837&go=0"
            },
            {
                "category": "b.手机.影音娱乐.专业音频",
                "url": "http://list.jd.com/list.html?cat=652-828-962&go=0"
            },
            {
                "category": "b.手机.影音娱乐.苹果周边",
                "url": "http://list.jd.com/list.html?cat=652-828-5270&go=0"
            },
            {
                "category": "b.手机.智能设备.智能手环",
                "url": "http://list.jd.com/list.html?cat=652-12345-12347&go=0"
            },
            {
                "category": "b.手机.智能设备.智能手表",
                "url": "http://list.jd.com/list.html?cat=652-12345-12348&go=0"
            },
            {
                "category": "b.手机.智能设备.智能眼镜",
                "url": "http://list.jd.com/list.html?cat=652-12345-12349&go=0"
            },
            {
                "category": "b.手机.智能设备.智能机器人",
                "url": "http://list.jd.com/list.html?cat=652-12345-12806&go=0"
            },
            {
                "category": "b.手机.智能设备.运动跟踪器",
                "url": "http://list.jd.com/list.html?cat=652-12345-12350&go=0"
            },
            {
                "category": "b.手机.智能设备.健康监测",
                "url": "http://list.jd.com/list.html?cat=652-12345-12351&go=0"
            },
            {
                "category": "b.手机.智能设备.智能配饰",
                "url": "http://list.jd.com/list.html?cat=652-12345-12352&go=0"
            },
            {
                "category": "b.手机.智能设备.智能家居",
                "url": "http://list.jd.com/list.html?cat=652-12345-12353&go=0"
            },
            {
                "category": "b.手机.智能设备.体感车",
                "url": "http://list.jd.com/list.html?cat=652-12345-12354&go=0"
            },
            {
                "category": "b.手机.智能设备.无人机",
                "url": "http://list.jd.com/list.html?cat=652-12345-12807&go=0"
            },
            {
                "category": "b.手机.智能设备.其他配件",
                "url": "http://list.jd.com/list.html?cat=652-12345-12355&go=0"
            },
            {
                "category": "b.手机.电子教育.学生平板",
                "url": "http://list.jd.com/list.html?cat=652-12346-12358&go=0"
            },
            {
                "category": "b.手机.电子教育.点读机/笔",
                "url": "http://list.jd.com/list.html?cat=652-12346-12357&go=0"
            },
            {
                "category": "b.手机.电子教育.早教益智",
                "url": "http://list.jd.com/list.html?cat=652-12346-12359&go=0"
            },
            {
                "category": "b.手机.电子教育.录音笔",
                "url": "http://list.jd.com/list.html?cat=652-12346-840&go=0"
            },
            {
                "category": "b.手机.电子教育.电纸书",
                "url": "http://list.jd.com/list.html?cat=652-12346-1203&go=0"
            },
            {
                "category": "b.手机.电子教育.电子词典",
                "url": "http://list.jd.com/list.html?cat=652-12346-838&go=0"
            },
            {
                "category": "b.手机.电子教育.复读机",
                "url": "http://list.jd.com/list.html?cat=652-12346-12356&go=0"
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
