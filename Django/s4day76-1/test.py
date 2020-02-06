#!/usr/bin/env python
#coding:utf-8
from wsgiref.simple_server import make_server
from views import account


def RunServer(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    url = environ['PATH_INFO']
    urlpatterns = (
        ('/index/',account.index),
        ('/login/',account.login),
    )
    func = None
    for item in urlpatterns:
        if item[0] == url:
            func = item[1]
            break
    if func:
        return func()
    else:
        return [b'404 not found',]
     
if __name__ == '__main__':
    httpd = make_server('', 8000, RunServer)
    httpd.serve_forever()