
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

driver.get('https://pythonav.com/login/')
# 定位用户名
driver.find_element_by_class_name('form-control').send_keys('zhan')
time.sleep(3)
driver.find_element_by_class_name('form-control').send_keys(Keys.CONTROL, 'a')
time.sleep(1)
driver.find_element_by_class_name('form-control').send_keys(Keys.CONTROL, 'c')
# 密码
# driver.find_elements_by_class_name("form-control")[1].send_keys('66666')
# 验证码
driver.find_elements_by_class_name("form-control")[2].send_keys(Keys.CONTROL, 'v')


time.sleep(5)
driver.quit()



