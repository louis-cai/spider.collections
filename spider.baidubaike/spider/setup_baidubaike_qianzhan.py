# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

from spider import Spider
from log import init_logging
import time
import logging

import sys

reload(sys)
sys.setdefaultencoding("utf-8")
print "sys default encoding: ", sys.getdefaultencoding()


def main():
    init_logging("log/qianzhan.log", "log/qianzhan_2.log")
    spider = Spider()
    begin_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    try:
        spider.run()
    except Exception, e:
        logging.exception(e)
    end_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    logging.info("-------begin: %s, end: %s--------" % (begin_time, end_time))
    pass


if __name__ == "__main__":
    main()
    pass
