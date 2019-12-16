from django.shortcuts import render
from django.http.response import JsonResponse

# Create your views here.
from django.views.decorators.csrf import csrf_exempt, csrf_protect
import json


@csrf_exempt
def asset(request):
    print(request.POST)
    data = json.loads(request.body.decode('utf-8'))
    print(data, type(data))
    return JsonResponse({'status': '200'})


from django.views import View
from django.utils.decorators import method_decorator


@method_decorator(csrf_exempt, name='dispatch')
class Asset(View):
    def post(self, request):
        print(request.POST)
        data = json.loads(request.body.decode('utf-8'))
        print(data, type(data))
        return JsonResponse({'status': '200'})


from rest_framework.views import APIView
from rest_framework.response import Response
from repository import models
import datetime
from django.db.models import Q


class Asset(APIView):

    def get(self, request):
        now = datetime.datetime.now()
        host_list = models.Server.objects.filter(Q(latest_date__lt=now) | Q(latest_date__isnull=True)).values(
            'hostname')
        # print(host_list)
        return Response(host_list)

    def post(self, request):
        # print(request.POST)
        # data = json.loads(request.body.decode('utf-8'))
        # print(data, type(data))

        info = request.data
        action = info['action']
        hostname = info['basic']['data']['hostname']

        if action == 'update':
            # 只更新硬件信息

            # 更新 主板 + cpu + 基本信息
            server_list = models.Server.objects.filter(hostname=hostname)
            # now = datetime.datetime.now()
            server_list.update(**info['basic']['data'], **info['cpu']['data'], **info['main_board']['data'],
                               )
            from api.service import process_memory, process_disk, process_nic
            process_memory(info, server_list)
            process_disk(info, server_list)
            process_nic(info, server_list)

        elif action == 'host_update':
            cert = info['cert']
            # 更新 主板 + cpu + 基本信息
            server_list = models.Server.objects.filter(hostname=cert)
            # now = datetime.datetime.now()
            server_list.update(**info['basic']['data'], **info['cpu']['data'], **info['main_board']['data'],
                               )
            from api.service import process_memory, process_disk, process_nic
            process_memory(info, server_list)
            process_disk(info, server_list)
            process_nic(info, server_list)



        return Response({'status': '200'})
