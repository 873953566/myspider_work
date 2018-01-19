# -*- coding:utf-8 -*-

from bs4 import BeautifulSoup

soup = BeautifulSoup(open("index.html"),'lxml')

print soup.div.contents
print soup.div.children

for child in soup.div.children:
    print child.string

# print dir(soup)