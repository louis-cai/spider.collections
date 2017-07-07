# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

from site_client import SiteClient

site_client = SiteClient()
site_client.index_1()

response = site_client.get_verify_img()
