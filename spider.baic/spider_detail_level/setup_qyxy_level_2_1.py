# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

import logging
import sys
import time

from log import init_logging
from spider_level_2 import Spider

reload(sys)
sys.setdefaultencoding("utf-8")
print "sys default encoding: ", sys.getdefaultencoding()


def main():
    init_logging("log/level_2_1.log", "log/level_2_1_log.log")
    spider = Spider(1)
    begin_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    spider.run()
    end_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    logging.info("-------begin: %s, end: %s--------" % (begin_time, end_time))
    pass


if __name__ == "__main__":
    main()
    pass
