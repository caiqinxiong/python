from django.utils.deprecation import MiddlewareMixin

from django.shortcuts import HttpResponse
class Middle1(MiddlewareMixin):
    def process_request(self, request):
        print('m1.process_request')
        # return HttpResponse('不要在往下周了')

    def process_response(self, request, response):
        print('m1.process_response')
        return response

class Middle2(MiddlewareMixin):
    def process_request(self, request):
        print('m2.process_request')
        # return HttpResponse('不要在往下周了')

    def process_response(self, request, response):
        print('m2.process_response')
        return response