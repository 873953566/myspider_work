# -*- coding:utf-8 -*-

import urllib2
import random

ua = [
    "Mozilla/5.0(Macintosh;U;IntelMacOSX10_6_8;en-us)AppleWebKit/534.50(KHTML,likeGecko)Version/5.1Safari/534.50",
    "Mozilla/5.0(Windows;U;WindowsNT6.1;en-us)AppleWebKit/534.50(KHTML,likeGecko)Version/5.1Safari/534.50",
    "Mozilla/5.0(compatible;MSIE9.0;WindowsNT6.1;Trident/5.0;",
    "Mozilla/4.0(compatible;MSIE8.0;WindowsNT6.0;Trident/4.0)",
    "Mozilla/4.0(compatible;MSIE7.0;WindowsNT6.0)",
]

user_agent = random.choice(ua)
print user_agent

my_header = {
    "User-agent": user_agent,
    "message": "hehheheeh"
}
url = "https://www.taobao.com"

request = urllib2.Request(url, headers=my_header)

request.add_header("info", "爬虫")

response = urllib2.urlopen(request)

print response.read()
