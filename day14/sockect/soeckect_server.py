# -*- coding:utf-8 -*-
# Author:caiqinxiong
# web框架
import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world\n")
        print("#########")
        u = self.get_argument('user')
        p = self.get_argument('passwd')
        if u == 'caiqinxiong' and p == 'cai':
            self.write("登陆成功！！！")
        else:
            self.write("账号秘密不正确！")
        #self.write('GET')
    def post(self,*args,**kwargs):
        self.write("Hello,China!\n")
        print("@@@@@@@@@@@@@@")
        self.write('POST')

application = tornado.web.Application([
    (r"/index", MainHandler),
])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()