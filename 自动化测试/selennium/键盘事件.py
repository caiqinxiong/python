# -*- coding:utf-8 -*-
# caiqinxiong 

# 2019/12/15 下午3:31
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

executable_path = r'/Users/caiqinxiong/PycharmProjects/python/自动化测试/selennium/chromedriver'
driver = webdriver.Chrome(executable_path = executable_path)
driver.get('https://pythonav.com/login')
driver.maximize_window()
driver.find_element_by_class_name('form-control').send_keys('caiqinxiong')
driver.find_elements_by_class_name('form-control')[1].send_keys('mima')
driver.find_elements_by_class_name('form-control')[2].send_keys('1234')



time.sleep(10) # 10秒后关闭浏览器
# driver.close()
driver.quit()
