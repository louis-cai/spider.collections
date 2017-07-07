# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

import requests

import pymongo
import time
import logging

import sys

reload(sys)
sys.setdefaultencoding("utf-8")
print "sys default encoding: ", sys.getdefaultencoding()

# MONGO
MONGO_URI = "localhost:27017"
MONGO_PROXY_DB = "proxy"

mongo_client = pymongo.MongoClient(MONGO_URI)
proxy_db = mongo_client[MONGO_PROXY_DB]

#### 变量
log_file = "log/check_proxy_to_qianlima_2.log"
test_url = "http://center.qianlima.com/login.jsp"
test_txt = "qianlima"
test_to_collection = "proxy_items_qianlima_2"
test_to_collection_2 = "proxy_items_qianlima_3"
test_timeout = 1

if __name__ == "__main__":

    session = requests.Session()

    session.headers.update({
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, sdch',
        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.6',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        # 'Cookie': 'qznewsite.uid=rssbv51ml0mwomw4k4mkycz2; qz.newsite=41A3A9C8ADE5F5073B86647E6C185D2272112F0E96AD14B275E442ED8A2B85688F50512A00FAD14DB2D485EF57054E35ECB028B44D155EE32D029A4352C6617B74BE83EB551C4D66024D7F4913B053785964ED37F3061D43BA0E8663791A1E143AC458E738C7484453887CEAB6EDEC359632DDDEAF6D585D0BD31087077296B6D97CF68F',
        # 'Host': 'www.qianlima.com',
        'Pragma': 'no-cache',
        # 'Referer': 'http://qiye.qianzhan.com/',
        'Upgrade-Insecure-Requests': 1,
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
    })

    format_str = '%(asctime)s %(filename)s[line:%(lineno)d] <%(levelname)s> %(message)s'

    logging.basicConfig(
        level=logging.DEBUG,
        format=format_str,
        datefmt='%Y-%m-%d %H:%M:%S',
        filename=log_file,
        filemode='w'
    )

    # cur = proxy_db.proxy_items_all.find({}, {'_id': 0}).batch_size(50).skip(4000)
    # i = 0
    # for item in cur:
    #     logging.info("i+++++++++++++++++++:%s" % i)
    #     i += 1
    #     # time.sleep(1)
    #     logging.info("%s:%s" % (item['ip'], item['port']))
    #     proxies = {"http": "http://%s:%s" % (item['ip'], item['port'])}
    #     try:
    #         response = session.get(test_url, proxies=proxies, timeout=test_timeout, allow_redirects=False)
    #         logging.info("<response %d>" % response.status_code)
    #         if response.status_code == 200 and response.text.find(test_txt) > 0:
    #             proxy_db[test_to_collection].update({"ip": item['ip'], "port": item['port']}, item, True, True)
    #         else:
    #             # proxy_db.proxy_items_other.update({"ip": item['ip'], "port": item['port']}, item, True, True)
    #             pass
    #     except Exception, e:
    #         logging.exception(e)
    #         # proxy_db.proxy_items_other.update({"ip": item['ip'], "port": item['port']}, item, True, True)
    #         # proxy_db.proxy_items_qianzhan_5.remove({"ip": item['ip'], "port": item['port']})
    #         # proxy_db.proxy_items_all.update({"ip": item['ip'], "port": item['port']}, item, True, True)

    cur = proxy_db[test_to_collection].find({}, {'_id': 0}).batch_size(50)
    i = 0
    for item in cur:
        logging.info("i+++++++++++++++++++:%s" % i)
        i += 1
        # time.sleep(1)
        logging.info("%s:%s" % (item['ip'], item['port']))
        proxies = {"http": "http://%s:%s" % (item['ip'], item['port'])}
        try:
            response = session.get(test_url, proxies=proxies, timeout=test_timeout, allow_redirects=False)
            logging.info("<response %d>" % response.status_code)
            if response.status_code == 200 and response.text.find(test_txt) > 0:
                proxy_db[test_to_collection_2].update({"ip": item['ip'], "port": item['port']}, item, True, True)
            else:
                # proxy_db.proxy_items_other.update({"ip": item['ip'], "port": item['port']}, item, True, True)
                pass
        except Exception, e:
            logging.exception(e)
            # proxy_db.proxy_items_other.update({"ip": item['ip'], "port": item['port']}, item, True, True)
            # proxy_db.proxy_items_qianzhan_5.remove({"ip": item['ip'], "port": item['port']})
            # proxy_db.proxy_items_all.update({"ip": item['ip'], "port": item['port']}, item, True, True)

    logging.info("success finish!!-------")
