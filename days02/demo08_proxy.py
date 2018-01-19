# -*- coding:utf-8 -*-

import urllib2

url = "https://www.taobao.com"
request = urllib2.Request(url)

proxy_handler = urllib2.ProxyHandler({"http":"110.72.36.159:8123"})

proxy_open = urllib2.build_opener(proxy_handler)

response = proxy_open.open(request)


print response.read()