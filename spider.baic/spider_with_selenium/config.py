# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

# download_delay = 1.0
implicitly_wait = 1.0

log_file1 = "log/log.log"
log_file2 = "log/debug.log"


max_thread_num = 4 * 2 + 2


proxy_type = "http"
proxy_ip = "211.143.45.216"
proxy_port = "3128"
proxies = "%s://%s:%s" % (proxy_type, proxy_ip, proxy_port)
