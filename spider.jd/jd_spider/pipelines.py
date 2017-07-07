# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exceptions import DropItem
from jd_spider.db.mongo import ShellerInfoItemsDB


class ValidParamsPipeline(object):
    def process_item(self, item, spider):
        if item.get("shop_name"):
            return item
        raise DropItem("shop name is null")


class DuplicatesPipeline(object):
    def __init__(self):
        self.ips_seen = set()

    def process_item(self, item, spider):
        if item['shop_name'] in self.ips_seen and not item.get('sheller_phone'):
            raise DropItem("Duplicate item found: %s" % item['shop_name'])
        else:
            self.ips_seen.add(item['shop_name'])
            return item


class MongoPipeline(object):
    def process_item(self, item, spider):
        ShellerInfoItemsDB.upsert_sheller_info_item(dict(item))
        return item
