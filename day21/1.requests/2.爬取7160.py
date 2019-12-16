'''
http://www.7160.com/meishitupian/list_15_2.html
pip install beautifulsoup4

'''

# 0. 导包
import os
import requests
from bs4 import BeautifulSoup
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
print(BASE_DIR)
# 1. 模拟浏览器发请求
response = requests.get(url='http://www.7160.com/meishitupian/list_15_2.html')
# print(response.status_code)
# print(response.encoding)
response.encoding = 'gbk'
# 2. 获取请求内容
text = response.text
# 3. 使用bs4库解析请求
soup = BeautifulSoup(text, 'html.parser')  # html.parser:解析器，负责解析文本

# print(soup)
# 从整个文本中进一步缩小定位范围， div:所有图片外部的盒子
div_obj = soup.find(name='div', attrs={"class": "news_bom-left"})
# print(div_obj)
# 4. 定位图片位置
# 从盒子中找所有li标签
li_list = div_obj.find_all(name="li")
for li in li_list:
    # 5. 获取图片链接
    img = li.find(name='img')
    src = img.get("src")
    print(src)
    # 6. 使用requests模块向图片链接发请求
    res = requests.get(url=src)
    # 7. 保存图片到本地
    file_path = os.path.join(BASE_DIR, '7160', src.rsplit('/', 1)[-1])
    with open(file_path, 'wb') as f:
        f.write(res.content)
    # break
















