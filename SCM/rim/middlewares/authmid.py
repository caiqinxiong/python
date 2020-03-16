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

    # def process_request(self, request):  # 请求之前
    #     flag = False
    #     request_url = request.path_info  # 获取请求路径
    #     # get_full_path()表示带参数的路径
    #     # print(request.path_info, request.get_full_path())
    #     # 黑名单的网址限制访问
    #     if request_url in self.black_list:
    #         self.ret['msg'] = "这是非法请求"
    #         self.ret['url'] = "/rim/login/"
    #     # 白名单的网址或者登陆用户不做限制
    #     # 判断是否在白名单内或者已经有了session(表示已经登录了)
    #     elif request_url in self.white_list or request.session.get("email"):
    #         flag = True
    #     else:
    #         self.ret['msg'] = "请登录后,再访问!"
    #         self.ret['url'] = "/rim/login/?next={}".format(request_url)
    #
    #     print(request.path_info, request.get_full_path())
    #     print(self.ret)
    #
    #     permission_list = request.session.get("permission_url_list")
    #     print(permission_list)
    #
    #     for db_url in permission_list:
    #         print(db_url)
    #         regax = "^{0}$".format(db_url['permission__url'])
    #         if re.match(regax, request_url):
    #             flag = True
    #             return None
    #
    #     if not flag:
    #         return HttpResponse('无权访问')
    #
    #     # 错误页面提示
    #     # return render(request, "jump.html", self.ret)

    def process_request(self, request):
        # 1. 当前请求URL
        current_request_url = request.path_info

        # 2. 处理白名单,如login及admin页面需开放访问权限，根据实际情况而定
        for url in self.white_list:
            if re.match(url, current_request_url):
                return None

        # 3. 获取session中保存的权限信息
        permission_list = request.session.get("permission_url_list")
        if not permission_list:
            # 登陆页面
            return redirect('/rim/login/')

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