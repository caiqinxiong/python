# -*- coding:utf-8 -*-
# caiqinxiong 

# 2019/12/15 下午3:31
import time
from selenium import webdriver

executable_path = r'/Users/caiqinxiong/PycharmProjects/python/自动化测试/selennium/chromedriver'
driver = webdriver.Chrome(executable_path = executable_path)
driver.get('http://www.baidu.com')
driver.maximize_window()
driver.find_element_by_id('kw').send_keys('雨之夜&秋')
driver.find_element_by_id('su').click()
time.sleep(3)
driver.find_element_by_xpath('//*[@id="1"]/h3/a/em').click()



time.sleep(10) # 10秒后关闭浏览器
# driver.close()
driver.quit()
