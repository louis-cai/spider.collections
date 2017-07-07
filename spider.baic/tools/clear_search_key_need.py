# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

import logging

import pymongo

from log import init_logging

# MONGO
# MONGO_URI = "localhost:27017"
mongo_client = pymongo.MongoClient()

qyxy_baic_db = mongo_client["qyxy_baic"]

import sys

reload(sys)
sys.setdefaultencoding("utf-8")
print "sys default encoding: ", sys.getdefaultencoding()

if __name__ == "__main__":
    init_logging('1.log', '2.log')

    cur = qyxy_baic_db.search_key_have.find()

    l = list(cur)

    for i in l:
        search_key = i[u'search_key']
        logging.info(search_key)
        qyxy_baic_db.search_key_need.remove({"search_key": search_key})
