# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

import pymongo
import logging
import time

# MONGO
MONGO_URI = "localhost:27017"
mongo_client = pymongo.MongoClient(MONGO_URI)
qianzhan_db = mongo_client["qianzhan"]
bjsat_gov_cn_db = mongo_client["bjsat_gov_cn"]


class BjsatDB(object):
    def __init__(self):
        pass

    @staticmethod
    def get_all():
        return bjsat_gov_cn_db.company_info.find().batch_size(50)


class QianzhanDB(object):
    def __init__(self):
        pass

    @staticmethod
    def company_detail(company_name):
        return qianzhan_db.company_info_items_base.find_one({"company_name": company_name})

    @staticmethod
    def upsert_company_export(item):
        logging.info("<MONGO> %s" % item)
        qianzhan_db.export_from_bjsat.update({'company_name': item['company_name']}, {'$set': item}, True, True)


import sys

reload(sys)
sys.setdefaultencoding("utf-8")
print "sys default encoding: ", sys.getdefaultencoding()

format_str = '%(asctime)s %(filename)s[line:%(lineno)d] <%(levelname)s> %(message)s'

logging.basicConfig(
    level=logging.DEBUG,
    format=format_str,
    datefmt='%Y-%m-%d %H:%M:%S',
    filename="log/bjsat.log",
    filemode='w'
)


if __name__ == "__main__":
    cur = BjsatDB.get_all()
    i = 0
    for item in cur:
        i += 1
        company_name = item['company_name']
        logging.info(i)
        company = QianzhanDB.company_detail(company_name)
        if company:
            QianzhanDB.upsert_company_export(company)
