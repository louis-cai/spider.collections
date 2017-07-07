# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

from mongo import ChinabiddingDB
from mredis import RedisClient

if __name__ == "__main__":
    cur = ChinabiddingDB.get_all()
    for item in cur:
        RedisClient.set_result_url_key(item['detail_url'])
