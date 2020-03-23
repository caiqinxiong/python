# -*- coding: utf-8 -*-
__author__ = 'caiqinxiong_cai'
#2020/3/20 14:42
from django.utils.deconstruct import deconstructible
from django.utils import timezone
from django.conf import settings
import os

@deconstructible
class PathAndRename(object):

    def __init__(self, sub_path):
        self.path = sub_path    # 要创建的文件夹名称

        self.full_path = "%s/%s" % (settings.MEDIA_ROOT, sub_path)  # 拼接 settings 中设置的根目录
        if not os.path.exists(self.full_path):  # 拼接的路径是否被创建
            os.makedirs(self.full_path)

    def __call__(self, instance, filename):
        ext = filename.split('.')[-1]
        t = timezone.now().strftime('%Y%m%d%H%M%S%f')

        if instance.pk:
            filename = '{}-{}.{}'.format(instance.pk, t, ext)
        else:
            filename = '{}.{}'.format(t, ext)
        return os.path.join(self.path , filename)