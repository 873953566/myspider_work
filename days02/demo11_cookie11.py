import urllib2
import cookielib

cookie = cookielib.MozillaCookieJar()

cookie.load("fanyi.txt")

cookie_handler = urllib2.HTTPCookieProcessor(cookie)

cookie_opener = urllib2.build_opener(cookie_handler)

response = cookie_opener.open("http://www.baidu.com")

print response.read()