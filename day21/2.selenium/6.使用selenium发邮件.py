
import time
from selenium import webdriver
from selenium.webdriver import ChromeOptions  # 需要导入的类
from selenium.webdriver.common.keys import Keys
from getpass import getpass



def run():
    driver.get(url='https://mail.163.com')

    # 点击密码登录
    driver.find_element_by_id('switchAccountLogin').click()
    # 遇到iframe，需要切换
    iframe_list = driver.find_elements_by_tag_name('iframe')
    # print(iframe_list)
    driver.switch_to.frame(iframe_list[0])   # 将driver对象切iframe中
    # driver.switch_to.default_content()   # 切出来
    # 获取用户名并输入
    driver.find_element_by_class_name('dlemail').send_keys(user)

    # 获取密码框并输入
    driver.find_element_by_class_name('dlpwd').send_keys(pwd)
    driver.find_element_by_class_name('dlpwd').send_keys(Keys.ENTER)
    # 点击登录按钮, bug在此,但是，已解决
    # driver.find_element_by_xpath('//*[@id="dologin"]').click()
    # driver.find_element_by_id('dologin').click()
    # time.sleep(5)

    # 点击写信
    driver.find_element_by_id('_mail_component_19_19').click()

    # 输入收件人信息
    driver.find_element_by_class_name('nui-editableAddr-ipt').send_keys(to)
    # driver.find_element_by_class_name('nui-editableAddr-ipt').send_keys(Keys.TAB)
    # 输入主题信息
    res = driver.find_elements_by_class_name('nui-ipt-input')
    # print(1111111111, res)
    res[2].send_keys(theme)
    # 遇到iframe
    iframe = driver.find_element_by_class_name('APP-editor-iframe')
    driver.switch_to.frame(iframe)
    # 输入文本
    driver.find_element_by_class_name('nui-scroll').send_keys(content)
    # 从iframe中切出来
    driver.switch_to.default_content()
    # 点击发送按钮
    driver.find_element_by_class_name('nui-mainBtn').click()

if __name__ == '__main__':
    to = '1206180814@qq.com'
    theme = 'python自动化27期selenium'
    content = '天不生我李淳罡， 剑道万古如长夜............'
    user = 'tingyuweilou'
    pwd = getpass("密码: ")
    # pwd = 'aaaa'
    # try:
    # 创建 option 对象
    option = ChromeOptions()
    option.add_experimental_option('excludeSwitches', ['enable-automation'])
    # 创建浏览器对象
    driver = webdriver.Chrome(options=option)
    driver.implicitly_wait(10)
    run()
    # except Exception as e:
    #     print(e)
    # finally:
    #     time.sleep(20)
    #     driver.quit()









