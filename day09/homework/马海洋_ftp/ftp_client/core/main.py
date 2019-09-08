#encoding:utf-8
#--title：'马海阳'
#--mtime：'2019/9/4'

import sys
import socket
from core.user_login import User
from core.program import Program
from conf.settings import IP_PORT
from core.warpper import format_wrapper



def run(obj):
    '''用户功能'''
    for index, pro_list in enumerate(obj.program_list, 1): print(index, pro_list[0])
    user_input = int(input('\n请输入你要操作的功能：').strip())
    # 反射执行主要功能
    if not user_input > len(obj.program_list) and hasattr(obj, obj.program_list[user_input - 1][1]):
        getattr(obj, obj.program_list[user_input - 1][1])()
    else:
        print('请输入正确的功能数字')


def main():
    '''客户端功能总逻辑'''
    sk = socket.socket() # 实例化
    sk.connect(IP_PORT) # 连接服务端
    cls = getattr(sys.modules[__name__],'User') # 反射客户端的用户登陆注册功能
    obj = cls(sk)  # 实例化，将连接传进去
    # 死循环
    while True:
        for index,opt in enumerate(obj.user_list,1):print(index,opt[0])
        input_num = int(input('\n请输入功能序号：').strip())

        # 反射执行用户功能
        if not input_num > len(obj.user_list) and hasattr(obj,obj.user_list[input_num-1][1]) :
                getattr(obj,obj.user_list[input_num-1][1])()
        else:
            print('请输入正确的功能数字')

        # 获取上面用户登录状态的flag
        if not getattr(obj,'flag'): # 判断flag为False
            continue  # 跳出本层循环
        else:
            # 反射客户端主要功能的类内存地址
            cls = getattr(sys.modules[__name__], 'Program')
            obj = cls(sk) # 实例化
            while True:
                run(obj)