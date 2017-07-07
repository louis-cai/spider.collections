# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

import requests

proxies = {"http": "http://175.153.21.241:5839"}

response = requests.get("http://www.baidu.com", proxies=proxies)

print response.content
