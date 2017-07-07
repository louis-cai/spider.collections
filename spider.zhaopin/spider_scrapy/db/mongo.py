# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

import pymongo
import logging

# MONGO
MONGO_URI = "localhost:27017"

mongo_client = pymongo.MongoClient(MONGO_URI)
zhaopin_db = mongo_client["zhaopin"]

proxy_db = mongo_client['proxy']
qianzhan_db = mongo_client["qianzhan"]


class QianzhanDB(object):
    def __init__(self):
        pass

    @staticmethod
    def upsert_company(item):
        logging.info("<MONGO> %s" % item)
        qianzhan_db.company_info_items_base.update({'company_name': item['company_name']}, {'$set': item}, True, True)

    @staticmethod
    def is_had(company_name):
        cur = qianzhan_db.company_info_items_base.find_one({"company_name": company_name})
        # logging.debug("cur:%s" % cur)
        if cur:
            return True
        else:
            return False

    @staticmethod
    def get_companys():
        return qianzhan_db.company_info_items_base.find().batch_size(50)


class ZhaopinDB(object):
    def __init__(self):
        pass

    @staticmethod
    def upsert_company(item):
        logging.info("<MONGO> %s" % item)
        zhaopin_db.company_info_items.update({'company_name': item['company_name']}, {'$set': item}, True, True)

    @staticmethod
    def upsert_company_gaoxin(item):
        logging.info("<MONGO> %s" % item)
        zhaopin_db.company_info_items_gaoxin.update({'company_name': item['company_name']}, {'$set': item}, True, True)


class ProxyDB(object):
    def __init__(self):
        pass

    @staticmethod
    def get_items():
        return proxy_db.proxy_items.find().batch_size(50)
