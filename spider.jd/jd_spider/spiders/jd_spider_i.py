# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

import scrapy
import json
import datetime

from ..items import ShellerInfoItem


class JDSpider(scrapy.Spider):
    name = "jd_spider_i"

    def start_requests(self):

        data1 = [
            {
                "category": "i.汽车.汽车价格.5万以下",
                "url": "http://list.jd.com/list.html?cat=car.jd.com/hmc/select/0-5&go=0"
            },
            {
                "category": "i.汽车.汽车价格.5-8万",
                "url": "http://list.jd.com/list.html?cat=car.jd.com/hmc/select/5-8&go=0"
            },
            {
                "category": "i.汽车.汽车价格.8-10万",
                "url": "http://list.jd.com/list.html?cat=car.jd.com/hmc/select/8-10&go=0"
            },
            {
                "category": "i.汽车.汽车价格.10-15万",
                "url": "http://list.jd.com/list.html?cat=car.jd.com/hmc/select/10-15&go=0"
            },
            {
                "category": "i.汽车.汽车价格.15-25万",
                "url": "http://list.jd.com/list.html?cat=car.jd.com/hmc/select/15-25&go=0"
            },
            {
                "category": "i.汽车.汽车价格.25-40万",
                "url": "http://list.jd.com/list.html?cat=car.jd.com/hmc/select/25-40&go=0"
            },
            {
                "category": "i.汽车.汽车价格.40万以上",
                "url": "http://list.jd.com/list.html?cat=car.jd.com/hmc/select/40-_&go=0"
            },
            {
                "category": "i.汽车.汽车品牌.东风标致",
                "url": "http://list.jd.com/list.html?cat=mall.jd.com/index-127277.html&go=0"
            },
            {
                "category": "i.汽车.汽车品牌.东风风行",
                "url": "http://list.jd.com/list.html?cat=mall.jd.com/index-154463.html&go=0"
            },
            {
                "category": "i.汽车.汽车品牌.东风雪铁龙",
                "url": "http://list.jd.com/list.html?cat=mall.jd.com/index-153157.html&go=0"
            },
            {
                "category": "i.汽车.汽车品牌.天津一汽",
                "url": "http://list.jd.com/list.html?cat=mall.jd.com/index-185901.html&go=0"
            },
            {
                "category": "i.汽车.汽车品牌.陆风",
                "url": "http://list.jd.com/list.html?cat=mall.jd.com/index-144691.html&go=0"
            },
            {
                "category": "i.汽车.汽车品牌.一汽奔腾",
                "url": "http://list.jd.com/list.html?cat=mall.jd.com/index-143184.html&go=0"
            },
            {
                "category": "i.汽车.维修保养.机油",
                "url": "http://list.jd.com/list.html?cat=6728-6742-11849&go=0"
            },
            {
                "category": "i.汽车.维修保养.添加剂",
                "url": "http://list.jd.com/list.html?cat=6728-6742-11850&go=0"
            },
            {
                "category": "i.汽车.维修保养.防冻液",
                "url": "http://list.jd.com/list.html?cat=6728-6742-6756&go=0"
            },
            {
                "category": "i.汽车.维修保养.滤清器",
                "url": "http://list.jd.com/list.html?cat=6728-6742-11852&go=0"
            },
            {
                "category": "i.汽车.维修保养.火花塞",
                "url": "http://list.jd.com/list.html?cat=6728-6742-6767&go=0"
            },
            {
                "category": "i.汽车.维修保养.雨刷",
                "url": "http://list.jd.com/list.html?cat=6728-6742-6766&go=0"
            },
            {
                "category": "i.汽车.维修保养.车灯",
                "url": "http://list.jd.com/list.html?cat=6728-6742-6768&go=0"
            },
            {
                "category": "i.汽车.维修保养.减震器",
                "url": "http://list.jd.com/list.html?cat=6728-6742-13243&go=0"
            },
            {
                "category": "i.汽车.维修保养.轮胎",
                "url": "http://list.jd.com/list.html?cat=6728-6742-9248&go=0"
            },
            {
                "category": "i.汽车.维修保养.轮毂",
                "url": "http://list.jd.com/list.html?cat=6728-6742-11951&go=0"
            },
            {
                "category": "i.汽车.维修保养.刹车片/盘",
                "url": "http://list.jd.com/list.html?cat=6728-6742-11859&go=0"
            },
            {
                "category": "i.汽车.维修保养.维修配件",
                "url": "http://list.jd.com/list.html?cat=6728-6742-6769&go=0"
            },
            {
                "category": "i.汽车.维修保养.蓄电池",
                "url": "http://list.jd.com/list.html?cat=6728-6742-9971&go=0"
            },
            {
                "category": "i.汽车.维修保养.底盘装甲/护板",
                "url": "http://list.jd.com/list.html?cat=6728-6742-9964&go=0"
            },
            {
                "category": "i.汽车.维修保养.贴膜",
                "url": "http://list.jd.com/list.html?cat=6728-6742-6770&go=0"
            },
            {
                "category": "i.汽车.维修保养.汽修工具",
                "url": "http://list.jd.com/list.html?cat=6728-6742-6795&go=0"
            },
            {
                "category": "i.汽车.维修保养.改装配件",
                "url": "http://list.jd.com/list.html?cat=6728-6742-12406&go=0"
            },
            {
                "category": "i.汽车.维修保养.正时皮带",
                "url": "http://list.jd.com/list.html?cat=6728-6742-13244&go=0"
            },
            {
                "category": "i.汽车.维修保养.汽车喇叭",
                "url": "http://list.jd.com/list.html?cat=6728-6742-13245&go=0"
            },
            {
                "category": "i.汽车.车载电器.行车记录仪",
                "url": "http://list.jd.com/list.html?cat=6728-6740-6964&go=0"
            },
            {
                "category": "i.汽车.车载电器.导航仪",
                "url": "http://list.jd.com/list.html?cat=6728-6740-11867&go=0"
            },
            {
                "category": "i.汽车.车载电器.电源",
                "url": "http://list.jd.com/list.html?cat=6728-6740-6749&go=0"
            },
            {
                "category": "i.汽车.车载电器.电器配件",
                "url": "http://list.jd.com/list.html?cat=6728-6740-13247&go=0"
            },
            {
                "category": "i.汽车.车载电器.净化器",
                "url": "http://list.jd.com/list.html?cat=6728-6740-6807&go=0"
            },
            {
                "category": "i.汽车.车载电器.车载影音",
                "url": "http://list.jd.com/list.html?cat=6728-6740-6965&go=0"
            },
            {
                "category": "i.汽车.车载电器.冰箱",
                "url": "http://list.jd.com/list.html?cat=6728-6740-6753&go=0"
            },
            {
                "category": "i.汽车.车载电器.安全预警仪",
                "url": "http://list.jd.com/list.html?cat=6728-6740-9959&go=0"
            },
            {
                "category": "i.汽车.车载电器.倒车雷达",
                "url": "http://list.jd.com/list.html?cat=6728-6740-9961&go=0"
            },
            {
                "category": "i.汽车.车载电器.蓝牙设备",
                "url": "http://list.jd.com/list.html?cat=6728-6740-9962&go=0"
            },
            {
                "category": "i.汽车.车载电器.智能驾驶",
                "url": "http://list.jd.com/list.html?cat=6728-6740-12408&go=0"
            },
            {
                "category": "i.汽车.车载电器.车载电台",
                "url": "http://list.jd.com/list.html?cat=6728-6740-12409&go=0"
            },
            {
                "category": "i.汽车.车载电器.吸尘器",
                "url": "http://list.jd.com/list.html?cat=6728-6740-6752&go=0"
            },
            {
                "category": "i.汽车.车载电器.智能车机",
                "url": "http://list.jd.com/list.html?cat=6728-6740-13248&go=0"
            },
            {
                "category": "i.汽车.车载电器.汽车音响",
                "url": "http://list.jd.com/list.html?cat=6728-6740-13249&go=0"
            },
            {
                "category": "i.汽车.车载电器.车载生活电器",
                "url": "http://list.jd.com/list.html?cat=6728-6740-13250&go=0"
            },
            {
                "category": "i.汽车.美容清洗.车蜡",
                "url": "http://list.jd.com/list.html?cat=6728-6743-11875&go=0"
            },
            {
                "category": "i.汽车.美容清洗.镀晶镀膜",
                "url": "http://list.jd.com/list.html?cat=6728-6743-13251&go=0"
            },
            {
                "category": "i.汽车.美容清洗.补漆笔",
                "url": "http://list.jd.com/list.html?cat=6728-6743-9974&go=0"
            },
            {
                "category": "i.汽车.美容清洗.玻璃水",
                "url": "http://list.jd.com/list.html?cat=6728-6743-6757&go=0"
            },
            {
                "category": "i.汽车.美容清洗.清洁剂",
                "url": "http://list.jd.com/list.html?cat=6728-6743-11878&go=0"
            },
            {
                "category": "i.汽车.美容清洗.洗车机",
                "url": "http://list.jd.com/list.html?cat=6728-6743-13252&go=0"
            },
            {
                "category": "i.汽车.美容清洗.洗车水枪",
                "url": "http://list.jd.com/list.html?cat=6728-6743-13253&go=0"
            },
            {
                "category": "i.汽车.美容清洗.洗车配件",
                "url": "http://list.jd.com/list.html?cat=6728-6743-11880&go=0"
            },
            {
                "category": "i.汽车.美容清洗.毛巾掸子",
                "url": "http://list.jd.com/list.html?cat=6728-6743-13254&go=0"
            },
            {
                "category": "i.汽车.汽车装饰.脚垫",
                "url": "http://list.jd.com/list.html?cat=6728-6745-11883&go=0"
            },
            {
                "category": "i.汽车.汽车装饰.座垫",
                "url": "http://list.jd.com/list.html?cat=6728-6745-11881&go=0"
            },
            {
                "category": "i.汽车.汽车装饰.座套",
                "url": "http://list.jd.com/list.html?cat=6728-6745-11882&go=0"
            },
            {
                "category": "i.汽车.汽车装饰.后备箱垫",
                "url": "http://list.jd.com/list.html?cat=6728-6745-6972&go=0"
            },
            {
                "category": "i.汽车.汽车装饰.方向盘套",
                "url": "http://list.jd.com/list.html?cat=6728-6745-13255&go=0"
            },
            {
                "category": "i.汽车.汽车装饰.头枕腰靠",
                "url": "http://list.jd.com/list.html?cat=6728-6745-11887&go=0"
            },
            {
                "category": "i.汽车.汽车装饰.香水",
                "url": "http://list.jd.com/list.html?cat=6728-6745-6785&go=0"
            },
            {
                "category": "i.汽车.汽车装饰.空气净化",
                "url": "http://list.jd.com/list.html?cat=6728-6745-11886&go=0"
            },
            {
                "category": "i.汽车.汽车装饰.功能小件",
                "url": "http://list.jd.com/list.html?cat=6728-6745-11889&go=0"
            },
            {
                "category": "i.汽车.汽车装饰.车衣",
                "url": "http://list.jd.com/list.html?cat=6728-6745-6798&go=0"
            },
            {
                "category": "i.汽车.汽车装饰.挂件摆件",
                "url": "http://list.jd.com/list.html?cat=6728-6745-11888&go=0"
            },
            {
                "category": "i.汽车.汽车装饰.车身装饰件",
                "url": "http://list.jd.com/list.html?cat=6728-6745-11953&go=0"
            },
            {
                "category": "i.汽车.安全自驾.安全座椅",
                "url": "http://list.jd.com/list.html?cat=6728-6747-6792&go=0"
            },
            {
                "category": "i.汽车.安全自驾.胎压监测",
                "url": "http://list.jd.com/list.html?cat=6728-6747-11954&go=0"
            },
            {
                "category": "i.汽车.安全自驾.充气泵",
                "url": "http://list.jd.com/list.html?cat=6728-6747-12407&go=0"
            },
            {
                "category": "i.汽车.安全自驾.防盗设备",
                "url": "http://list.jd.com/list.html?cat=6728-6747-11955&go=0"
            },
            {
                "category": "i.汽车.安全自驾.应急救援",
                "url": "http://list.jd.com/list.html?cat=6728-6747-6796&go=0"
            },
            {
                "category": "i.汽车.安全自驾.保温箱",
                "url": "http://list.jd.com/list.html?cat=6728-6747-6804&go=0"
            },
            {
                "category": "i.汽车.安全自驾.储物箱",
                "url": "http://list.jd.com/list.html?cat=6728-6747-6801&go=0"
            },
            {
                "category": "i.汽车.安全自驾.自驾野营",
                "url": "http://list.jd.com/list.html?cat=6728-6747-11898&go=0"
            },
            {
                "category": "i.汽车.安全自驾.摩托车装备",
                "url": "http://list.jd.com/list.html?cat=6728-6747-9985&go=0"
            },
            {
                "category": "i.汽车.安全自驾.摩托车",
                "url": "http://list.jd.com/list.html?cat=6728-6747-13270&go=0"
            },
            {
                "category": "i.汽车.汽车服务.清洗美容",
                "url": "http://list.jd.com/list.html?cat=6728-12402-12403&go=0"
            },
            {
                "category": "i.汽车.汽车服务.功能升级",
                "url": "http://list.jd.com/list.html?cat=6728-12402-12404&go=0"
            },
            {
                "category": "i.汽车.汽车服务.保养维修",
                "url": "http://list.jd.com/list.html?cat=6728-12402-12405&go=0"
            },
            {
                "category": "i.汽车.汽车服务.驾驶培训",
                "url": "http://list.jd.com/list.html?cat=6728-12402-13267&go=0"
            },
            {
                "category": "i.汽车.汽车服务.ETC",
                "url": "http://list.jd.com/list.html?cat=6728-12402-13266&go=0"
            },
            {
                "category": "i.汽车.汽车服务.加油卡",
                "url": "http://list.jd.com/list.html?cat=6728-12402-13242&go=0"
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
