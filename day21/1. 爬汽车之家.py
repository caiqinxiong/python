# -*- coding: utf-8 -*-
# __author__ = "maple"


"""
https://www.autohome.com.cn/all/

爬取汽车之家新闻页的新闻列表：图片，并且将图片保存到本地的目录内
    - 普通的爬取
    - 线程池爬取
-- requests
    - https://www.cnblogs.com/Neeo/articles/11511087.html
    - response.encoding  # 获取当前页面的编码
    - response.encoding = "gbk"     # 处理乱码问题
    - response.json()    # 获取json类型的数据
    - response.text   # 获取文本类型的数据
    - response.content   # 获取bytes类型的数据

-- bs4
    - find:找一个标签
    - find_all: 找所有标签
    - tag_obj.get('src')   # 取标签中的某个属性
    - tag_obj.text    # 获取标签的内容
"""

# ----------------------- 爬取汽车之家新闻页第一页 ---------------
# import os
# import requests   # 模拟浏览器发请求
# from bs4 import BeautifulSoup   # 解析请求结果，也就是去请求结果中，取数据
#
#
# url = "https://www.autohome.com.cn/all/"
# BASE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)))
#
#
#
# # 1. 使用requests模块向指定地址发请求
# # response = requests.request(method='get', url=url)
# response = requests.get(url=url)
# # 2. 获取请求结果
# # print(response.encoding)  # ISO-8859-1
# response.encoding = "gbk"
# # print(response.text)
# # 3. 使用bs4取数据，解析请求结果
# soup = BeautifulSoup(response.text, "html.parser")
# div_obj = soup.find(name='div', attrs={"id": "auto-channel-lazyload-article"})
# img_list = div_obj.find_all(name="img")
# for img in img_list:
#     # 获取图片的url，因为源地址是不全的，我们要拼接
#     img_url = "https:" + img.get("src")
#     # 使用requests模块向图片地址发请求，获取图片数据，bytes
#     img_response = requests.get(url=img_url)
#     # 制作保存图片的路径
#     file_path = os.path.join(BASE_DIR, 'img', img_url.rsplit('/', 1)[-1])
#     # 将bytes类型的数据保存到本地
#     with open(file_path, 'wb') as f:
#         f.write(img_response.content)
    # break







# ----------------------- 顺序爬取汽车之家新闻页50页 ---------------

# import os
# import requests   # 模拟浏览器发请求
# from bs4 import BeautifulSoup   # 解析请求结果，也就是去请求结果中，取数据
#
#
# # url = "https://www.autohome.com.cn/all/"
# BASE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)))
#
#
# def spider(num):
#     # 1. 使用requests模块向指定地址发请求
#     # response = requests.request(method='get', url=url)
#     response = requests.get(url="https://www.autohome.com.cn/all/{}/#liststart".format(num))
#     # 2. 获取请求结果
#     # print(response.encoding)  # ISO-8859-1
#     response.encoding = "gbk"
#     # print(response.text)
#     # 3. 使用bs4取数据，解析请求结果
#     soup = BeautifulSoup(response.text, "html.parser")
#     div_obj = soup.find(name='div', attrs={"id": "auto-channel-lazyload-article"})
#     img_list = div_obj.find_all(name="img")
#     for img in img_list:
#         # 获取图片的url，因为源地址是不全的，我们要拼接
#         img_url = "https:" + img.get("src")
#         # 使用requests模块向图片地址发请求，获取图片数据，bytes
#         img_response = requests.get(url=img_url)
#         # 制作保存图片的路径
#         file_path = os.path.join(BASE_DIR, 'img', img_url.rsplit('/', 1)[-1])
#         # 将bytes类型的数据保存到本地
#         with open(file_path, 'wb') as f:
#             f.write(img_response.content)
#         print('{} 爬取完毕'.format(img_url))
#
#
# if __name__ == '__main__':
#     import time
#     start = time.time()
#     for num in range(1, 51):
#         spider(num)
#     print(time.time() - start)


# --------------------- 线程池爬取汽车之家新闻页50页 --------------------

import os
import requests   # 模拟浏览器发请求
from bs4 import BeautifulSoup   # 解析请求结果，也就是去请求结果中，取数据
from concurrent.futures import ThreadPoolExecutor  # 线程池

# url = "https://www.autohome.com.cn/all/"
BASE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)))


def spider(num):
    # 1. 使用requests模块向指定地址发请求
    # response = requests.request(method='get', url=url)
    page_url = "https://www.autohome.com.cn/all/{}/#liststart".format(num)
    response = requests.get(url=page_url)
    # 2. 获取请求结果
    # print(response.encoding)  # ISO-8859-1
    response.encoding = "gbk"
    # print(response.text)
    # 3. 使用bs4取数据，解析请求结果
    soup = BeautifulSoup(response.text, "html.parser")
    div_obj = soup.find(name='div', attrs={"id": "auto-channel-lazyload-article"})
    img_list = div_obj.find_all(name="img")
    for img in img_list:
        # 获取图片的url，因为源地址是不全的，我们要拼接
        img_url = "https:" + img.get("src")
        # 使用requests模块向图片地址发请求，获取图片数据，bytes
        img_response = requests.get(url=img_url)
        # 制作保存图片的路径
        file_path = os.path.join(BASE_DIR, 'img', img_url.rsplit('/', 1)[-1])
        # 将bytes类型的数据保存到本地
        with open(file_path, 'wb') as f:
            f.write(img_response.content)
        print('正在爬取{} 页 中的{}图片 爬取完毕'.format(page_url, img_url))

if __name__ == '__main__':
    import time
    start = time.time()
    t = ThreadPoolExecutor(max_workers=10)
    for num in range(1, 51):
        t.submit(spider, num)
    t.shutdown()
    print(time.time() - start)


































