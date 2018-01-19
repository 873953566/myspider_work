# -*- coding:utf-8 -*-

import requests

# 定义post参数
post_data = {
    "i": "hello",# 要翻译的词语
    "from":	"AUTO", # 词语的翻译之前的语言
    "to":	"AUTO", # 词语翻译之后的语言
    "smartresult": "dict", # 数据类型
    "client":	"fanyideskweb", # 客户端标识
    "salt":	124141234234, # ~~~~可能是~~~时间
    "sign":	'a87123912423423435',# ~~~~可能是~~~~md5
    "doctype":	"json", # 数据类型
    "version":	2.1,# 版本号
    "keyfrom":	"fanyi.web",# 关键字
    "action":	"FY_BY_REALTIME",# 行为描述
    "typoResult":	False # 结果类型
}
# 发送请求，得到相应数据
response = requests.post("http://fanyi.youdao.com",data=post_data)

content = response.text
print content
print '###############################'
print '###############################'
print type(content)

with open("yaodao.html","w") as f:
    f.write("content".encode("utf-8"))













