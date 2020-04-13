from django.utils.deprecation import MiddlewareMixin
from web import models
import datetime
from django.shortcuts import redirect
from django.conf import settings


class Tracer(object):

    def __init__(self):
        self.user = None
        self.price_policy = None


class AuthMiddleware(MiddlewareMixin):

    def process_request(self, request):

        """ 如果用户已登录，则request中赋值 """
        request.tracer = Tracer()
        user_id = request.session.get('user_id', 0)
        user_object = models.UserInfo.objects.filter(id=user_id).first()
        request.tracer.user = user_object

        if request.path_info in settings.WHITE_REGEX_URL_LIST:
            return  #直接通过校验

        if not request.tracer.user:
            return redirect("login")
        _object = models.Transaction.objects.filter(user=user_object,status=2).order_by('-id').first()
        current_datetime = datetime.datetime.now()
        if _object.end_time and _object.end_time < current_datetime:
            _object = models.Transaction.objects.filter(user=user_object,status=2,price_policy__category=1).first()
        request.tracer.price_policy = _object.price_policy

    def process_view(self,request,view,args,kwargs):
        if not request.path_info.startswith('/manage/'):
            return

        project_id = kwargs.get('project_id')
        # 是否是我创建的
        project_object = models.Project.objects.filter(creator=request.tracer.user, id=project_id).first()
        if project_object:
            # 是我创建的项目的话，我就让他通过
            request.tracer.project = project_object
            return

        # 是否是我参与的项目
        project_user_object = models.ProjectUser.objects.filter(user=request.tracer.user, project_id=project_id).first()
        if project_user_object:
            # 是我参与的项目
            request.tracer.project = project_user_object.project
            return

        return redirect('project_list')
