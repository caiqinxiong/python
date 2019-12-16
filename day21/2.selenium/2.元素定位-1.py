'''
selenium元素定位
    -- id
    -- class
        classes
    -- xpath
    -- tag
    -- link_text
'''

# 根据id定位
import time
from selenium import webdriver
executable_path = r'C:\Python36\Scripts\chromedriver.exe'
driver = webdriver.Chrome(executable_path=executable_path)
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
time.sleep(3)
driver.find_element_by_xpath('//*[@id="1"]/h3/a/em').click()   # 根据xpath定位
time.sleep(3)
driver.quit()




