# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

from setuptools import setup, find_packages

setup(name='scrapy-proxy_spider',
      entry_points={
          'scrapy.commands': [
              'mc_crawl_all=proxy_spider.commands:mc_crawl_all',
              'mc_clean_dirty_data=proxy_spider.commands:mc_clean_dirty_data',
          ],
      },
      )
