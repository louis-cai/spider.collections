# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

import scrapy
import json
import datetime

from ..items import ShellerInfoItem


class JDSpider(scrapy.Spider):
    name = "jd_spider_j"

    def start_requests(self):

        data1 = [
            {
                "category": "j.母婴.奶粉.1段",
                "url": "http://list.jd.com/list.html?cat=1319,1523,7052&ev=12212_121497&go=0&JL=2_1_0"
            },
            {
                "category": "j.母婴.奶粉.2段",
                "url": "http://list.jd.com/list.html?cat=1319,1523,7052&ev=12212_121498&go=0&JL=2_1_0"
            },
            {
                "category": "j.母婴.奶粉.3段",
                "url": "http://list.jd.com/list.html?cat=1319,1523,7052&ev=12212%5F121499&go=0&JL=2_1_0"
            },
            {
                "category": "j.母婴.奶粉.4段",
                "url": "http://list.jd.com/list.html?cat=1319,1523,7052&ev=12212%5F121500&go=0&JL=2_1_0"
            },
            {
                "category": "j.母婴.奶粉.孕妈奶粉",
                "url": "http://list.jd.com/list.html?cat=1319-1523-7054&go=0"
            },
            {
                "category": "j.母婴.奶粉.特殊配方奶粉",
                "url": "http://list.jd.com/list.html?cat=1319,1523,7052&ev=115919%5F651826&go=0&JL=2_1_0"
            },
            {
                "category": "j.母婴.奶粉.有机奶粉",
                "url": "http://list.jd.com/list.html?cat=1319,1523,7052&ev=115919%5F651825&go=0&JL=2_1_0"
            },
            {
                "category": "j.母婴.营养辅食.米粉/菜粉",
                "url": "http://list.jd.com/list.html?cat=1319-1524-1533&go=0"
            },
            {
                "category": "j.母婴.营养辅食.面条/粥",
                "url": "http://list.jd.com/list.html?cat=1319-1524-9399&go=0"
            },
            {
                "category": "j.母婴.营养辅食.果泥/果汁",
                "url": "http://list.jd.com/list.html?cat=1319-1524-1534&go=0"
            },
            {
                "category": "j.母婴.营养辅食.益生菌/初乳",
                "url": "http://list.jd.com/list.html?cat=1319-1524-1537&go=0"
            },
            {
                "category": "j.母婴.营养辅食.DHA",
                "url": "http://list.jd.com/list.html?cat=1319-1524-7055&go=0"
            },
            {
                "category": "j.母婴.营养辅食.钙铁锌/维生素",
                "url": "http://list.jd.com/list.html?cat=1319-1524-1538&go=0"
            },
            {
                "category": "j.母婴.营养辅食.清火/开胃",
                "url": "http://list.jd.com/list.html?cat=1319-1524-1539&go=0"
            },
            {
                "category": "j.母婴.营养辅食.宝宝零食",
                "url": "http://list.jd.com/list.html?cat=1319-1524-12191&go=0"
            },
            {
                "category": "j.母婴.尿裤湿巾.NB",
                "url": "http://list.jd.com/list.html?cat=1319,1525,7057&ev=105925%5F614543&go=0&JL=2_1_0"
            },
            {
                "category": "j.母婴.尿裤湿巾.S",
                "url": "http://list.jd.com/list.html?cat=1319,1525,7057&ev=105925%5F614545&go=0&JL=2_1_0"
            },
            {
                "category": "j.母婴.尿裤湿巾.M",
                "url": "http://list.jd.com/list.html?cat=1319,1525,7057&ev=105925%5F614548&go=0&JL=2_1_0"
            },
            {
                "category": "j.母婴.尿裤湿巾.L",
                "url": "http://list.jd.com/list.html?cat=1319,1525,7057&ev=105925%5F614553&go=0&JL=2_1_0"
            },
            {
                "category": "j.母婴.尿裤湿巾.XL",
                "url": "http://list.jd.com/list.html?cat=1319,1525,7057&ev=105925%5F614555&go=0&JL=2_1_0"
            },
            {
                "category": "j.母婴.尿裤湿巾.XXL",
                "url": "http://list.jd.com/list.html?cat=1319,1525,7057&ev=105925%5F614557&go=0&JL=2_1_0"
            },
            {
                "category": "j.母婴.尿裤湿巾.拉拉裤",
                "url": "http://list.jd.com/list.html?cat=1319-1525-1546&go=0"
            },
            {
                "category": "j.母婴.尿裤湿巾.成人尿裤",
                "url": "http://list.jd.com/list.html?cat=1319-1525-7058&go=0"
            },
            {
                "category": "j.母婴.尿裤湿巾.婴儿湿巾",
                "url": "http://list.jd.com/list.html?cat=1319-1525-1548&go=0"
            },
            {
                "category": "j.母婴.喂养用品.奶瓶奶嘴",
                "url": "http://list.jd.com/list.html?cat=1319-1526-7060&go=0"
            },
            {
                "category": "j.母婴.喂养用品.吸奶器",
                "url": "http://list.jd.com/list.html?cat=1319-1526-1550&go=0"
            },
            {
                "category": "j.母婴.喂养用品.暖奶消毒",
                "url": "http://list.jd.com/list.html?cat=1319-1526-1551&go=0"
            },
            {
                "category": "j.母婴.喂养用品.辅食料理机",
                "url": "http://list.jd.com/list.html?cat=1319-1526-12197&go=0"
            },
            {
                "category": "j.母婴.喂养用品.牙胶安抚",
                "url": "http://list.jd.com/list.html?cat=1319-1526-1553&go=0"
            },
            {
                "category": "j.母婴.喂养用品.食物存储",
                "url": "http://list.jd.com/list.html?cat=1319-1526-13287&go=0"
            },
            {
                "category": "j.母婴.喂养用品.儿童餐具",
                "url": "http://list.jd.com/list.html?cat=1319-1526-1552&go=0"
            },
            {
                "category": "j.母婴.喂养用品.水壶/水杯",
                "url": "http://list.jd.com/list.html?cat=1319-1526-7061&go=0"
            },
            {
                "category": "j.母婴.喂养用品.围兜/防溅衣",
                "url": "http://list.jd.com/list.html?cat=1319-1526-13286&go=0"
            },
            {
                "category": "j.母婴.洗护用品.宝宝护肤",
                "url": "http://list.jd.com/list.html?cat=1319-1527-1556&go=0"
            },
            {
                "category": "j.母婴.洗护用品.日常护理",
                "url": "http://list.jd.com/list.html?cat=1319-1527-1559&go=0"
            },
            {
                "category": "j.母婴.洗护用品.洗发沐浴",
                "url": "http://list.jd.com/list.html?cat=1319-1527-1555&go=0"
            },
            {
                "category": "j.母婴.洗护用品.洗澡用具",
                "url": "http://list.jd.com/list.html?cat=1319-1527-13288&go=0"
            },
            {
                "category": "j.母婴.洗护用品.洗衣液/皂",
                "url": "http://list.jd.com/list.html?cat=1319-1527-1557&go=0"
            },
            {
                "category": "j.母婴.洗护用品.理发器",
                "url": "http://list.jd.com/list.html?cat=1319-1527-12341&go=0"
            },
            {
                "category": "j.母婴.洗护用品.婴儿口腔清洁",
                "url": "http://list.jd.com/list.html?cat=1319-1527-13289&go=0"
            },
            {
                "category": "j.母婴.洗护用品.座便器",
                "url": "http://list.jd.com/list.html?cat=1319-1527-1562&go=0"
            },
            {
                "category": "j.母婴.洗护用品.驱蚊防晒",
                "url": "http://list.jd.com/list.html?cat=1319-1527-1560&go=0"
            },
            {
                "category": "j.母婴.寝居服饰.睡袋/抱被",
                "url": "http://list.jd.com/list.html?cat=1319-6313-13290&go=0"
            },
            {
                "category": "j.母婴.寝居服饰.家居床品",
                "url": "http://list.jd.com/list.html?cat=1319-6313-6316&go=0"
            },
            {
                "category": "j.母婴.寝居服饰.安全防护",
                "url": "http://list.jd.com/list.html?cat=1319-6313-6317&go=0"
            },
            {
                "category": "j.母婴.寝居服饰.爬行垫",
                "url": "http://list.jd.com/list.html?cat=1319-6313-13291&go=0"
            },
            {
                "category": "j.母婴.寝居服饰.婴儿内衣",
                "url": "http://list.jd.com/list.html?cat=1319-6313-11234&go=0"
            },
            {
                "category": "j.母婴.寝居服饰.婴儿礼盒",
                "url": "http://list.jd.com/list.html?cat=1319-6313-11235&go=0"
            },
            {
                "category": "j.母婴.寝居服饰.婴儿鞋帽袜",
                "url": "http://list.jd.com/list.html?cat=1319-6313-6315&go=0"
            },
            {
                "category": "j.母婴.寝居服饰.婴儿外出服",
                "url": "http://list.jd.com/list.html?cat=1319-6313-6314&go=0"
            },
            {
                "category": "j.母婴.妈妈专区.防辐射服",
                "url": "http://list.jd.com/list.html?cat=1319-4997-4999&go=0"
            },
            {
                "category": "j.母婴.妈妈专区.孕妈装",
                "url": "http://list.jd.com/list.html?cat=1319-4997-4998&go=0"
            },
            {
                "category": "j.母婴.妈妈专区.孕妇护肤",
                "url": "http://list.jd.com/list.html?cat=1319-4997-5000&go=0"
            },
            {
                "category": "j.母婴.妈妈专区.妈咪包/背婴带",
                "url": "http://list.jd.com/list.html?cat=1319-4997-5002&go=0"
            },
            {
                "category": "j.母婴.妈妈专区.待产护理",
                "url": "http://list.jd.com/list.html?cat=1319-4997-12198&go=0"
            },
            {
                "category": "j.母婴.妈妈专区.产后塑身",
                "url": "http://list.jd.com/list.html?cat=1319-4997-5001&go=0"
            },
            {
                "category": "j.母婴.妈妈专区.文胸/内裤",
                "url": "http://list.jd.com/list.html?cat=1319-4997-7062&go=0"
            },
            {
                "category": "j.母婴.妈妈专区.防溢乳垫",
                "url": "http://list.jd.com/list.html?cat=1319-4997-13292&go=0"
            },
            {
                "category": "j.母婴.妈妈专区.孕期营养",
                "url": "http://list.jd.com/list.html?cat=1319-4997-6319&go=0"
            },
            {
                "category": "j.母婴.童车童床.安全座椅",
                "url": "http://list.jd.com/list.html?cat=1319-12193-12195&go=0"
            },
            {
                "category": "j.母婴.童车童床.婴儿推车",
                "url": "http://list.jd.com/list.html?cat=1319-1528-1563&go=0"
            },
            {
                "category": "j.母婴.童车童床.婴儿床",
                "url": "http://list.jd.com/list.html?cat=1319-1528-1564&go=0"
            },
            {
                "category": "j.母婴.童车童床.婴儿床垫",
                "url": "http://list.jd.com/list.html?cat=1319-1528-13293&go=0"
            },
            {
                "category": "j.母婴.童车童床.餐椅",
                "url": "http://list.jd.com/list.html?cat=1319-1528-1565&go=0"
            },
            {
                "category": "j.母婴.童车童床.学步车",
                "url": "http://list.jd.com/list.html?cat=1319-1528-1568&go=0"
            },
            {
                "category": "j.母婴.童车童床.三轮车",
                "url": "http://list.jd.com/list.html?cat=1319-1528-1569&go=0"
            },
            {
                "category": "j.母婴.童车童床.自行车",
                "url": "http://list.jd.com/list.html?cat=1319-1528-1566&go=0"
            },
            {
                "category": "j.母婴.童车童床.扭扭车",
                "url": "http://list.jd.com/list.html?cat=1319-1528-4702&go=0"
            },
            {
                "category": "j.母婴.童车童床.滑板车",
                "url": "http://list.jd.com/list.html?cat=1319-1528-12192&go=0"
            },
            {
                "category": "j.母婴.童车童床.电动车",
                "url": "http://list.jd.com/list.html?cat=1319-1528-1567&go=0"
            },
            {
                "category": "j.母婴.玩具.适用年龄",
                "url": "http://list.jd.com/list.html?cat=6233-6234&go=0"
            },
            {
                "category": "j.母婴.玩具.遥控/电动",
                "url": "http://list.jd.com/list.html?cat=6233-6235&go=0"
            },
            {
                "category": "j.母婴.玩具.益智玩具",
                "url": "http://list.jd.com/list.html?cat=6233-6271&go=0"
            },
            {
                "category": "j.母婴.玩具.积木拼插",
                "url": "http://list.jd.com/list.html?cat=6233-6275&go=0"
            },
            {
                "category": "j.母婴.玩具.动漫玩具",
                "url": "http://list.jd.com/list.html?cat=6233-6264&go=0"
            },
            {
                "category": "j.母婴.玩具.毛绒布艺",
                "url": "http://list.jd.com/list.html?cat=6233-6236&go=0"
            },
            {
                "category": "j.母婴.玩具.模型玩具",
                "url": "http://list.jd.com/list.html?cat=6233-6253&go=0"
            },
            {
                "category": "j.母婴.玩具.健身玩具",
                "url": "http://list.jd.com/list.html?cat=6233-6260&go=0"
            },
            {
                "category": "j.母婴.玩具.娃娃玩具",
                "url": "http://list.jd.com/list.html?cat=6233-6237&go=0"
            },
            {
                "category": "j.母婴.玩具.DIY玩具",
                "url": "http://list.jd.com/list.html?cat=6233-6279&go=0"
            },
            {
                "category": "j.母婴.玩具.创意减压",
                "url": "http://list.jd.com/list.html?cat=6233-6289&go=0"
            },
            {
                "category": "j.母婴.乐器.钢琴",
                "url": "http://list.jd.com/list.html?cat=6233-6291-6294&go=0"
            },
            {
                "category": "j.母婴.乐器.电子琴/电钢琴",
                "url": "http://list.jd.com/list.html?cat=6233-6291-6296&go=0"
            },
            {
                "category": "j.母婴.乐器.吉他/尤克里里",
                "url": "http://list.jd.com/list.html?cat=6233-6291-6299&go=0"
            },
            {
                "category": "j.母婴.乐器.打击乐器",
                "url": "http://list.jd.com/list.html?cat=6233-6291-6303&go=0"
            },
            {
                "category": "j.母婴.乐器.西洋管弦",
                "url": "http://list.jd.com/list.html?cat=6233-6291-6301&go=0"
            },
            {
                "category": "j.母婴.乐器.民族乐器",
                "url": "http://list.jd.com/list.html?cat=6233-6291-6300&go=0"
            },
            {
                "category": "j.母婴.乐器.乐器配件",
                "url": "http://list.jd.com/list.html?cat=6233-6291-6305&go=0"
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
