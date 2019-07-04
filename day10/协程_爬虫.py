# -*- coding:utf-8 -*-
# Author:caiqinxiong


import gevent,time
#from  urllib.request import urlopen # python3
from  urllib import urlopen # python2
from gevent import monkey; # gevent 不能识别urllib和socket,打上补丁
monkey.patch_all() # 把当前程序所有打IO操作给我单独做上标记

def f(url):
    print('GET: %s' % url)
    resp = urlopen(url)
    data = resp.read()
    print('%d bytes received from %s.' % (len(data), url))

urls = ['https://www.python.org/',
        'https://www.yahoo.com/',
        'https://github.com/']
start_time = time.time()
for url in urls:
    f(url)
print('同步cost：',time.time()-start_time)

async_time = time.time()
gevent.joinall([
    gevent.spawn(f, 'https://www.python.org/'),
    gevent.spawn(f, 'https://www.yahoo.com/'),
    gevent.spawn(f, 'https://github.com/'),
])
print("异步cost:",time.time()-async_time)