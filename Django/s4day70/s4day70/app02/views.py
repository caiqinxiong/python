from django.shortcuts import render,HttpResponse

def index(request):

    return HttpResponse('app02.index')
