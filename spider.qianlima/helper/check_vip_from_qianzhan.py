# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

import pymongo
import logging
import threadpool

# MONGO
MONGO_URI = "localhost:27017"
mongo_client = pymongo.MongoClient(MONGO_URI)

qianlima_db = mongo_client["qianlima_vip"]
qianzhan_db = mongo_client["qianzhan"]

import redis
import os

REDIS_HOST = os.getenv("REDIS_HOST", '127.0.0.1')
REDIS_PORT = os.getenv("REDIS_PORT", 6379)

redis_client = redis.StrictRedis(REDIS_HOST, REDIS_PORT, db=0)


# i = 0

def do_search(item):
    # i += 1
    company_name = item['company_name']
    redis_client.hset("check_vip.company_name", company_name, True)
    company = qianzhan_db.company_info_items_base.find_one({"company_name": company_name})
    if company:
        # logging.info("----------%d" % i)
        company = dict(company)
        company.update(item)
        company.update({'from_qianlima_vip': 1})
        qianzhan_db.export_from_qianlima.update({'company_name': company['company_name']},
                                                {'$set': company}, True,
                                                True)
        if company.get('register_date') and company.get('register_date') <= "2014-09-12":
            # logging.info("---------------%d" % i)
            qianzhan_db.export_from_qianlima_more_two_years.update({'company_name': company['company_name']},
                                                                   {'$set': company}, True,
                                                                   True)


if __name__ == "__main__":
    from log import init_logging

    init_logging('log/check_vip.log.log', 'log/check_vip.log')
    cur = qianlima_db.company_info.find().batch_size(50)

    pool = threadpool.ThreadPool(20)
    reqs = threadpool.makeRequests(do_search, cur)
    [pool.putRequest(req) for req in reqs]
    pool.wait()
