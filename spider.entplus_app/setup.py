# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

import sys

from entplus_app_spider import Spider

if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding("utf8")
    print "sys default encoding: ", sys.getdefaultencoding()

    spider = Spider()
    spider.start()
