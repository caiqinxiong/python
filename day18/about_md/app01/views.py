from django.shortcuts import render, HttpResponse
from django.template.response import TemplateResponse


# Create your views here.
def index(request):
    print('index')
    # print(request, id(request))
    # int('asd')
    # return HttpResponse('index')
    return TemplateResponse(request, 'index.html', {'name': 'alex', 'age': '84'})
