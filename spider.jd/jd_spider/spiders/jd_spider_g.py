# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

import scrapy
import json
import datetime

from ..items import ShellerInfoItem


class JDSpider(scrapy.Spider):
    name = "jd_spider_g"

    def start_requests(self):

        data1 = [
            {
                "category": "g.鞋靴.时尚女鞋.单鞋",
                "url": "http://list.jd.com/list.html?cat=11729-11731-6914&go=0"
            },
            {
                "category": "g.鞋靴.时尚女鞋.休闲鞋",
                "url": "http://list.jd.com/list.html?cat=11729-11731-6916&go=0"
            },
            {
                "category": "g.鞋靴.时尚女鞋.帆布鞋",
                "url": "http://list.jd.com/list.html?cat=11729-11731-9774&go=0"
            },
            {
                "category": "g.鞋靴.时尚女鞋.鱼嘴鞋",
                "url": "http://list.jd.com/list.html?cat=11729-11731-6915&go=0"
            },
            {
                "category": "g.鞋靴.时尚女鞋.妈妈鞋",
                "url": "http://list.jd.com/list.html?cat=11729-11731-9778&go=0"
            },
            {
                "category": "g.鞋靴.时尚女鞋.凉鞋",
                "url": "http://list.jd.com/list.html?cat=11729-11731-6917&go=0"
            },
            {
                "category": "g.鞋靴.时尚女鞋.拖鞋/人字拖",
                "url": "http://list.jd.com/list.html?cat=11729-11731-9775&go=0"
            },
            {
                "category": "g.鞋靴.时尚女鞋.布鞋/绣花鞋",
                "url": "http://list.jd.com/list.html?cat=11729-11731-6918&go=0"
            },
            {
                "category": "g.鞋靴.时尚女鞋.坡跟鞋",
                "url": "http://list.jd.com/list.html?cat=11729-11731-12061&go=0"
            },
            {
                "category": "g.鞋靴.时尚女鞋.松糕鞋",
                "url": "http://list.jd.com/list.html?cat=11729-11731-12062&go=0"
            },
            {
                "category": "g.鞋靴.时尚女鞋.防水台",
                "url": "http://list.jd.com/list.html?cat=11729-11731-12064&go=0"
            },
            {
                "category": "g.鞋靴.时尚女鞋.高跟鞋",
                "url": "http://list.jd.com/list.html?cat=11729-11731-9772&go=0"
            },
            {
                "category": "g.鞋靴.时尚女鞋.踝靴",
                "url": "http://list.jd.com/list.html?cat=11729-11731-9769&go=0"
            },
            {
                "category": "g.鞋靴.时尚女鞋.内增高",
                "url": "http://list.jd.com/list.html?cat=11729-11731-12063&go=0"
            },
            {
                "category": "g.鞋靴.时尚女鞋.女靴",
                "url": "http://list.jd.com/list.html?cat=11729-11731-9776&go=0"
            },
            {
                "category": "g.鞋靴.时尚女鞋.马丁靴",
                "url": "http://list.jd.com/list.html?cat=11729-11731-12060&go=0"
            },
            {
                "category": "g.鞋靴.时尚女鞋.雪地靴",
                "url": "http://list.jd.com/list.html?cat=11729-11731-6920&go=0"
            },
            {
                "category": "g.鞋靴.时尚女鞋.雨鞋/雨靴",
                "url": "http://list.jd.com/list.html?cat=11729-11731-9777&go=0"
            },
            {
                "category": "g.鞋靴.时尚女鞋.鞋配件",
                "url": "http://list.jd.com/list.html?cat=11729-11731-9779&go=0"
            },
            {
                "category": "g.鞋靴.流行男鞋.休闲鞋",
                "url": "http://list.jd.com/list.html?cat=11729-11730-6908&go=0"
            },
            {
                "category": "g.鞋靴.流行男鞋.商务休闲鞋",
                "url": "http://list.jd.com/list.html?cat=11729-11730-6907&go=0"
            },
            {
                "category": "g.鞋靴.流行男鞋.正装鞋",
                "url": "http://list.jd.com/list.html?cat=11729-11730-6906&go=0"
            },
            {
                "category": "g.鞋靴.流行男鞋.帆布鞋",
                "url": "http://list.jd.com/list.html?cat=11729-11730-9783&go=0"
            },
            {
                "category": "g.鞋靴.流行男鞋.工装鞋",
                "url": "http://list.jd.com/list.html?cat=11729-11730-12067&go=0"
            },
            {
                "category": "g.鞋靴.流行男鞋.增高鞋",
                "url": "http://list.jd.com/list.html?cat=11729-11730-12066&go=0"
            },
            {
                "category": "g.鞋靴.流行男鞋.拖鞋/人字拖",
                "url": "http://list.jd.com/list.html?cat=11729-11730-6911&go=0"
            },
            {
                "category": "g.鞋靴.流行男鞋.凉鞋/沙滩鞋",
                "url": "http://list.jd.com/list.html?cat=11729-11730-6909&go=0"
            },
            {
                "category": "g.鞋靴.流行男鞋.雨鞋/雨靴",
                "url": "http://list.jd.com/list.html?cat=11729-11730-9782&go=0"
            },
            {
                "category": "g.鞋靴.流行男鞋.定制鞋",
                "url": "http://list.jd.com/list.html?cat=11729-11730-12068&go=0"
            },
            {
                "category": "g.鞋靴.流行男鞋.男靴",
                "url": "http://list.jd.com/list.html?cat=11729-11730-6912&go=0"
            },
            {
                "category": "g.鞋靴.流行男鞋.传统布鞋",
                "url": "http://list.jd.com/list.html?cat=11729-11730-6910&go=0"
            },
            {
                "category": "g.鞋靴.流行男鞋.功能鞋",
                "url": "http://list.jd.com/list.html?cat=11729-11730-9781&go=0"
            },
            {
                "category": "g.鞋靴.流行男鞋.鞋配件",
                "url": "http://list.jd.com/list.html?cat=11729-11730-6913&go=0"
            },
            {
                "category": "g.鞋靴.潮流女包.单肩包",
                "url": "http://list.jd.com/list.html?cat=1672-2575-5257&go=0"
            },
            {
                "category": "g.鞋靴.潮流女包.手提包",
                "url": "http://list.jd.com/list.html?cat=1672-2575-5259&go=0"
            },
            {
                "category": "g.鞋靴.潮流女包.斜挎包",
                "url": "http://list.jd.com/list.html?cat=1672-2575-5260&go=0"
            },
            {
                "category": "g.鞋靴.潮流女包.双肩包",
                "url": "http://list.jd.com/list.html?cat=1672-2575-5258&go=0"
            },
            {
                "category": "g.鞋靴.潮流女包.钱包",
                "url": "http://list.jd.com/list.html?cat=1672-2575-2580&go=0"
            },
            {
                "category": "g.鞋靴.潮流女包.手拿包",
                "url": "http://list.jd.com/list.html?cat=1672-2575-5256&go=0"
            },
            {
                "category": "g.鞋靴.潮流女包.卡包/零钱包",
                "url": "http://list.jd.com/list.html?cat=1672-2575-12070&go=0"
            },
            {
                "category": "g.鞋靴.潮流女包.钥匙包",
                "url": "http://list.jd.com/list.html?cat=1672-2575-12069&go=0"
            },
            {
                "category": "g.鞋靴.精品男包.商务公文包",
                "url": "http://list.jd.com/list.html?cat=1672-2576-1455&go=0"
            },
            {
                "category": "g.鞋靴.精品男包.单肩/斜挎包",
                "url": "http://list.jd.com/list.html?cat=1672-2576-12072&go=0"
            },
            {
                "category": "g.鞋靴.精品男包.男士手包",
                "url": "http://list.jd.com/list.html?cat=1672-2576-5262&go=0"
            },
            {
                "category": "g.鞋靴.精品男包.双肩包",
                "url": "http://list.jd.com/list.html?cat=1672-2576-12071&go=0"
            },
            {
                "category": "g.鞋靴.精品男包.男士钱包",
                "url": "http://list.jd.com/list.html?cat=1672-2576-2584&go=0"
            },
            {
                "category": "g.鞋靴.精品男包.卡包名片夹",
                "url": "http://list.jd.com/list.html?cat=1672-2576-13542&go=0"
            },
            {
                "category": "g.鞋靴.精品男包.钥匙包",
                "url": "http://list.jd.com/list.html?cat=1672-2576-12073&go=0"
            },
            {
                "category": "g.鞋靴.功能箱包.拉杆箱",
                "url": "http://list.jd.com/list.html?cat=1672-2577-2589&go=0"
            },
            {
                "category": "g.鞋靴.功能箱包.拉杆包",
                "url": "http://list.jd.com/list.html?cat=1672-2577-13543&go=0"
            },
            {
                "category": "g.鞋靴.功能箱包.旅行包",
                "url": "http://list.jd.com/list.html?cat=1672-2577-2588&go=0"
            },
            {
                "category": "g.鞋靴.功能箱包.电脑包",
                "url": "http://list.jd.com/list.html?cat=1672-2577-3997&go=0"
            },
            {
                "category": "g.鞋靴.功能箱包.休闲运动包",
                "url": "http://list.jd.com/list.html?cat=1672-2577-3998&go=0"
            },
            {
                "category": "g.鞋靴.功能箱包.相机包",
                "url": "http://list.jd.com/list.html?cat=1672-2577-12074&go=0"
            },
            {
                "category": "g.鞋靴.功能箱包.腰包/胸包",
                "url": "http://list.jd.com/list.html?cat=1672-2577-12076&go=0"
            },
            {
                "category": "g.鞋靴.功能箱包.登山包",
                "url": "http://list.jd.com/list.html?cat=1672-2577-2587&go=0"
            },
            {
                "category": "g.鞋靴.功能箱包.旅行配件",
                "url": "http://list.jd.com/list.html?cat=1672-2577-4000&go=0"
            },
            {
                "category": "g.鞋靴.功能箱包.书包",
                "url": "http://list.jd.com/list.html?cat=1672-2577-5265&go=0"
            },
            {
                "category": "g.鞋靴.功能箱包.妈咪包",
                "url": "http://list.jd.com/list.html?cat=1672-2577-5271&go=0"
            },
            {
                "category": "g.鞋靴.奢侈品.箱包",
                "url": "http://list.jd.com/list.html?cat=1672-2615-9186&go=0"
            },
            {
                "category": "g.鞋靴.奢侈品.钱包",
                "url": "http://list.jd.com/list.html?cat=1672-2615-9187&go=0"
            },
            {
                "category": "g.鞋靴.奢侈品.服饰",
                "url": "http://list.jd.com/list.html?cat=1672-2615-9188&go=0"
            },
            {
                "category": "g.鞋靴.奢侈品.腰带",
                "url": "http://list.jd.com/list.html?cat=1672-2615-9189&go=0"
            },
            {
                "category": "g.鞋靴.奢侈品.鞋靴",
                "url": "http://list.jd.com/list.html?cat=1672-2615-11934&go=0"
            },
            {
                "category": "g.鞋靴.奢侈品.太阳镜/眼镜框",
                "url": "http://list.jd.com/list.html?cat=1672-2615-9190&go=0"
            },
            {
                "category": "g.鞋靴.奢侈品.饰品",
                "url": "http://list.jd.com/list.html?cat=1672-2615-11935&go=0"
            },
            {
                "category": "g.鞋靴.奢侈品.配件",
                "url": "http://list.jd.com/list.html?cat=1672-2615-9191&go=0"
            },
            {
                "category": "g.鞋靴.礼品.火机烟具",
                "url": "http://list.jd.com/list.html?cat=1672-2599-1440&go=0"
            },
            {
                "category": "g.鞋靴.礼品.军刀军具",
                "url": "http://list.jd.com/list.html?cat=1672-2599-1443&go=0"
            },
            {
                "category": "g.鞋靴.礼品.美妆礼品",
                "url": "http://list.jd.com/list.html?cat=1672-2599-12078&go=0"
            },
            {
                "category": "g.鞋靴.礼品.工艺礼品",
                "url": "http://list.jd.com/list.html?cat=1672-2599-1445&go=0"
            },
            {
                "category": "g.鞋靴.礼品.礼盒礼券",
                "url": "http://list.jd.com/list.html?cat=1672-2599-1446&go=0"
            },
            {
                "category": "g.鞋靴.礼品.礼品文具",
                "url": "http://list.jd.com/list.html?cat=1672-2599-1442&go=0"
            },
            {
                "category": "g.鞋靴.礼品.收藏品",
                "url": "http://list.jd.com/list.html?cat=1672-2599-1444&go=0"
            },
            {
                "category": "g.鞋靴.礼品.古董把玩",
                "url": "http://list.jd.com/list.html?cat=1672-2599-12080&go=0"
            },
            {
                "category": "g.鞋靴.礼品.礼品定制",
                "url": "http://list.jd.com/list.html?cat=1672-2599-12079&go=0"
            },
            {
                "category": "g.鞋靴.礼品.创意礼品",
                "url": "http://list.jd.com/list.html?cat=1672-2599-5266&go=0"
            },
            {
                "category": "g.鞋靴.礼品.婚庆用品",
                "url": "http://list.jd.com/list.html?cat=1672-2599-4942&go=0"
            },
            {
                "category": "g.鞋靴.礼品.鲜花绿植",
                "url": "http://list.jd.com/list.html?cat=1672-2599-4698&go=0"
            },
            {
                "category": "g.鞋靴.礼品.京东卡",
                "url": "http://list.jd.com/list.html?cat=1672-2599-6980&go=0"
            },
            {
                "category": "g.鞋靴.珠宝首饰.K金",
                "url": "http://list.jd.com/list.html?cat=6144-13062&go=0"
            },
            {
                "category": "g.鞋靴.珠宝首饰.时尚饰品",
                "url": "http://list.jd.com/list.html?cat=6144-6182&go=0"
            },
            {
                "category": "g.鞋靴.珠宝首饰.钻石",
                "url": "http://list.jd.com/list.html?cat=6144-6160&go=0"
            },
            {
                "category": "g.鞋靴.珠宝首饰.翡翠玉石",
                "url": "http://list.jd.com/list.html?cat=6144-6167&go=0"
            },
            {
                "category": "g.鞋靴.珠宝首饰.银饰",
                "url": "http://list.jd.com/list.html?cat=6144-6155&go=0"
            },
            {
                "category": "g.鞋靴.珠宝首饰.水晶玛瑙",
                "url": "http://list.jd.com/list.html?cat=6144-6172&go=0"
            },
            {
                "category": "g.鞋靴.珠宝首饰.彩宝",
                "url": "http://list.jd.com/list.html?cat=6144-6174&go=0"
            },
            {
                "category": "g.鞋靴.珠宝首饰.铂金",
                "url": "http://list.jd.com/list.html?cat=6144-12040&go=0"
            },
            {
                "category": "g.鞋靴.珠宝首饰.天然木饰",
                "url": "http://list.jd.com/list.html?cat=6144-12041&go=0"
            },
            {
                "category": "g.鞋靴.珠宝首饰.珍珠",
                "url": "http://list.jd.com/list.html?cat=6144-12042&go=0"
            },
            {
                "category": "g.鞋靴.金银投资.投资金",
                "url": "http://list.jd.com/list.html?cat=6144-6146-6151&go=0"
            },
            {
                "category": "g.鞋靴.金银投资.投资银",
                "url": "http://list.jd.com/list.html?cat=6144-6146-6152&go=0"
            },
            {
                "category": "g.鞋靴.金银投资.投资收藏",
                "url": "http://list.jd.com/list.html?cat=6144-6146-13531&go=0"
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
