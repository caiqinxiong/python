import os
import sys


if __name__ == '__main__':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ormday71.settings")
    import django
    django.setup()

    from app01 import models

    # ret = models.Employee.objects.all().values("id", "dept")
    # print(ret)

    from django.db.models import Avg
    # ret = models.Employee.objects.values("dept").annotate(avg=Avg("salary")).values("dept","avg")
    # print(ret)

    # ret = models.Employee2.objects.values("dept_id").annotate(avg=Avg("salary")).values("dept__name","avg")
    # print(ret)

    # 查所有的员工和部门名称
    # ret = models.Employee2.objects.values("name", "dept__name")
    # print(ret)
    #
    # ret = models.Employee2.objects.select_related().values("name", "dept__name")
    # print(ret)
    #
    # ret = models.Author.objects.select_related("books__title").values("name", "books__title")
    # print(ret)
    # print("=" * 120)
    # ret = models.Author.objects.prefetch_related("books__title").values("name", "books__title")
    # print(ret)


    # 批量创建
    # 有100个书籍对象
    objs = [models.Book(title="沙河{}".format(i)) for i in range(1500)]

    # 在数据库中批量创建, 10次一提交
    models.Book.objects.bulk_create(objs, 10)

    # models.Book.objects.all().delete()