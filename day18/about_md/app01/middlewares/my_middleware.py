from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import HttpResponse


class MD1(MiddlewareMixin):
    def process_request(self, request):
        # print(request,id(request))
        print('MD1 process_request')
        # return HttpResponse('md1')

    def process_response(self, request, response):
        print('MD1 process_response')
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        # print(view_func)
        # print(view_args)
        # print(view_kwargs)

        print('MD1 process_view')
        # return HttpResponse('md1 process_view')

    def process_exception(self, request, exception):
        # print(exception)
        print('MD1 process_exception')

    def process_template_response(self,request,response):

        print('MD1 process_template_response')
        response.template_name = 'index1.html'
        response.context_data['age'] = 1000

        # self.template_name = template
        #  self.context_data = context
        return response

class MD2(MiddlewareMixin):
    def process_request(self, request):
        print('MD2 process_request')

    def process_response(self, request, response):
        print('MD2 process_response')
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        print('MD2 process_view')

    def process_exception(self, request, exception):
        # print(exception)
        print('MD2 process_exception')
        # return HttpResponse('111')
