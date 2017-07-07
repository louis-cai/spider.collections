#!/usr/bin/env bash
cd /home/apps/spider.baic
python spider_detail_level/setup_qyxy_level_2_0.py &
sleep 5s
python spider_detail_level/setup_qyxy_level_2_1.py &
sleep 5s
python spider_detail_level/setup_qyxy_level_2_2.py &
sleep 5s
python spider_detail_level/setup_qyxy_level_2_3.py &
sleep 5s
python spider_detail_level/setup_qyxy_level_2_4.py &
sleep 5s