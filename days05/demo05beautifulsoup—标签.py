#coding:utf-8

from bs4 import BeautifulSoup

soup = BeautifulSoup(open("index.html"),'lxml')

print soup.title
print soup.div

print soup.h1.attrs
print soup.h1.attrs['class']
print soup.h1.attrs.get('class')
print soup.h2.attrs

print soup.h2.string
