
import django
import os
import sys

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_dir)
os.environ.setdefault("DJANGO_SETTINGS_MODULE","tracer.settings")
django.setup()

from web import models
models.UserInfo.objects.create(username='alex',email='1.qq.com',mobile_phone='15200000000',password='12345')