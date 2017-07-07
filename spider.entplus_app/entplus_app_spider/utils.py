# -*- coding:utf-8 -*-
__author__ = 'zhaojm'
import codecs


def get_gb2312_txt():
    f = codecs.open('data/gb2312.txt', 'r', 'utf-8')
    return f.read()
