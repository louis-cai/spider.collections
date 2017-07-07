# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

import json, re
import codecs


# import sys
# reload(sys)
# sys.setdefaultencoding('utf8')


def read_json_file(file):
    return json.load(codecs.open(file, 'r', 'utf-8'))


def write_json_file(file, json_obj):
    json.dump(json_obj, codecs.open(file, 'w', 'utf-8'), ensure_ascii=False)
