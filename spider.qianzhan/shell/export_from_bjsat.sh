#!/usr/bin/env bash
cd /home/apps/qianzhan_spider
dt=$(date "+%Y-%m-%d")
path_to_log="log/""$dt""_export_from_bjsat.log"
echo $path_to_log
python helper/export_from_bjsat.py &
