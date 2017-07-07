# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

import pymongo
import logging
import time
from log import init_logging

# MONGO
MONGO_URI = "localhost:27017"
mongo_client = pymongo.MongoClient(MONGO_URI)
qianzhan_db = mongo_client["qianzhan"]
zhaopin_db = mongo_client["zhaopin"]


class ZhaopinDB(object):
    def __init__(self):
        pass

    @staticmethod
    def get_all():
        return zhaopin_db.company_info_items.find().batch_size(50)


class QianzhanDB(object):
    def __init__(self):
        pass

    @staticmethod
    def company_detail(company_name):
        return qianzhan_db.company_info_items_detail.find_one({"company_name": company_name}, {"_id": 0})

    @staticmethod
    def company_base(company_name):
        return qianzhan_db.company_info_items_base.find_one({"company_name": company_name}, {"_id": 0})

    @staticmethod
    def upsert_company_export(item):
        logging.info("<MONGO> %s" % item)
        qianzhan_db.export_from_zhaopin.update({'company_name': item['company_name']}, {'$set': item}, True, True)


import sys
reload(sys)
sys.setdefaultencoding("utf-8")
print "sys default encoding: ", sys.getdefaultencoding()

if __name__ == "__main__":
    init_logging('log/export_from_zhaopin.log', 'log/export_from_zhaopin_2.log')

    cur = ZhaopinDB.get_all()
    i = 0
    for item in cur:
        i += 1
        company_name = item['company_name']
        logging.info(i)
        company = QianzhanDB.company_detail(company_name)
        if company:
            QianzhanDB.upsert_company_export(company)
        company = QianzhanDB.company_base(company_name)
        if company:
            QianzhanDB.upsert_company_export(company)
