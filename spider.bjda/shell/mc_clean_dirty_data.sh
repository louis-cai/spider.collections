#!/usr/bin/env bash
cd /home/apps/bjda_spider
dt=$(date "+%Y-%m-%d")
path_to_log="log/""$dt""_mc_clean_dirty_data.log"
echo $path_to_log
scrapy mc_clean_dirty_data -s LOG_FILE=$path_to_log &
