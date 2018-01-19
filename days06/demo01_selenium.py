# -*- coding:utf-8 -*-

from selenium import webdriver

# driver = webdriver.PhantomJS('./phantomjs-2.1.1-windows/bin/phantomjs')
driver = webdriver.Chrome(r'C:\Users\admin\AppData\Local\Google\Chrome\Application\chrome.exe')

driver.get('http://www.baidu.com')


driver.save_screenshot("baidu.png")

with open("baidu.html",'w') as f:
    f.write(driver.page_source.encode("utf-8"))