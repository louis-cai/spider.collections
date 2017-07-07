# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

import pymongo
import logging

# MONGO
MONGO_URI = "localhost:27017"
MONGO_DB = "qianzhan"
# MONGO_NEEQ_DB = "neeq"
# qichacha_db = "qichacha"

mongo_client = pymongo.MongoClient(MONGO_URI)
db = mongo_client[MONGO_DB]
qichacha_db = mongo_client['qichacha']

from log import init_logging

init_logging('log/merge.log', 'log/merge_2.log')

cur = qichacha_db.company_info_items.find({}, {"_id": 0}).batch_size(50)
i = 0
for item in cur:
    i += 1
    logging.info(i)
    db.company_info_items_base.update({'company_name': item['company_name']}, {'$set': item}, True, True)
