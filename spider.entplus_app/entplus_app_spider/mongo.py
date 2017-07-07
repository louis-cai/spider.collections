# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

import pymongo

MONGO_URI = "localhost:27017"
MONGO_DB = "entplus_app"

mongo_client = pymongo.MongoClient(MONGO_URI)
db = mongo_client[MONGO_DB]


class Company(object):
    def __init__(self):
        pass

    @staticmethod
    def upsert(item):
        db.company.update(
            {'fei_entname': item.get('fei_entname')},
            {'$set': item}, True, True
        )
