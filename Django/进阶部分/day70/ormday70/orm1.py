import os
import sys


if __name__ == '__main__':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ormday70.settings")
    import django
    django.setup()

    from app01 import models

    # 一对一的查询
    # author_obj = models.Author.objects.get(id=1)
    # obj = author_obj.detail
    # print(obj.hobby, obj.addr)

    # 在app01 里面 查询 id是1的作者关联的书
    from app01 import models
    ret = models.Author.objects.get(id=1).books.all()

    # 从作者关联的书里面移除id是1的书
    models.Author.objects.get(id=1).books.remove(1)
    print(ret)
    print("app01".center(80, "-"))
    # 在app02 里面 查询 id是1的作者关联的书
    from app02 import models

    ret = models.Author2Book.objects.filter(author_id=1).values_list("book_id")
    # id是1的作者关联的书的id
    print(ret)
    ret = [i[0] for i in ret]
    # 查书这张表
    ret = models.Book.objects.filter(id__in=ret)
    print(ret)
    print("app03".center(80, "-"))
    # 在app03 里面 查询 id是1的作者关联的书
    from app03 import models
    ret = models.Author.objects.get(id=1).books.all()
    print(ret)
    # 从作者关联的书里面移除id是1的书
    # 没有django ORM 封装的那些快捷方式了，我们要自己亲自改第三张表
    models.Author2Book.objects.get(author_id=1, book_id=1).delete()
