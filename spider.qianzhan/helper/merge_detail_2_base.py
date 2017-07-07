# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

import pymongo
import logging

mongo_client = pymongo.MongoClient("localhost:27017")
db = mongo_client["qianzhan"]


from log import init_logging

init_logging('log/merge_detail.log', 'log/merge_detail_2.log')

cur = db.company_info_items_detail.find({}, {"_id": 0}).batch_size(50)
i = 0
for item in cur:
    i += 1
    logging.info(i)
    db.company_info_items_base.update({'company_name': item['company_name']}, {'$set': item}, True, True)
