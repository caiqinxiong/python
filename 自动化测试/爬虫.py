# -*- coding:utf-8 -*-
# caiqinxiong 
# 2019/12/15 上午10:26
import os
import requests
from bs4 import BeautifulSoup
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# print(BASE_DIR)

# 1。模拟浏览器发请求
# response = requests.get(url='http://www.7160.com/meishitupian/list_15_2.html')
# response = requests.request('get',url='http://www.7160.com/meishitupian/list_15_2.html')
response = requests.request('get',url='http://www.7160.com/xiaohua/list_6_1.html')
print(response.status_code)
print(response.encoding)
response.encoding = 'gbk' # 编码转换
# print(response.text)

# 2.获取请求内容
text = response.text

# 3.使用bs4库解析请求
soup = BeautifulSoup(text,'html.parser')
# print(soup)
# 从文本中进一步缩小定位范围
div_obj = soup.find(name='div',attrs={'class':'news_bom-left'})
# print(div_obj)
li_list = div_obj.find_all(name='li')
# print(li_list[0])
for i in li_list:
    img = i.find(name='img')
    print(img)
    # 定位图片位置
    src = img.get('src')
    # 获取图片链接
    res = requests.get(url=src)
    # 保存图片路径
    file_path = os.path.join(BASE_DIR,'img',src.rsplit('/',1)[-1])
    print(file_path)
    # 写入图片
    # with open(file_path, 'wb') as f:
    #     f.write(res.content)
    break