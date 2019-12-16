

# -------------- 显式等待  ---------------
# import time
# from selenium import webdriver
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.common.by import By
#
# executable_path = r'C:\Python36\Scripts\chromedriver.exe'
# driver = webdriver.Chrome(executable_path=executable_path)
# wait = WebDriverWait(driver, 10, 0.5)
# # 访问url
# driver.get('https://www.baidu.com/')
# # 向input框输入内容
# # input_obj = driver.find_element_by_id('kw')
# # # print(input_obj)
# # input_obj.send_keys('听雨危楼')
#
# driver.find_element_by_id('kw').send_keys('听雨危楼')
# # 定位button按钮
# driver.find_element_by_id('su').click()
# # 点击输入结果
# # time.sleep(3)
# # WebDriverWait(driver, 10, 0.5).until(EC.presence_of_element_located((By.LINK_TEXT, '听雨危楼 - 博客园'))).click()
# wait.until(EC.presence_of_element_located((By.LINK_TEXT, '听雨危楼 - 博客园'))).click()
# driver.find_element_by_xpath('//*[@id="1"]/h3/a/em').click()   # 根据xpath定位
# driver.quit()



# -------------- 隐式等待  ---------------


import time
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

executable_path = r'C:\Python36\Scripts\chromedriver.exe'
driver = webdriver.Chrome(executable_path=executable_path)
# wait = WebDriverWait(driver, 10, 0.5)   # 显式等待
driver.implicitly_wait(10)
# 访问url
driver.get('https://www.baidu.com/')
# 向input框输入内容
# input_obj = driver.find_element_by_id('kw')
# # print(input_obj)
# input_obj.send_keys('听雨危楼')

driver.find_element_by_id('kw').send_keys('听雨危楼')
# 定位button按钮
driver.find_element_by_id('su').click()
# 点击输入结果
# time.sleep(3)
# WebDriverWait(driver, 10, 0.5).until(EC.presence_of_element_located((By.LINK_TEXT, '听雨危楼 - 博客园'))).click()
# wait.until(EC.presence_of_element_located((By.LINK_TEXT, '听雨危楼 - 博客园'))).click()
# 隐式等待
# driver.find_element_by_xpath('//*[@id="1"]/h3/a/em').click()

# time.sleep(3)
# driver.quit()






