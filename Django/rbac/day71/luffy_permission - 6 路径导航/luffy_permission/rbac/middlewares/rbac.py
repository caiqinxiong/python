from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import HttpResponse, redirect, reverse
from django.conf import settings
import re


class RbacMiddleWare(MiddlewareMixin):
    def process_request(self, request):
        # 获取当前访问的页面

        url = request.path_info  # index

        # setattr(request, settings.CURRENT_MENU_ID, None)
        # 当前访问的父权限的id
        request.current_menu_id = None

        # 路径导航的列表
        request.breadcrumb_list = [{'title': '首页', 'url': '/index/'}]

        # 白名单
        for i in settings.WHITE_LIST:
            if re.match(i, url):
                return
        # 获取登录状态
        is_login = request.session.get('is_login')
        # 没有登录跳转到登录页面
        if not is_login:
            return redirect(reverse('login'))

        # 免认证
        for i in settings.NO_PERMISSION_LIST:
            if re.match(i, url):
                return

        # 获取当前用户的权限
        permission_dict = request.session[settings.PERMISSION_SESSION_KEY]
        print(permission_dict)
        # 权限的校验
        for i in permission_dict.values():
            if re.match('^{}$'.format(i['url']), url):

                """
                {'url': '/customer/add/', 'id': 2, 'pid': 1}  子权限
                {'url': '/customer/list/', 'id': 1, 'pid': None}  父权限

                """
                pid = i.get('pid')
                id = i.get('id')

                if pid:
                    # 当前访问的是子权限
                    request.current_menu_id = pid
                    # setattr(request, settings.CURRENT_MENU_ID, pid)
                    parent = permission_dict[str(pid)]
                    request.breadcrumb_list.append({'url': parent['url'], 'title': parent['title']})


                else:
                    # 当前访问的是父权限
                    request.current_menu_id = id
                    # setattr(request, settings.CURRENT_MENU_ID, id)

                request.breadcrumb_list.append({'url': i['url'], 'title': i['title']})

                return

        # 没匹配成功  没有权限
        return HttpResponse('没有访问的权限')
