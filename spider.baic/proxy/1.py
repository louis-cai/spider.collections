# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

import hashlib
import sys
import time

reload(sys)
sys.setdefaultencoding("utf-8")
print "sys default encoding: ", sys.getdefaultencoding()


def get_authHeader():
    # 请替换appkey和secret
    appkey = "17644285"
    secret = "54d9b18269c54a19a841cc25f4633cac"

    paramMap = {
        "app_key": appkey,
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),  # 如果你的程序在国外，请进行时区处理
        "with-transaction": "1"
    }
    # 排序
    keys = paramMap.keys()
    keys.sort()

    codes = "%s%s%s" % (secret, str().join('%s%s' % (key, paramMap[key]) for key in keys), secret)

    # 计算签名
    sign = hashlib.md5(codes).hexdigest().upper()

    paramMap["sign"] = sign


    # 拼装请求头Proxy-Authorization的值
    keys = paramMap.keys()
    authHeader = "MYH-AUTH-MD5 " + str('&').join('%s=%s' % (key, paramMap[key]) for key in keys)

    print "authHeader", authHeader
    return authHeader


# 接下来使用蚂蚁动态代理进行访问

# proxy_handler = urllib2.ProxyHandler({"http" : 'http://test.proxy.mayidaili.com:8123'})
# opener = urllib2.build_opener(proxy_handler)

# request = urllib2.Request('http://1212.ip138.com/ic.asp')
import requests

session = requests.Session()

proxies = {"http": "http://123.57.155.168:8123"}

# //将authHeader放入请求头中即可,注意authHeader必须在每次请求时都重新计算，要不然会因为时间误差而认证失败  
# request.add_header('Proxy-Authorization', authHeader)

# response = opener.open(request)

url = "http://test.zhironghao.com/api/p/user/login"
url = "http://123.206.84.74:8080/api/loanApplication/list?wd=mz"
url = "http://123.206.6.251:8888/test_ip"

payload = {'account': 'mingzi', 'password': 'mingzi', 'signature': '11111', 'timestamp': '11111'}

num = 10

while num > 0:
    print time.strftime("%Y-%m-%d %H:%M:%S")
    authHeader = get_authHeader()
    headers = {'Proxy-Authorization': authHeader}
    print headers
    # response = requests.post(url, proxies=proxies, headers=headers, data=payload)
    response = session.get(url, proxies=proxies, headers=headers)
    print response.content
    print response.headers
    num -= 1
