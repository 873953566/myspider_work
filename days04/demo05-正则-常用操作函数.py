#coding:utf-8

import re

'''
match(): 用于根据表达式进行字符匹配的操作函数~只匹配一次[从指定的起始位置进行匹配]
search(): 用于根据表达式进行字符匹配的操作函数~只匹配一次[从完整的目标字符串中进行检索匹配]
findall(): 用于根据表达式进行字符匹配~匹配多次，返回匹配到的列表
finditer(): 用于根据表达式进行字符撇皮~匹配多次，返回匹配到的迭代器
split(): 根据指定的表达式对目标字符串进行切割，返回切割后的列表
sub(): 用于字符替换

1. 匹配对象的函数
match(string[, pos[, endpos]])
search(string[, pos[, endpos]])
findall(string[, pos[, endpos]])
finditer(string[, pos[, endpos]])

2. re模块的函数
match(pattern, string, flags=0)
search(pattern, string, flags=0)
findall(pattern, string, flags=0)
finditer(pattern, string, flags=0)

3. 公共函数【匹配对象|re模块操作方式一样】
split()：拆分字符串的函数
sub()：根据正则替换字符串的函数

'''

intro = 'my name is ljy, i am 10 years old. i am nice'

#定义正则表达式
reg1 = 'my'
reg2 = '10'

#编译匹配对象
p1 = re.compile(reg1)
p2 = re.compile(reg2)

#match函数
print(p1.match(intro).group())
print(p2.match(intro))
print(p2.match(intro,21))

#search
print(p1.search(intro).group())
print(p2.search(intro))
print(p2.search(intro,21))

#findall
print(p1.findall(intro))
print(p2.findall(intro))

#finditer
print (p1.finditer(intro))
for p in p1.finditer(intro):
    print(p,p.group(),p.span(),p.start(),p.end())

#########################################################
print '#'*30
r_match = re.match(r'my',intro)
print(r_match.group(),r_match.span())


r2_match = re.match(r'10',intro)
print r2_match

r_search = re.match(r'my',intro)
print (r_search.group(),r_search.span())

r_findall = re.findall(r'my',intro)
print r_findall

r_finditer = re.finditer(r'my',intro)
print r_finditer

for x in r_finditer:
    print (x,x.group(),x.start(),x.end())

#拆分字符串
print '#' *30
s_list = re.split(r'\s+',intro)
print s_list

m_list = re.split(r'm',intro)
print m_list

x = 'm'.join(m_list)
print x

#字符串替换
print '#' *30
intro_replace = intro.replace('m',"*")
print intro_replace

intro_replace2 = intro.replace('m','*',2)
print intro_replace2

intro_replace3 = intro.replace(r'\d+','%')
print intro_replace3

intro_replace4 = re.sub(r'\d+','^_^',intro)
print intro_replace4








