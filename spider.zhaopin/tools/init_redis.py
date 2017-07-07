# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

import pymongo
import logging

# MONGO
MONGO_URI = "localhost:27017"

mongo_client = pymongo.MongoClient(MONGO_URI)
zhaopin_db = mongo_client["zhaopin"]

import redis
import os

REDIS_HOST = os.getenv("REDIS_HOST", '127.0.0.1')
REDIS_PORT = os.getenv("REDIS_PORT", 6379)

redis_client = redis.StrictRedis(REDIS_HOST, REDIS_PORT, db=0)


class ZhaopinDB(object):
    def __init__(self):
        pass

    @staticmethod
    def get_companys():
        return zhaopin_db.company_info_items_searched.find().batch_size(50)


class RedisClient(object):
    def __init__(self):
        pass

    @staticmethod
    def set_search_key_key(key):
        redis_client.hset("zhaopin.search_key", key, True)

    @staticmethod
    def get_search_key_key(key):
        return redis_client.hexists("zhaopin.search_key", key)


import sys

reload(sys)
sys.setdefaultencoding("utf-8")
print "sys default encoding: ", sys.getdefaultencoding()



if __name__ == "__main__":
    cur = ZhaopinDB.get_companys()
    for item in cur:
        # print item['company_name']
        RedisClient.set_search_key_key(item['company_name'])
    pass
