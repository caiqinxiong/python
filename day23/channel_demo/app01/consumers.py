# -*- coding:utf-8 -*-
# caiqinxiong 
# 2019/12/29 下午3:24
from channels.generic.websocket import WebsocketConsumer
from channels.exceptions import StopConsumer

CONSUMER_OBJECT_LIST = []

class ChatConsumer(WebsocketConsumer):

    def websocket_connect(self, message):
        """
        客户端发来连接请求之后就会被触发
        :param message:
        :return:
        """
        # 服务端接收连接,向客户端浏览器发送一个加密字符串
        ret = self.accept()
        print(ret)
        # 连接成功
        CONSUMER_OBJECT_LIST.append(self)

    def websocket_receive(self, message):
        """
        客户端浏览器向服务端发送消息,此方法自动触发
        :param message:
        :return:
        """
        # 服务端给客户端回一条消息
        # self.send(text_data=message['text'])
        print(message)
        print(message['text'])
        for obj in CONSUMER_OBJECT_LIST:
            obj.send(text_data=message['text'])
    def websocket_disconnect(self, message):
        """
        客户端主动断开连接
        :param message:
        :return:
        """
        # 服务端断开连接
        CONSUMER_OBJECT_LIST.remove(self)
        raise StopConsumer()
