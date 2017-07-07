# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

import logging

import pymongo

from log import init_logging

# MONGO
# MONGO_URI = "localhost:27017"
# mongo_client = pymongo.MongoClient(MONGO_URI)
mongo_client = pymongo.MongoClient()

qyxy_baic_db = mongo_client["qyxy_baic"]
other_from_excel_db = mongo_client["other_from_excel"]

import sys

reload(sys)
sys.setdefaultencoding("utf-8")
print "sys default encoding: ", sys.getdefaultencoding()



if __name__ == "__main__":
    init_logging('1.log', '2.log')

    company_list = []

    cur = other_from_excel_db.beijinggaoxin.find()

    for item in cur:
        search_key = item[u'company_name']
        # logging.debug(search_key)
        if qyxy_baic_db.search_key_need.find_one({"search_key": search_key}):
            # logging.debug("pass............")
            print "pass.."
            pass
        elif qyxy_baic_db.search_key_have.find_one({"search_key": search_key}):
            # logging.debug("pass............")
            print "pass.."
            pass
        else:
            company_list.append(search_key)

    company_set = set(company_list)

    company_list = []
    for c in company_set:
        company = {"search_key": c}
        company_list.append(company)

    logging.info(len(company_list))
    qyxy_baic_db.search_key_need.insert(company_list)
