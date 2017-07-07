# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

import requests
import logging
from log import init_logging
from mongo import ProxyItemsDB, AlivebaicDB
import time
import random
from config import host, domain

default_header = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, sdch, br',
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.6',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    # 'Cookie': 'qznewsite.uid=rssbv51ml0mwomw4k4mkycz2; qz.newsite=41A3A9C8ADE5F5073B86647E6C185D2272112F0E96AD14B275E442ED8A2B85688F50512A00FAD14DB2D485EF57054E35ECB028B44D155EE32D029A4352C6617B74BE83EB551C4D66024D7F4913B053785964ED37F3061D43BA0E8663791A1E143AC458E738C7484453887CEAB6EDEC359632DDDEAF6D585D0BD31087077296B6D97CF68F',
    'Host': host,
    'Pragma': 'no-cache',
    # 'Referer': 'http://qiye.qianzhan.com/',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36'
}

valid_url = domain
valid_txt = u"北京市企业信用信息网"
valid_timeout = 3


def valid_proxy(item):
    try:
        proxies = {"http": "%s:%s" % (item["ip"], item["port"])}
        logging.info(proxies)
        response = requests.get(valid_url, proxies=proxies, allow_redirects=False, timeout=valid_timeout,
                                headers=default_header)
        if response.status_code != 200:
            raise Exception("status code error")
        if response.content.find(valid_txt) < 0:
            raise Exception("not found valid txt")
        logging.info("-----------------valid good---------------------")
        return True
    except Exception, e:
        logging.info("-----------------valid bad---------------------%s" % e.message)
        return False
        # logging.info(item)
        # return True


def main():
    cur = ProxyItemsDB.get_proxy_items()
    for item in cur:
        if valid_proxy(item):
            AlivebaicDB.upsert_proxy_item(item)
            time.sleep(2 * random.random())


def init_defaultencoding():
    import sys
    reload(sys)
    sys.setdefaultencoding("utf-8")
    print "sys default encoding: ", sys.getdefaultencoding()


if __name__ == "__main__":
    init_defaultencoding()
    init_logging("log/check_proxy_to_baic.log", "log/check_proxy_to_baic_2.log")
    logging.info("main begin!!-------")
    main()
    logging.info("success finish!!-------")
    pass
