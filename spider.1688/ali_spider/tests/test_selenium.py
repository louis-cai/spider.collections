# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

from selenium import webdriver

driver = webdriver.PhantomJS(
    desired_capabilities={
        'javascriptEnabled': True,
        'platform': 'windows',
        'browserName': 'Mozilla',
        'version': '5.0',
        'phantomjs.page.settings.userAgent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.57 Safari/537.36"
    })
driver.get(
    "http://s.1688.com/selloffer/offer_search.htm?earseDirect=false&sign2=20&keywords=%B7%FE%D7%B0%B0%FC%D7%B0%B4%FC+%CB%DC%C1%CF&from=marketSearch&n=y&filt=y")
print driver.page_source
# content = driver.page_source.encode('utf-8')
# print content
# url = driver.current_url.encode('utf-8')
driver.quit()
