# -*- coding:utf-8 -*-

import urllib2
import cookielib



cookie = cookielib.CookieJar()

cookie_handler = urllib2.HTTPCookieProcessor(cookie)

cookie_opener = urllib2.build_opener(cookie_handler)

response = cookie_opener.open("https://www.baidu.com")

for item in cookie:
    print ("%s-%s" % (item.name,item.value))
    #"{} - {}" (hello world)