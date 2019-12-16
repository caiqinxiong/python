'''
1. 下载 selenium 模块
pip install selenium

2. 下载浏览器驱动
    - https://www.cnblogs.com/Neeo/articles/10671532.html  # 下载selenium驱动
    - 注意，浏览器驱动和浏览器版本保持一致 notes.txt
    - 将驱动安装到python的目录去    环境变量的目录
'''
import time
from selenium import webdriver

# 获取浏览器对象
driver = webdriver.Chrome()
driver.get('https://www.baidu.com')  # 访问url
# 常用的操作
# print(driver.title)  # 百度一下，你就知道
# driver.maximize_window()  # 窗口最大化
# driver.minimize_window()  # 窗口最小化
# print(driver.current_url)  # https://www.baidu.com/
# print(driver.current_window_handle)  # CDwindow-C1C326D35B1E228B5FCBD679B1FD6EBC
# print(driver.page_source)  # 当前页面的内容
# print(driver.get_cookie())
# driver.add_cookie()
# driver.save_screenshot('a.png')   # 截图 必须是png图片



# time.sleep(3)
# # driver.close() # 关闭当前窗口对象
# driver.quit()  # 退出浏览器









