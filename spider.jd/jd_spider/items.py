# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JdSpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class ShellerInfoItem(scrapy.Item):
    category = scrapy.Field()
    sheller_name = scrapy.Field()   # 店铺名称
    shop_name = scrapy.Field()  # 公司名称
    shop_address = scrapy.Field()
    sheller_phone = scrapy.Field()
    sheller_url = scrapy.Field()
    insert_time = scrapy.Field()
    pass


