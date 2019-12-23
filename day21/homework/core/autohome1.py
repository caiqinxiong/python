# -*- coding: utf-8 -*-
__author__ = 'caiqinxiong_cai'
#2019/12/16 10:35
import os
import time
import requests
import traceback
from bs4 import BeautifulSoup
from  multiprocessing import Process, Pool
from threading import Thread
from concurrent.futures import ThreadPoolExecutor  # 线程池
import gevent
from conf import settings as ss
from core.log import Log as log

def save_img(file_name,content):
    '''保存图片到本地'''
    with open(file_name, 'wb') as f:
        f.write(content)

def spider(num):
    '''爬虫操作'''
    rep_url = r"https://www.autohome.com.cn/all/{}/#liststart".format(num)
    print(rep_url)
    # 1. 模拟浏览器发请求
    response = requests.get(url=rep_url)
    # response.encoding = 'gbk'
    # 2. 获取请求内容
    text = response.text
    # 3. 使用bs4库解析请求
    soup = BeautifulSoup(text, 'html.parser')  # html.parser:解析器，负责解析文本
    # 从整个文本中进一步缩小定位范围， div:所有图片外部的盒子
    div_obj = soup.find(name='div', attrs={"class": "article-wrapper"})
    # print(div_obj)
    # 4. 定位图片位置
    # 从盒子中找所有li标签
    li_list = div_obj.find_all(name="li")
    for li in li_list:
        # 5. 获取图片链接
        img = li.find(name='img')
        try:
            src = img.get("src")
            # print(src)
            img_name = src.rsplit('/',1)[-1]
            file_name = os.path.join(ss.IMG_PATH,img_name)
            # 获取到的图片链接没有http，给补齐
            if not src.startswith('http'): src = 'http:' + src
            # 6. 使用requests模块向图片链接发请求
            res = requests.get(url=src)
            # 7.保存图片到本地
            save_img(file_name, res.content)
        except Exception as e:
            log.error(traceback.format_exc())

        # break


def thread_pool():
    t = ThreadPoolExecutor(max_workers=10)
    for num in range(1, 101):
        t.submit(spider,num)
    t.shutdown()


if __name__ == '__main__':
    start = time.time()
    thread_pool()
    # for num in range(1, 51):
    #     gevent.joinall([
    #         gevent.spawn(spider,num),
    #     ])

#     pool = Pool(5) # 进程池，允许进程池同时放入5个进程
#     print('主进程：',os.getpid())
#     for i in range(10):
#         pool.apply_async(func=spider)#callback=回调，Foo（子进程）执行完才回调Bar（主进程）
#         print('主进程：',i, os.getpid())
# #
    print(time.time() - start)





