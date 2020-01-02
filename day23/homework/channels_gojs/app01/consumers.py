from channels.generic.websocket import WebsocketConsumer
from channels.exceptions import StopConsumer
import json
CONSUMER_OBJECT_LIST = []

class ChatConsumer(WebsocketConsumer):

    def websocket_connect(self, message):
        """
        客户端发来连接请求之后就会被触发
        :param message:
        :return:
        """
        # 服务端接收连接,向客户端浏览器发送一个加密字符串
        print(111111111111111)
        print(message)
        self.accept()
        # 连接成功
        # CONSUMER_OBJECT_LIST.append(self)
        l = [
            {'key': "start", 'text': '开始', 'figure': 'Ellipse', 'color': "lightgreen"},
            {'key': "download", 'parent': 'start', 'text': '下载代码', 'color': "lightgreen", 'link_text': '执行中...'},
            {'key': "compile", 'parent': 'download', 'text': '本地编译', 'color': "lightgreen"},
            {'key': "zip", 'parent': 'compile', 'text': '打包', 'color': "red", 'link_color': 'red'},
            {'key': "c1", 'text': '服务器1', 'parent': "zip"},
            {'key': "c11", 'text': '服务重启', 'parent': "c1"},
            {'key': "c2", 'text': '服务器2', 'parent': "zip"},
            {'key': "c21", 'text': '服务重启', 'parent': "c2"},
            {'key': "c3", 'text': '服务器3', 'parent': "zip"},
            {'key': "c31", 'text': '服务重启', 'parent': "c3"}
        ]
        l = json.dumps(l)
        self.send(text_data=l)

    def websocket_receive(self, message):
        """
        客户端浏览器向服务端发送消息,此方法自动触发
        :param message:
        :return:
        """
        print(22222222222222222222)
        # 服务端给客户端回一条消息
        self.send(text_data=message['text'])
        # for obj in CONSUMER_OBJECT_LIST:
        #     obj.send(text_data=message['text'])
    def websocket_disconnect(self, message):
        """
        客户端主动断开连接
        :param message:
        :return:
        """
        # 服务端断开连接
        # CONSUMER_OBJECT_LIST.remove(self)
        print(3333333333333333333)
        raise StopConsumer()
