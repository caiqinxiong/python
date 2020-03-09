from django.shortcuts import render
from django.views import View
from django.http import JsonResponse, HttpResponse

from .db_config import DB_helper
from .authority import menu_filter


def getJson(request):
    """
    后台表格所需数据
    """
    dbheper = DB_helper()

    ProductName = request.GET.get('Name', None)
    Splug_insrtTime = request.GET.get('Splug_insrtTime', None)
    EndTime = request.GET.get('EndTime', None)
    NowTime = request.GET.get('NowTime', None)
    Path = request.GET.get('Path', None)

    if Path == '/xadmin/plug_ins/menu1/':
        massages = dbheper.select_menu_1(ProductName, Splug_insrtTime, EndTime, NowTime)
        keys = ['date', 'productname', 'stunum', 'grade']

    elif Path == '/xadmin/plug_ins/menu2/':
        massages = dbheper.select_menu_2(ProductName, Splug_insrtTime, EndTime, NowTime)
        keys = ['date', 'productname', 'stunum', 'grade']

    elif Path == '/xadmin/plug_ins/menu2/':
        massages = dbheper.select_menu_3(ProductName, Splug_insrtTime, EndTime, NowTime)
        keys = ['date', 'productname', 'stunum', 'grade']

    list_json = [dict(zip(keys, item)) for item in massages]
    res = {}
    res['rows'] = list_json

    return JsonResponse(res, safe=False)


class MenuOneXadminView(View):
    """
        功能一
    """

    def get(self, request):
        menu_authorities = menu_filter(request)
        menu = {
            'menus': [],
        }
        for menu_authority in menu_authorities['menus']:
            menu['menus'].append({
                'name': menu_authority['id'],
                'url': menu_authority['url']
            })

        # url权限过滤
        ids = [id['id'] for id in menu_authorities['menus']]
        # 无权限则跳转到首页
        if str(request.path).split('/')[-2] not in ids:
            return HttpResponse('<br/><br/><br/><center><h1>对不起，您无权访问该页面！</h1></center>')

        return render(request, 'plug_ins/menu1.html', {'menus': menu['menus']})


class MenuTwoXadminView(View):
    """
        功能二
    """

    def get(self, request):
        menu_authorities = menu_filter(request)
        menu = {
            'menus': [],
        }
        for menu_authority in menu_authorities['menus']:
            menu['menus'].append({
                'name': menu_authority['id'],
                'url': menu_authority['url']
            })

        # url权限过滤
        ids = [id['id'] for id in menu_authorities['menus']]
        # 无权限则跳转到首页
        if str(request.path).split('/')[-2] not in ids:
            return HttpResponse('<br/><br/><br/><center><h1>对不起，您无权访问该页面！</h1></center>')

        return render(request, 'plug_ins/menu2.html', {'menus': menu['menus']})


class MenuTheXadminView(View):
    """
        功能三
    """

    def get(self, request):
        menu_authorities = menu_filter(request)
        menu = {
            'menus': [],
        }
        for menu_authority in menu_authorities['menus']:
            menu['menus'].append({
                'name': menu_authority['id'],
                'url': menu_authority['url']
            })

        # url权限过滤
        ids = [id['id'] for id in menu_authorities['menus']]
        # 无权限则跳转到首页
        if str(request.path).split('/')[-2] not in ids:
            return HttpResponse('<br/><br/><br/><center><h1>对不起，您无权访问该页面！</h1></center>')

        return render(request, 'plug_ins/menu3.html', {'menus': menu['menus']})
