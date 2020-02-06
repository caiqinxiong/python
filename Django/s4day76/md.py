from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import HttpResponse
class M1(MiddlewareMixin):
    def process_request(self,request):
        print('m1.process_request')

    def process_view(self, request, callback, callback_args, callback_kwargs):
        print('m1.process_view')
        # response = callback(request,*callback_args,**callback_kwargs)
        # return response

    def process_response(self,request,response):
        print('m1.process_response')
        return response

    def process_exception(self, request, exception):
        print('m1.process_exception')

    def process_template_response(self,request,response):
        """
        视图函数的返回值中，如果有render方法，才被调用
        :param request:
        :param response:
        :return:
        """
        print('m1.process_template_response')
        return response

class M2(MiddlewareMixin):
    def process_request(self,request):
        print('m2.process_request')
    def process_view(self, request, callback, callback_args, callback_kwargs):
        print('m2.process_view')
    def process_response(self,request,response):
        print('m2.process_response')
        return response
    def process_exception(self, request, exception):
        print('m2.process_exception')
        return HttpResponse('错误了...')