# 网络编程
    # 1.概念
        # osi五层协议
            # 应用层
            # 传输层
                # tcp 面向连接通信,并且数据之间无边界,可靠
                    # 先建立连接 : 三次握手
                    # 基于连接通信 :每一条信息都有回执
                        # 粘包现象
                            # struct模块自定义协议解决
                    # 断开连接 :  四次挥手
                # udp 不需要提前建立链接,数据之间有边界,不可靠-
                    # 不需要建立\断开连接
                    # 只要知道对方的ip和端口直接发送信息就可以
            # 网络层
            # 数据链路层
            # 物理层
    # 2.代码
        # socket
        # osi5层协议除了应用层之外其他基层的抽象层
# # tcp-server
# import socket
# sk = socket.socket()
# sk.bind(('192.168.12.1',9001))
# sk.listen()
#
# conn,addr = sk.accept()   # 接受客户端请求建立连接 -- 三次握手
# conn.send(msg)     # msg必须是字节类型
# message = conn.recv(n)    # n是接受消息的最大字节数
# conn.close()       # 关闭了和某一个客户端的连接 -- 四次挥手
#
# sk.close()         # 关闭了整个网络服务
#
# # tcp-client-+
# import socket
# sk = socket.socket()
# sk.connect(('192.168.12.1',9001))  #  三次握手
# message = sk.recv(n)
# sk.send(msg)
# sk.close()

# udp-server
# import socket
# socket.socket(type = socket.SOCK_DGRAM)

# from socket import socket,SOCK_DGRAM
# sk = socket(type=SOCK_DGRAM)
# sk.bind(('127.0.0.1',9002))
#
# msg,client_addr = sk.recvfrom(n)
# sk.sendto(消息,client_addr)
#
# sk.close()


# udp-client
# import socket
# sk = socket.socket(type = socket.SOCK_DGRAM)
# sk.sendto(msg,('127.0.0.1',9002))
# msg,server_addr = sk.recvfrom(n)
# sk.close()

# socketserver
# import socketserver
#
# class Myserver(socketserver.BaseRequestHandler):
#     def handle(self):
#         conn = self.request
#
# server = socketserver.ThreadingTCPServer(Myserver,('127.0.0.1',9000))
# server.serve_forever()
