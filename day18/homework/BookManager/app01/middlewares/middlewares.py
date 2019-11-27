from django.utils.deprecation import MiddlewareMixin


class AuthMD(MiddlewareMixin):
    white_list = ['/login/', ]  # 白名单
    black_list = ['/black/', ]  # 黑名单

    def process_request(self, request):
        from django.shortcuts import redirect, HttpResponse

        next_url = request.path_info
        print(request.path_info, request.get_full_path())
        # 黑名单的网址限制访问
        if next_url in self.black_list:
            return HttpResponse('This is an illegal URL')
        # 白名单的网址或者登陆用户不做限制
        elif next_url in self.white_list or request.session.get("user"):
            return
        else:
            return redirect("/login/?return={}".format(next_url))
        