import sys
import os
import json
import struct
import socket

def send_dic(sk,dic,protocol=False):
    bytes_d = json.dumps(dic).encode('utf-8')
    if protocol:  # 如果protocol是True 就按照协议来执行send，如果protole不是True,就不需要协议，直接发送json字典即可
        # 在实际发送字典之前，先把字典的字节类型的长度计算出来，然后先发送字典的长度，再发字典内容
        len_b = len(bytes_d)
        len_dic = struct.pack('i', len_b)
        sk.send(len_dic)
    sk.send(bytes_d)

def recv_dic(sk):
    str_dic = sk.recv(1024).decode('utf-8')
    res_dic = json.loads(str_dic)
    return res_dic

def get_user(opt='login'):
    d = {}
    usr = input('用户名:').strip()
    pwd = input('密码:').strip()
    if usr and pwd and opt == 'register':
        pwd2 = input('密码确认:').strip()
        if pwd == pwd2:
            d = {'username': usr, 'password': pwd,'operate': opt}
    elif usr and pwd:
        d = {'username': usr, 'password': pwd, 'operate': opt}
    return d

def login(sk):
    d = get_user()
    if d : send_dic(sk,d)
    res_dic = recv_dic(sk)
    if res_dic['operate'] == 'login' and res_dic['flag']:
        print('登录成功')
        return True
    else:
        print('登录失败')

def register(sk):
    d = get_user('register')
    if d : send_dic(sk,d)
    res_dic = recv_dic(sk)
    if res_dic['operate'] == 'register' and res_dic['flag']:
        print('注册成功')
        return True
    else:
        print('注册失败')

def processBar(num, total):
        '''打印进度条'''
        rate = num / total
        rate_num = int(rate * 100)
        bar = ('>' * rate_num, rate_num,) # 展示的进度条符号
        r = '\r%s>%d%%\n' % bar if rate_num == 100 else '\r%s>%d%%' % bar
        sys.stdout.write(r) # 覆盖写入
        return  sys.stdout.flush # 实时刷新

def upload(sk):
    # 在本地你可以输入任意的路径 选择任意文件上传
    path = input('请输入要上传的文件路径: ')
    if os.path.isfile(path):
        filename = os.path.basename(path)
        filesize = os.path.getsize(path)
        dic = {'filename': filename, 'filesize': filesize, 'operate': 'upload'}
        send_dic(sk,dic,True)  # True表示这里使用自定义协议进行字典的传递
        num = 0
        with open(path,'rb') as f:
            while filesize>0:
                content = f.read(1024*1000)
                num += len(content)
                processBar(num,dic['filesize'])
                sk.send(content)
                filesize -= len(content)

def download(sk):
    pass

def myquit(sk):
    pass

def choose_opt(opt_lst):
    for index, opt in enumerate(opt_lst, 1):
        print(index, opt[0])
    num = int(input('请输入要选择的操作序号 ：'))
    func = opt_lst[num - 1][1]  # func = login / register
    return func

sk = socket.socket()
sk.connect(('127.0.0.1',9001))
while True:
    # 登录/注册
    opt_lst = [('登录',login),('注册',register)]
    func = choose_opt(opt_lst)
    res = func(sk)   # 登录注册

    while res:    # 如果登录或者注册成功，才能进行上传和下载
        opt_lst2 = [('上传',upload),('下载',download),('退出',myquit)]
        func = choose_opt(opt_lst2)
        func(sk)   # 登录注册

# 上传
    # 在本地你可以输入任意的路径 选择任意文件上传
    # 将文件名和文件大小发送到对方
    # 对方根据文件大小和名字进行接收 和写文件
    # 上传到远程服务器中的哪个位置 ：默认的文件夹remote中

# 下载
    # 从固定的remote文件夹下下载对应的内容，直接输入remote文件夹中存在的文件名
    # 在server端计算文件的大小 和文件名 组成字典发送到客户端
    # 客户端接收数据，并预备接收文件，这个文件暂时下载到固定的文件夹local下
    # server端读文件发送数据，client端打开文件 接收数据 写文件
    # 过程中注意连续发送的数据可能产生粘包问题，需要用自定义协议解决 其他内容基本和上传一致

# 退出
    # 如果需要退出，不能单方面退出
    # 需要用户先发消息到服务端，然后再完成客户端的结束


# 具体的操作 ：上传、下载、退出


# 进阶需求的讲解
    # 下载和上传加入进度条
    # 每个用户都有自己的家目录
        # 在server端应该有一个固定的目录root，里面放着所有的用户的目录
        # 如果用户注册，就以用户的唯一标识为名创建一个属于他的文件夹
        # 接下来alex登录之后，就把alex的用户名作为他的家目录，上传和下载都基于自己的家目录完成
    # 磁盘配额
        # 每一个用户都需要有一个自己的磁盘配额
        # 每次登录 就对已经上传的文件进行一次大小的计算 记录下来
        # 每次上传文件的时候就对这个文件大小进行评估 判断磁盘配额 - 已经上传占用的位置 是否大于 文件大小
        # 如果大于 就上传
        # 如果小于 就提前报放不下。。。
    # 断点续传
        # seek来完成
        # 你如何确定你断点上传的文件和原来的文件是一个文件？？？