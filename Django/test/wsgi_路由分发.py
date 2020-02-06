# -*- coding:utf-8 -*-
# Author:caiqinxiong
from wsgiref.simple_server import make_server

def book(environ,star_response):
    star_response('200 ok', [('Conten-Type', 'text/html;charset=utf-8')])
    return [bytes('书城页面！',encoding='gbk')]

def cloth(environ,star_response):
    star_response('200 ok', [('Conten-Type', 'text/html;charset=utf-8')])
    return [bytes('衣服购买！',encoding='gbk')]

def routers():
    '''
    路由分发
    :return: 
    '''
    urls = {
        "/book":book,
        "/cloth":cloth,
    }
    return urls

def run_server(environ,star_response):
    '''
    :param environ: 请求相关内容，比如浏览器的类型，url，版本信息，来源地址等
    :param star_response: 相应相关内容
    :return: 
    '''

    # star_response('200 ok',[('Conten-Type','text/html;charset=utf-8')])
    # #return [bytes('李小欣，你好。',encoding='utf-8'),]
    # return [bytes('李小欣，你好。',encoding='gbk')]
    url_list = routers()
    url = environ.get('PATH_INFO')
    if url in url_list:
        func_data = url_list[url](environ,star_response)
        return func_data
    else:
        star_response('404 ok', [('Conten-Type', 'text/html;charset=utf-8')])
        return  [bytes('页面不存在！！',encoding='gbk')]

if __name__ == '__main__':
    httpd = make_server('localhost',8001,run_server)
    httpd.serve_forever() # 一直监听