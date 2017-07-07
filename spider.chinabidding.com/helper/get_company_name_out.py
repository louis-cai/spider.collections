# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

from mongo import ChinabiddingDB

if __name__ == "__main__":
    cur = ChinabiddingDB.get_all()
    for item in cur:
        company_name_list = item['company_name_list']
        detail = item['detail']

        line_list = detail.split('\n')
        for line in line_list:
            text = line.replace(u'：', u':')

            if text.find(u'采购单位名称:') > -1:
                company_name = text[text.find(u'采购单位名称：') + len(u'采购单位名称:'):]
                if company_name not in company_name_list:
                    company_name_list.append(company_name)
            if text.find(u'采购代理机构全称:') > -1:
                company_name = text[text.find(u'采购代理机构全称:') + len(u'采购代理机构全称:'):]
                if company_name not in company_name_list:
                    company_name_list.append(company_name)
            if text.find(u'成交供应商名称:') > -1:
                company_name = text[text.find(u'成交供应商名称:') + len(u'成交供应商名称:'):]
                if company_name not in company_name_list:
                    company_name_list.append(company_name)
            if text.find(u'中标供应商:') > -1:
                company_name = text[text.find(u'中标供应商:') + len(u'中标供应商:'):]
                if company_name not in company_name_list:
                    company_name_list.append(company_name)
            if text.find(u'中标人:') > -1:
                company_name = text[text.find(u'中标人:') + len(u'中标人:'):]
                if company_name not in company_name_list:
                    company_name_list.append(company_name)
            if text.find(u'推荐中标商:') > -1:
                company_name = text[text.find(u'推荐中标商:') + len(u'推荐中标商:'):]
                if company_name not in company_name_list:
                    company_name_list.append(company_name)
            if text.find(u'招标机构:') > -1:
                company_name = text[text.find(u'招标机构:') + len(u'招标机构:'):]
                if company_name not in company_name_list:
                    company_name_list.append(company_name)
            if text.find(u'招标代理机构:') > -1:
                company_name = text[text.find(u'招标代理机构:') + len(u'招标代理机构:'):]
                if company_name not in company_name_list:
                    company_name_list.append(company_name)
            if text.find(u'招标人:') > -1:
                company_name = text[text.find(u'招标人:') + len(u'招标人:'):]
                if company_name not in company_name_list:
                    company_name_list.append(company_name)
            if text.find(u'招标人名称:') > -1:
                company_name = text[text.find(u'招标人名称:') + len(u'招标人名称:'):]
                if company_name not in company_name_list:
                    company_name_list.append(company_name)
            if text.endswith(u'公司') and text.find(u':') < 0:
                company_name = text
                if company_name not in company_name_list:
                    company_name_list.append(company_name)
            if text.endswith(u'公司') and text.startswith(u'北京') < 0:
                company_name = text
                if company_name not in company_name_list:
                    company_name_list.append(company_name)
            if text.find(u'公司') > -1:
                company_name = text[text.find(u'公司') - 8: text.find(u'公司')]
                if company_name not in company_name_list:
                    company_name_list.append(company_name)
            if text.find(u'公司') > -1:
                company_name = text[text.find(u'公司') - 10: text.find(u'公司')]
                if company_name not in company_name_list:
                    company_name_list.append(company_name)

        for company_name in company_name_list:
            ChinabiddingDB.upsert_company_name(company_name)
