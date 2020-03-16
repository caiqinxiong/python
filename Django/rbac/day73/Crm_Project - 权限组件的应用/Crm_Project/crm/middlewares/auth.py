from django.utils.deprecation import MiddlewareMixin
from crm import models
from django.shortcuts import redirect, reverse


class AuthMiddleware(MiddlewareMixin):

    def process_request(self, request):

        if request.path_info in [reverse('login'), reverse('reg')]:
            return

        if request.path_info.startswith('/admin/'):
            return

        pk = request.session.get('pk')

        user = models.UserProfile.objects.filter(pk=pk).first()
        # 没有登录 跳转至登录页面
        if not user:
            return redirect(reverse('login'))

        request.user_obj = user
