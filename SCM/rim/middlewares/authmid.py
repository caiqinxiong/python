# -*- coding: utf-8 -*-
__author__ = 'caiqinxiong_cai'
#2020/2/26 15:48
import re
from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import render, redirect, HttpResponse


class AuthMD(MiddlewareMixin):  # 验证登录
    white_list = ['/rim/login/','/rim/logout/','/admin/.*', '/xadmin/.*', '/rim/project_list/' ]  # 白名单
    black_list = ['/black/', ]  # 黑名单
    ret = {"status": 0, 'url': '', 'msg': ''}  # 默认状态
    def process_request(self, request):
        # 1. 当前请求URL
        current_request_url = request.path_info

        # 2. 处理白名单,如login及admin页面需开放访问权限，根据实际情况而定
        for url in self.white_list:
            if re.match(url, current_request_url):
                return None

        # 3. 获取session中保存的权限信息
        permission_list = request.session.get("permission_url_list")
        if not permission_list and not request.session.get("email"):
            # 登陆页面
            # return redirect('/rim/login/')
            self.ret['msg'] = "请登录后,再访问!"
            self.ret['url'] = "/rim/login/?next={}".format(current_request_url)
            return render(request, "jump.html", self.ret)

        flag = False
        for db_url in permission_list:
            # print(db_url)
            regax = "^{0}$".format(db_url['permission__url'])
            if re.match(regax, current_request_url):
                flag = True
                break
        if not flag:
            # 无权访问页面，可以直接redirect
            return render(request,'permissionDenied.html')