# -*- coding:utf-8 -*-

import re


regexp = r'\d+'


pattern = re.compile(regexp)

#定义目标字符串
intro =  "hello 2018 world"

v_list = pattern.findall(intro)
print v_list