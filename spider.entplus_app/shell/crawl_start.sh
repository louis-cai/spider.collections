#!/usr/bin/env bash
cd /home/apps/entplus_app_spider


dt=$(date "+%Y-%m-%d")
path_to_log="log/""$dt""_crawl_gb2312.log"
echo $path_to_log

python setup.py >> $path_to_log &

