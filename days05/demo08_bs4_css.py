# -*- coding:utf-8 -*-

from bs4 import BeautifulSoup


soup = BeautifulSoup(open("index.html"),'lxml')

#1.标签选择器

span_e = soup.select('span')
print span_e

#2. ID选择器
h1_id = soup.select("#title")

print h1_id

#3.class选择器
p_class = soup.select(".content")
print p_class

#4. 包含选择器
p_e = soup.select('#container p')
print p_e

#5. 子类选择器
p_e = soup.select(('container > p'))
print p_e

#6. 属性选择器
div_attr = soup.select("div[class]")
print div_attr

div_attr2 = soup.select("div['intro']")
print div_attr2











