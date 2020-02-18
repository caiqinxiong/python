"""
完善的web服务端示例
根据不同的路径返回不同的内容
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
    # 把收到的数据转成字符串类型
    data_str = str(data, encoding="utf-8")  # bytes("str", enconding="utf-8")
    # print(data_str)
    # 用\r\n去切割上面的字符串
    l1 = data_str.split("\r\n")
    # print(l1[0])
    # 按照空格切割上面的字符串
    l2 = l1[0].split()
    url = l2[1]
    # 给客户端回复消息
    conn.send(b'http/1.1 200 OK\r\ncontent-type:text/html; charset=utf-8\r\n\r\n')
    # 想让浏览器在页面上显示出来的内容都是响应正文

    # 根据不同的url返回不同的内容
    if url == "/yimi/":
        response = b'<h1>hello yimi!</h1>'
    elif url == "/xiaohei/":
        response = b'<h1>hello xiaohei!</h1>'
    else:
        response = b'<h1>404! not found!</h1>'
    conn.send(response)
    # 关闭
    conn.close()
    sk.close()
