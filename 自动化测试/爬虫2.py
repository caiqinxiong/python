# -*- coding:utf-8 -*-
# caiqinxiong 
# 2019/12/15 下午12:08
import os
import requests
from bs4 import BeautifulSoup
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

response = requests.get(url='http://pic.yesky.com/c/6_243_4.shtml')
print(response.status_code)
print(response.encoding)

soup = BeautifulSoup(response.text,'html.parser')
# print(soup)
div_obj = soup.find(name='div',attrs={'class':'lb_box'})
# print(div_obj)
dd_list = div_obj.find_all(name='dd')
# print(dd_list[0])
for i in dd_list:
    dir_path = i.text.split()[-1].replace('"','')
    dir_path = os.path.join(BASE_DIR,'img',dir_path)
    print(dir_path)
    if not os.path.exists(dir_path):os.makedirs(dir_path)
    href = i.find(name = 'a').get('href')
    a_respone = requests.get(url=href)
    print(a_respone.encoding)
    a_respone.encoding = 'gbk'
    a_text= a_respone.text
    son_response = BeautifulSoup(a_respone.text,'html.parser')
    # print(son_response)
    son_div = son_response.find(name='div',attrs={'id':'scroll'})
    # print(son_div)
    # img_dir = os.path.join(BASE_DIR,)
    for img in son_div.find_all(name='img'):
        # print(img)
        img_src = img.get('src').replace('113x113','740x-')
        img_path = img_src.rsplit('/',1)[-1]
        img_path = os.path.join(dir_path,img_path)
        # print(img_path)
        img_response = requests.get(url=img_src)
        with open(img_path,'wb') as f:
            f.write(img_response.content)
        break
    break