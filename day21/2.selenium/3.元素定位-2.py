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
driver.get('https://pythonav.com/login/')
# 定位用户名
driver.find_element_by_class_name('form-control').send_keys('zhan')
# 密码
driver.find_elements_by_class_name("form-control")[1].send_keys('66666')
# 验证码
driver.find_elements_by_class_name("form-control")[2].send_keys('66666')

# 确定按钮
driver.find_element_by_xpath('//*[@id="fm"]/div[5]/div/input').click()
# 判断是否登录成功
text = driver.find_element_by_xpath('//*[@id="fm"]/div[2]/span').text
print(text)
if text:  # 登录失败，截屏
    driver.save_screenshot('error.png')
time.sleep(3)
driver.quit()




