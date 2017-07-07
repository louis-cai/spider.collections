# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

import pymongo
import logging
import random

# MONGO
# MONGO_URI = "localhost:27017"
# mongo_client = pymongo.MongoClient(MONGO_URI)
mongo_client = pymongo.MongoClient()
zhaopin_db = mongo_client["zhaopin"]




class ZhaopinDB(object):
    def __init__(self):
        pass

    @staticmethod
    def upsert_company(item):
        logging.info("<MONGO> %s" % item)
        zhaopin_db.company_info.update({'company_id': item['company_id']}, {'$set': item}, True, True)


    @staticmethod
    def check_have(company_id):
        if zhaopin_db.company_info.find_one({"company_id": company_id}):
            return True
        else:
            return False

    @staticmethod
    def get_one_random_company_id():
        cur = zhaopin_db.company_info.find()
        count = cur.count()
        r = random.randint(count)
        company = cur[r]
        return company['company_id']

    @staticmethod
    def get_one_company_id(index):
        cur = zhaopin_db.company_info.find().skip(index).limit(1)
        return cur[1]

    @staticmethod
    def check_have_job(url):
        if zhaopin_db.job_info.find_one({"url": url}):
            return True
        else:
            return False

    @staticmethod
    def set_company_id_have_crawl_job(company_id):
        zhaopin_db.company_id_crawl_job.insert({'company_id': company_id})

    @staticmethod
    def find_company_id_have_crawl_job(company_id):
        return zhaopin_db.company_id_crawl_job.find_one({'company_id': company_id})

    @staticmethod
    def upsert_job(item):
        logging.info("<MONGO> %s" % item)
        zhaopin_db.job_info.update({'url': item['url']}, {'$set': item}, True, True)
