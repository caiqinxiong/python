# 创建一个进程是非常浪费时间 和 资源的
# 线程 -- 轻型进程
# 同一个进程之间的多个线程内存是共享的
# 线程的开启速度比进程快
# 线程也可以利用多核

# 正常的进程和线程之间的区别 :
    # 进程是 内存隔离的 占用的资源多
    # 线程之间 内存共享的 占用的资源少

# python的线程
    # cpython解释器下的多线程
    # 同一个进程下的多个线程不能被CPU同时执行
    # 多个线程中的IO操作仍然会被规避
# 大部分只要涉及到文件\网络的操作,多线程会更快
# 真正能够参与计算的不过就是那几个CPU
    # 规避IO操作,让IO操作的时间尽量的缩短
    # 或者尽量的复用这部分时间
import time
from urllib import request
from threading import Thread
url_lst = [
    'http://www.baidu.com',
    'http://www.sogou.com',
    'http://www.qq.com',
    'http://www.163.com',
    'http://www.taobao.com',
    'http://www.jd.com',
    'http://www.tmall.com',
    'http://www.cnblogs.com',
    'http://www.mi.com',
    'http://www.luffycity.com',
]
def get_url(url):
    ret = request.urlopen(url)  # 请求一个网页

start_t = time.time()
t_lst = []
for url in url_lst:   # 开启10个线程,每个线程个字去请求1个网页,即同时请求10个网页
    t = Thread(target=get_url,args=(url,))
    t.start()
    t_lst.append(t)
for t in t_lst:
    t.join()
print(time.time()-start_t)

# start_t = time.time()
# for url in url_lst:
#     ret = request.urlopen(url)
# print(time.time()-start_t)

# jython Python语言 最终是被JAVA解释器解释的 而java的解释器回收机制不是gc -- 不会受到全局解释器锁的影响
# pypy
# cpython 有一个全局解释器锁 GIL 是由于GC机制和解释型语言双重限制导致了必须要在解释器中加锁
         # 导致了在一个进程中不能有多个线程同时访问CPU
         # 虽然不能同时做计算会影响一些效率,但是绝大多部分情况下线程仍然能够非常好的提高程序的效率











