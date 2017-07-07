#!/usr/bin/env bash
cd /home/apps/huangye88_spider
dt=$(date "+%Y-%m-%d")
path_to_log="log/""$dt""_crawl_all.log"
echo $path_to_log
scrapy crawl huangye88_spider -s LOG_FILE=$path_to_log &
