"""
不完善的web服务端示例
"""

import socket

# 生成socket实例对象
sk = socket.socket()
# 绑定IP和端口
sk.bind(("127.0.0.1", 8001))
# 监听
sk.listen()

# 写一个死循环,一直等待客户端来连我
while 1:
    # 获取与客户端的连接
    conn, _ = sk.accept()
    # 接收客户端发来消息
    data = conn.recv(8096)
    print(data)
    # 给客户端回复消息
    conn.send(b'<h1>hello s10!</h1>')
    # 关闭
    conn.close()
    sk.close()
