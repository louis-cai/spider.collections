# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

import pymongo
import logging

from config import skip_num

# MONGO
MONGO_URI = "localhost:27017"
mongo_client = pymongo.MongoClient(MONGO_URI)

bjsat_db = mongo_client["bjsat_gov_cn"]
proxy_db = mongo_client['proxy']
qianzhan_db = mongo_client["qianzhan"]


class BjsatDB(object):
    def __init__(self):
        pass

    @staticmethod
    def upsert_result(item):
        logging.info("<MONGO> %s" % item)
        bjsat_db.company_info.update({'number': item['number']}, {'$set': item}, True, True)


class ProxyDB(object):
    def __init__(self):
        pass

    @staticmethod
    def get_all():
        return proxy_db.proxy_items_bjsat.find().batch_size(1)

    @staticmethod
    def remove_proxy(proxy_ip, proxy_port):
        proxy_db.proxy_items_bjsat.remove({"ip": proxy_ip, "port": proxy_port})


class QianzhanDB(object):
    def __init__(self):
        pass

    @staticmethod
    def get_all_count():
        return qianzhan_db.company_info_items_base.find().count()

    @staticmethod
    def get_one(i):
        return qianzhan_db.company_info_items_base.find()[i]

    @staticmethod
    def get_all():
        return qianzhan_db.company_info_items_base.find().batch_size(1)

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
