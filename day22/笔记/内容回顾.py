
"""
作业:
    -- 汽车之家
        - https://www.cnblogs.com/Neeo/articles/10454499.html
    -- 天ji图
        - "http://pic.yesky.com/c/6_3655_{}.shtml".format(num)
内容回顾
    -- requests
        - requests.get(url='')
        - response = requests.request(method='get', url='httpxxxxx', json={})
            response.encoding
            response.headers
            response.content
            response.text
    -- selenium
        -
        - 问题
            - selenium.common.exceptions.SessionNotCreatedException: Message: session not created: This version of ChromeDriver only supports Chrome version 76
                - 浏览器驱动和浏览器的版本不一致
                - 解决办法
                    1. 先查看浏览器的版本是多少
                    2. 去下载一个与浏览器版本一致的浏览器驱动
                        - https://npm.taobao.org/mirrors/chromedriver
                            - notes.txt看一下版本是否一致
                    3. 将压缩包中的exe驱动放到python的scripts目录中
                        - 如果报selenium.common.exceptions.WebDriverException: Message: 'chromedriver' executable needs to be in PATH. Please see https://sites.google.com/a/chromium.org/chromedriver/home
                            - 法1. 将驱动目录添加到系统的环境变量
                            - 法2.
                                from selenium import webdriver
                                path = r'C:\Python36\Scripts\chromedriver1.exe'
                                driver = webdriver.Chrome(executable_path=path)

                    4. 重新运行代码检测
    -- 如果pip下载失败
        - pip install baidu-aip
        - pip install -i https://www.pypi.doubanio.com/simple/ baidu-aip

"""
# import requests
#
# # requests.get(url='')
# response = requests.request(method='get', url='httpxxxxx', json={})
# response.encoding
# response.headers
# response.content
# response.text



import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.implicitly_wait(10)
try:
    driver.get('https://pythonav.com/login/')
    # driver.find_element_by_id('id_username').send_keys('zhangkai')
    # 获取标签的属性或者css样式
    # 1. 找到标签
    # btn_obj = driver.find_element_by_xpath('//*[@id="fm"]/div[5]/div/input')
    # print(btn_obj.text)   # 获取标签的文本
    # print(btn_obj.submit())  # 如果标签有submit事件,就可以直接btn_obj.submit()
    # print(btn_obj.get_attribute('value'))   # 获取标签的属性
    # print(btn_obj.value_of_css_property('color'))
    # print(driver.save_screenshot('error.png'))


    # 获取验证码图片
    img = driver.find_element_by_id('image_code')
    print(img.size)
    # print(img.screenshot_as_png)
    with open('img.png', 'wb') as f:
        f.write(img.screenshot_as_png)
except Exception as e:
    print(e)
finally:
    time.sleep(19)
    driver.quit()



























