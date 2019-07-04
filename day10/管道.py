# -*- coding:utf-8 -*-
# Author:caiqinxiong
from multiprocessing import Process,Pipe

def f(conn):
    conn.send('hi,lixiaoxin,from child.')
    conn.send('miss you again,from child')
    print('%s from parent.' % conn.recv())
    conn.close()

if __name__ == '__main__':
    A , B = Pipe() # 管道两端，返回两个值
    p = Process(target=f,args=(A,))
    p.start()
    print(B.recv())
    print(B.recv())
    B.send('I am fine!')
    p.join()
