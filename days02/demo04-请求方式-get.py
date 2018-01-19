# -*- coding:utf-8 -*-
import urllib2
import random
import urllib

ua = [
    "Mozilla/5.0(Macintosh;U;IntelMacOSX10_6_8;en-us)AppleWebKit/534.50(KHTML,likeGecko)Version/5.1Safari/534.50",
    "Mozilla/5.0(Windows;U;WindowsNT6.1;en-us)AppleWebKit/534.50(KHTML,likeGecko)Version/5.1Safari/534.50",
    "Mozilla/5.0(compatible;MSIE9.0;WindowsNT6.1;Trident/5.0;",
    "Mozilla/4.0(compatible;MSIE8.0;WindowsNT6.0;Trident/4.0)",
    "Mozilla/4.0(compatible;MSIE7.0;WindowsNT6.0)",
]

user_agent = random.choice(ua)

keyword = raw_input("请输入你想搜索的关键词:")

get_parma = {
    'wd':keyword
}
#重新编码
data = urllib.urlencode(get_parma)
#定义url地址
url = "http://www.baidu.com/s?"

full_url = url + data
print full_url

#封装求求对象
request = urllib2.Request(full_url)

request.add_header('User_agent',user_agent)
response = urllib2.urlopen(request)

print response.read()