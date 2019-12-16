'''
http://pic.yesky.com/c/6_3655_5.shtml
'''
import os
import requests
from bs4 import BeautifulSoup

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# print(BASE_DIR)
# 向指定连接发请求

response = requests.get(url='http://pic.yesky.com/c/6_3655_5.shtml')
# print(response.encoding)
# print(response.text)
# 使用bs4解析requests请求的响应文本

soup = BeautifulSoup(response.text, 'html.parser')   # lxml
div_obj = soup.find(name='div', attrs={"class": "lb_box"})
# print(div_obj)
dd_list = div_obj.find_all(name='dd')
# print(dd_list[0])
for dd in dd_list:
    # 获取div中所有图片所在a标签的url
    a_url = dd.find(name='a').get('href')
    path = os.path.join(BASE_DIR, 'tianji', dd.find(name='a').text)
    if not os.path.isdir(path):
        # 这有bug，自己改
        os.mkdir(path)
    # print(path)
    # 向url发请求
    a_response = requests.get(url=a_url)
    a_response.encoding = 'gbk'
    # print(a_response.encoding)
    # 拿到url中的text文本
    a_text = a_response.text
    son_soup = BeautifulSoup(a_text, 'html.parser')  # lxml
    son_div_obj = son_soup.find(name='div', attrs={"id": "scroll"})
    # print(son_div_obj)
    for img in son_div_obj.find_all(name='img'):
        # 获取图片链接，并发请求
        son_src = img.get('src').replace('113x113', '740x-')
        # print(son_src)
        son_response = requests.get(url=son_src)
        # 打开文件写入
        img_path = os.path.join(path, son_src.rsplit("/",1)[-1])
        # print(img_path)
        with open(img_path, 'wb') as f:
            f.write(son_response.content)
        # break
    break









