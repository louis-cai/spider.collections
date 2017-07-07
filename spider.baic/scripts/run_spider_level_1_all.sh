#!/usr/bin/env bash
cd /home/apps/spider.baic
python spider_detail_level/setup_qyxy_level_1_0.py &
sleep 5s
python spider_detail_level/setup_qyxy_level_1_1.py &
sleep 5s
python spider_detail_level/setup_qyxy_level_1_2.py &
sleep 5s
python spider_detail_level/setup_qyxy_level_1_3.py &
sleep 5s
python spider_detail_level/setup_qyxy_level_1_4.py &
sleep 5s