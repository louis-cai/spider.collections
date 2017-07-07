# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

import codecs
import json

f_1 = codecs.open('1.json', encoding='utf-8', mode='r')
f_2 = codecs.open('2.json', encoding='utf-8', mode='r')
f_3 = codecs.open('3.json', encoding='utf-8', mode='w')

f_1_txt = f_1.read()

for line in f_2.readlines():
    j = json.loads(line)
    reg_bus_ent_id = j['reg_bus_ent_id']
    if f_1_txt.find(reg_bus_ent_id) == -1:
        f_3.write(line)
