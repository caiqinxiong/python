import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bookmanager.settings")

import django

django.setup()

from app01 import models

from django.db.models import F, Q

# ret = models.Book.objects.filter(sale__gt=F('kucun'))

# ret = models.Book.objects.update(sale=F('sale')*2+5)


ret = models.Book.objects.filter(Q(Q(~Q(pk__gte=3) | Q(pk__lte=2)) & Q(title__contains='小强')))

# Q(pk__gte=3) | Q(pk__lte=2)  或
# Q(pk__gte=3) & Q(pk__lte=2)  与
# ~Q(pk__gte=3)   非
ret = models.Book.objects.filter(Q(('pk__lte', 3)))
ret = models.Book.objects.filter(Q(pk__lte=3))

field_name = 'pk'
# Q(('pk__lte',3))    Q(pk__lte=3)
ret = models.Book.objects.filter(Q(('{}__lte'.format(field_name), 3)))

print(ret)
