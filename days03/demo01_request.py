# -*- coding:utf-8 -*-
import requests


response = requests.get("http://www.taobao.com")


content = response.text

print content

