#coding:utf-8

from lxml import etree
#从文件中加载html数据

html = etree.parse("index.html")

print(html)

ele_h1 = html.xpath("//h1")
print ele_h1
print ele_h1[0].xpath("string(.)")
print ele_h1[0].text


ele_h2_csb = html.xpath("//h2[@id='title2']")
print ele_h2_csb
print ele_h2_csb[0].text

ele_h2_zgl = html.xpath("//h2[@id='intro_title']")
print ele_h2_zgl
print ele_h2_zgl[0].text
print ele_h2_zgl[0].xpath("string(.)")

ele_p_hhl = html.xpath("//body/p[@class='content']")
print ele_p_hhl
for ele_p in ele_p_hhl:
    print ele_p

ele_p_hhl1 = html.xpath("//body/p[@class='content'][1]")
print ele_p_hhl1[0].text