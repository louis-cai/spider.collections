#!/usr/bin/env bash
cd /home/apps/spider.baic
python tools/restart_squid_service.py
sleep 5
ps -aux | grep qyxy | awk '{print $2}' | while read line; do kill -9 $line; done;
sleep 5
sh scripts/run_spider_qianzhan_all.sh &
sleep 5
sh scripts/run_spider_level_1.sh &
sh scripts/run_spider_level_2.sh &
