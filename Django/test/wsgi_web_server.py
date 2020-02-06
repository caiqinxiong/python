# -*- coding:utf-8 -*-
# Author:caiqinxiong
from wsgiref.simple_server import make_server

def run_server(environ,star_response):
    '''
    :param environ: 请求相关内容，比如浏览器的类型，url，版本信息，来源地址等
    :param star_response: 相应相关内容
    :return: 
    '''

    star_response('200 ok',[('Conten-Type','text/html;charset=utf-8')])
    #return [bytes('李小欣，你好。',encoding='utf-8'),]
    return [bytes('李小欣，你好。',encoding='gbk')]

if __name__ == '__main__':
    httpd = make_server('localhost',8001,run_server)
    httpd.serve_forever() # 一直监听