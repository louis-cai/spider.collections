#!/usr/bin/env bash
cd /home/apps/spider.baic
python spider/setup_qyxy_qianzhan_0.py &
sleep 5s
python spider/setup_qyxy_qianzhan_1.py &
sleep 5s
python spider/setup_qyxy_qianzhan_2.py &
sleep 5s
python spider/setup_qyxy_qianzhan_3.py &
#sleep 5s
