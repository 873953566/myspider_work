# -*- coding -*-

import urllib2

url = "https://www.baidu.com"

request = urllib2.Request(url)

response = urllib2.urlopen(request)

print response.read()