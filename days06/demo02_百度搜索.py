# -*- coding:utf-8 -*-

#引入测试模块
from selenium import webdriver
import os

# driver = webdriver.PhantomJS("./phantomjs-2.1.1-windows/bin/phantomjs")

driver = webdriver.Chrome(r'C:\Users\admin\AppData\Local\Google\Chrome\Application\chrome.exe')

driver.get("http://www.baidu.com")



# keyword = driver.find_element_by_id('kw')

# keyword.send_keys(u'火车票')

# driver.save_screenshot('baidu2.png')

driver.find_element_by_id("kw").send_keys("python")
#单击搜索按钮
driver.find_element_by_id("su").click()

#关闭浏览器
# driver.quit()