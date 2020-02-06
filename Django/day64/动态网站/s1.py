import socket

def f1(request):
    """
    处理用户请求，并返回相应的内容
    :param request: 用户请求的所有信息
    :return:
    """
    f = open('index.fsw','rb')
    data = f.read()
    f.close()
    return data

def f2(request):
    f = open('aricle.tpl','r',encoding='utf-8')
    data = f.read()
    f.close()
    import time
    ctime = time.time()
    data = data.replace('@@sw@@',str(ctime))
    return bytes(data,encoding='utf-8')

def f3(request):
    import pymysql

    # 创建连接
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='', db='db666')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute("select id,username,password from userinfo")
    user_list = cursor.fetchall()
    cursor.close()
    conn.close()

    content_list = []
    for row in user_list:
        tp = "<tr><td>%s</td><td>%s</td><td>%s</td></tr>" %(row['id'],row['username'],row['password'])
        content_list.append(tp)
    content = "".join(content_list)


    f = open('userlist.html','r',encoding='utf-8')
    template = f.read()
    f.close()

    # 模板渲染（模板+数据）
    data = template.replace('@@sdfsdffd@@',content)
    return bytes(data,encoding='utf-8')

def f4(request):
    import pymysql

    # 创建连接
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='', db='db666')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute("select id,username,password from userinfo")
    user_list = cursor.fetchall()
    cursor.close()
    conn.close()

    f = open('hostlist.html','r',encoding='utf-8')
    data = f.read()
    f.close()

    # 基于第三方工具实现的模板渲染
    from jinja2 import Template
    template = Template(data)
    data = template.render(xxxxx=user_list,user='sdfsdfsdf')
    return data.encode('utf-8')


routers = [
    ('/xxx', f1),
    ('/ooo', f2),
    ('/userlist.htm', f3),
    ('/host.html', f4),
]


def run():
    sock = socket.socket()
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(('127.0.0.1',8080))
    sock.listen(5)

    while True:
        conn,addr = sock.accept() # hang住
        # 有人来连接了
        # 获取用户发送的数据
        data = conn.recv(8096)
        data = str(data,encoding='utf-8')
        headers,bodys = data.split('\r\n\r\n')
        temp_list = headers.split('\r\n')
        method,url,protocal = temp_list[0].split(' ')
        conn.send(b"HTTP/1.1 200 OK\r\n\r\n")

        func_name = None
        for item in routers:
            if item[0] == url:
                func_name = item[1]
                break

        if func_name:
            response = func_name(data)
        else:
            response = b"404"

        conn.send(response)
        conn.close()

if __name__ == '__main__':
    run()