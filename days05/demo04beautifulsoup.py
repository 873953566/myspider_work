#coding:utf-8

from bs4 import BeautifulSoup

#加载网页数据
#从爬虫获取的网页数据查找

soup = BeautifulSoup(open('index.html'),'lxml')
print soup#soup对象，包含了整个dom模型树

