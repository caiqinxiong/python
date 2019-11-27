import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bookmanager.settings")

import django

django.setup()

from app01 import models

from django.db import transaction

try:
    with transaction.atomic():

        # 一系列的操作
            models.Publisher.objects.create(name='小强')
            models.Publisher.objects.create(name='小强')
            models.Publisher.objects.create(name='小强出版社')
            models.Publisher.objects.create(name='小强出版社')
            models.Publisher.objects.create(name='小强出版社')
            models.Publisher.objects.create(name='小强出版社')
except Exception as e :
    print(e)
print('xxxx')
