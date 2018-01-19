# -*- coding:utf-8 -*-

import requests

get_params = {
    "wd":'会员'
}
#get参数,通过params参数赋值，直接传递

response = requests.get("http://www.baidu.com/s",params=get_params)

#打印数据
print(response.text)

# get_param = {
#     "wd": "火影"
# }
# # get参数，通过params参数赋值，直接传递
# response = requests.get("http://www.baidu.com/s", params=get_param)
#
# # 打印获取数据
# print(response.text)
