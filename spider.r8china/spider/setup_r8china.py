# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

import logging
import time

from log import init_logging
from spider import Spider


def init_encoding():
    import sys
    reload(sys)
    sys.setdefaultencoding("utf-8")
    print "sys default encoding: ", sys.getdefaultencoding()


def main():
    init_encoding()
    init_logging("log/debug.log", "log/log.log")
    spider = Spider()
    begin_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    spider.run()
    end_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    logging.info("-------begin: %s, end: %s--------" % (begin_time, end_time))
    pass


if __name__ == "__main__":
    main()
