# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

from log import init_logging
# from spider_level_1 import Spider
from spider_level_2 import Spider

# from spider_level_3 import Spider

if __name__ == "__main__":
    init_logging()
    s = Spider()
    s.test("DCBB0FD56D324C87AD672F5D35EA3437")
    pass
