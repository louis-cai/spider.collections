#!/usr/bin/env bash
cd /home/apps/jd_spider
dt=$(date "+%Y-%m-%d")
path_to_log="log/""$dt""_error.log"
echo $path_to_log
scrapy crawl jd_spider_a -s LOG_FILE=$path_to_log &
