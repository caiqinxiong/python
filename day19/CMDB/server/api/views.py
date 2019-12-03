from django.shortcuts import render
from django.http.response import JsonResponse

# Create your views here.
from django.views.decorators.csrf import csrf_exempt, csrf_protect
import json

@csrf_exempt
def asset(request):
    print(request.POST)
    data = json.loads(request.body.decode('utf-8'))
    print(data,type(data))
    return JsonResponse({'status': '200'})
