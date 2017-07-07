cd /home/apps/zhaopin_spider
dt=$(date "+%Y-%m-%d")
path_to_log="log/""$dt""_zhaopin_spider.log"
echo $path_to_log
scrapy crawl zhaopin_spider -s LOG_FILE=$path_to_log &
