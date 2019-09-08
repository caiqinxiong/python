#encoding:utf-8
#--title：'马海阳'
#--mtime：'2019/9/3'

import socketserver
from core.action import Action



class FtpServer(socketserver.BaseRequestHandler):
    '''socketserver 自建的服务器端'''
    def handle(self):
        action = Action(self.request) # 实例化 并将socket对象传入
        while True:
                response = action.recv_messages()  # 接收客户端发送的请求

                if response['cmd'] == 'quit': # 判断 发送过来的是quit 就结束死循环
                    break
                elif hasattr(action,response['cmd']): # 判断客户端发送过来的是否可调用
                    getattr(action,response['cmd'])(response)  # 反射执行
        self.request.close()