# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

from spider import Spider
from log import init_logging

import sys

reload(sys)
sys.setdefaultencoding("utf-8")
print "sys default encoding: ", sys.getdefaultencoding()


def main():
    init_logging()
    spider = Spider()
    spider.run()
    pass


if __name__ == "__main__":
    main()
    pass
