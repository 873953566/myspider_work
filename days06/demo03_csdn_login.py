# -*- coding:utf-8 -*-

#引入自动化测试

from selenium import webdriver
#启动phantomjs无界面浏览器
driver = webdriver.PhantomJS('./phantomjs-2.1.1-windows/bin/phantomjs')

#访问登录界面
driver.get("https://passport.csdn.net/account/login?ref=toolbar")
#截图查看是否成功
# driver.save_screenshot('csdn1.png')

#登录表单中填写正常
driver.find_element_by_id('username').send_keys(u'18538113667')
driver.find_element_by_id('password').send_keys(u'123456')

# driver.save_screenshot('csdn1.png')

#开始登陆
btn = driver.find_element_by_css_selector('#fm1 .logging')
btn.click()
driver.save_screenshot('csdn2.png')