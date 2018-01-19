# -*- coding:utf-8 -*-

import requests

response = requests.get("http://www.baidu.com")

#响应数据编码的位置
response.encoding = "utf-8"

print (response.text)