from django.shortcuts import HttpResponse, redirect

"""
自定义的中间件
"""
from django.utils.deprecation import MiddlewareMixin

# 定义一个可以访问的白名单
URL = ["/oo/", "/xx/", "/haha/"]

class OoXx(MiddlewareMixin):

    # def process_request(self, request):
    #     print("这是我的第一个中间件：OoXx！")
    #     print(id(request))
    #     # print(request.path_info)
    #     # # 如果用户访问的URL 在 白名单里面
    #     # if request.path_info in URL:
    #     #     return
    #     # # 否则 直接返回一个 响应 不走视图那部分了
    #     # else:
    #     #     return HttpResponse("gun!")
    #
    # def process_response(self, request, response):
    #     """
    #     :param request: 是浏览器发来的请求对象
    #     :param response: 是视图函数返回的响应对象
    #     :return:
    #     """
    #     print("这是OOXX中间件里面的 process_response")
    #     # return response
    #     return HttpResponse("hahahaha")
    #
    # def process_view(self, request, view_func, view_args, view_kwargs):
    #     """
    #
    #     :param request: 浏览器发来的请求对象
    #     :param view_func: 将要执行的视图函数的名字
    #     :param view_args: 将要执行的视图函数的位置参数
    #     :param view_kwargs: 将要执行的视图函数的关键字参数
    #     :return:
    #     """
    #     print("ooxx里面的process_view")
    #     print(view_func, type(view_func))
    #     return HttpResponse("ooxx：process_view")


    # def process_exception(self, request, exception):
    #     print(exception)
    #     print("ooxx里面的process_exception")
    #     return redirect("http://www.luffycity.com")

    # def process_template_response(self, request, response):
    #     print("ooxx 中的process_template_response")
    #     return response

    def process_request(self, request):
       request.s10 = {"is_login": 1, "name": "s10"}



class MD2(MiddlewareMixin):

    # def process_request(self, request):
    #     print("这是我的第二个中间件：MD2！")
    #     print(id(request))
    #
    # def process_response(self, request, response):
    #     print("这是MD2中间件里面的 process_response")
    #     return response
    #
    # def process_view(self, request, view_func, view_args, view_kwargs):
    #     print("MD2里面的process_view")
    #     print(view_func, type(view_func))
    #     return HttpResponse("md2：process_view")

    # def process_exception(self, request, exception):
    #     print(exception)
    #     print("MD2里面的process_exception")

    # def process_template_response(self, request, response):
    #     print("MD2 中的process_template_response")
    #     return response


    def process_request(self, request):
       print(request.s10.get("is_login"))