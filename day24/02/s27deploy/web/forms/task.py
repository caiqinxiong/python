# -*- coding:utf-8 -*-
# caiqinxiong 
# 2020/1/5 下午4:40
import datetime
from web import models
from .base import BootStrapModelForm

class TaskModelForm(BootStrapModelForm):
    class Meta:
        model = models.DeployTask
        # fields = "__all__"
        exclude = ['uid', 'project', 'status']

    def __init__(self, project_object, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.project_object = project_object

    def save(self, commit=True):
        self.instance.uid = self.create_uid()
        self.instance.project_id = self.project_object.id
        super().save(commit)

    def create_uid(self):
        title = self.project_object.title
        env = self.project_object.env
        tag = self.cleaned_data.get('tag')
        date = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
        return '{0}-{1}-{2}-{3}'.format(title,env,tag,date)