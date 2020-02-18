"""
ORM小练习

如何在一个Python脚本或文件中 加载Django项目的配置和变量信息
"""

import os

if __name__ == '__main__':
    # 加载Django项目的配置信息
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ormday69.settings")
    # 导入Django，并启动Django项目
    import django
    django.setup()

    from app01 import models
    # # 查询所有的人
    # ret = models.Person.objects.all()
    # print(ret)
    # # get查询
    # ret = models.Person.objects.get(name="小黑")
    # print(ret)
    # # filter
    # ret = models.Person.objects.filter(id=100)  # 不存在返回一个空的QuerySet，不会报错
    # print(ret)
    # # 就算查询的结果只有一个，返回的也是QuerySet，我们要用索引的方式取出第一个元素
    # ret = models.Person.objects.filter(id=1)[0]
    # print(ret)
    # print("exclude".center(80, "*"))
    # # exclude
    # ret = models.Person.objects.exclude(id=1)
    # print(ret)
    # print("values".center(80, "*"))
    # # values 返回一个QuerySet对象，里面都是字典。 不写字段名，默认查询所有字段
    # ret = models.Person.objects.values("name", "birthday")
    # print(ret)
    # print("values_list".center(80, "*"))
    # # values_list 返回一个QuerySet对象，里面都是元祖。 不写字段名，默认查询所有字段
    # ret = models.Person.objects.values_list()
    # print(ret)
    # print("order_by".center(80, "*"))
    # # order_by 按照指定的字段排序
    # ret = models.Person.objects.all().order_by("birthday")
    # print(ret)
    # print("reverse".center(80, "*"))
    # # reverse 将一个有序的QuerySet 反转顺序
    # # 对有序的QuerySet才能调用reverse
    # ret = models.Person.objects.all().reverse()
    # print(ret)
    # print("count".center(80, "*"))
    # # count 返回QuerySet中对象的数量
    # ret = models.Person.objects.all().count()
    # print(ret)
    # print("first".center(80, "*"))
    # # first 返回QuerySet中第一个对象
    # ret = models.Person.objects.all().first()
    # print(ret)
    # print("last".center(80, "*"))
    # # last 返回QuerySet中最后一个对象
    # ret = models.Person.objects.all().last()
    # print(ret)
    # print("exists".center(80, "*"))
    # # exists 判断表里有没有数据
    # ret = models.Book.objects.exists()
    # print(ret)


    # 单表查询之神奇的双下划线
    # # 查询id值大于1小于4的结果
    # ret = models.Person.objects.filter(id__gt=1, id__lt=4)
    # print(ret)
    # # in
    # # 查询 id 在 [1, 3, 5, 7]中的结果
    # ret = models.Person.objects.filter(id__in=[1, 3, 5, 7])
    # print(ret)
    # ret = models.Person.objects.exclude(id__in=[1, 3, 5, 7])
    # print(ret)
    # # contains 字段包含指定值的
    # # icontains 忽略大小写包含指定值
    # ret = models.Person.objects.filter(name__contains="小")
    # print(ret)
    # # range
    # # 判断id值在 哪个区间的 SQL语句中的between and  1<= <=3
    # ret = models.Person.objects.filter(id__range=[1,3])
    # print(ret)
    # # 日期和时间字段还可以有以下写法
    # ret = models.Person.objects.filter(birthday__year=2000)
    # print(ret)
    # ret = models.Person.objects.filter(birthday__year=2000, birthday__month=5)
    # print(ret)


    # 外键的查询操作

    # 正向查询
    # 基于对象 跨表查询
    # book_obj = models.Book.objects.all().first()
    # ret = book_obj.publisher  # 和我这本书关联的出版社对象
    # print(ret, type(ret))
    # ret = book_obj.publisher.name  # 和我这本书关联的出版社对象
    # print(ret, type(ret))

    # 查询id是1的书的出版社的名称
    # 利用双下划线 跨表查询
    # 双下划线就表示跨了一张表
    # ret = models.Book.objects.filter(id=1).values_list("publisher__name")
    # print(ret)

    # 反向查询
    # 1. 基于对象查询
    # publisher_obj = models.Publisher.objects.get(id=1)  # 得到一个具体的对象
    # # ret = publisher_obj.book_set.all()
    # ret = publisher_obj.books.all()
    # print(ret)
    #
    # # 2. 基于双下划线
    # ret = models.Publisher.objects.filter(id=1).values_list("xxoo__title")
    # print(ret)

    # 多对多
    # 查询
    # author_obj = models.Author.objects.first()
    # print(author_obj.name)
    # 查询金老板写过的书
    # ret = author_obj.books.all()
    # print(author_obj.books, type(author_obj.books))
    # print(ret)
    # 1. create
    # 通过作者创建一本书,会自动保存
    # 做了两件事：
    # 1. 在book表里面创建一本新书，2. 在作者和书的关系表中添加关联记录
    # author_obj.books.create(title="金老板自传", publisher_id=2)
    # 2. add
    # 在金老板关联的书里面，再加一本id是4的书
    # book_obj = models.Book.objects.get(id=4)
    # author_obj.books.add(book_obj)
    # 添加多个
    # book_objs = models.Book.objects.filter(id__gt=5)
    # author_obj.books.add(*book_objs)  # 要把列表打散再传进去
    # 直接添加id
    # author_obj.books.add(9)


    # remove
    # 从金老板关联的书里面把 开飞船 删掉
    # book_obj = models.Book.objects.get(title="跟金老板学开飞船")
    # author_obj.books.remove(book_obj)
    # 从金老板关联的书里面把 id是8的记录 删掉
    # author_obj.books.remove(8)

    # clear
    # 清空
    # 把景女神 关联的所有书都删掉
    # jing_obj = models.Author.objects.get(id=2)
    # jing_obj.books.clear()


    # 额外补充的，外键的反向操作

    # 找到id是1的出版社
    # publisher_obj = models.Publisher.objects.get(id=2)
    # publisher_obj.books.clear()

    # 聚合
    from django.db.models import Avg, Sum, Max, Min, Count
    # ret = models.Book.objects.all().aggregate(price_avg=Avg("price"))
    # print(ret)
    #
    # ret = models.Book.objects.all().aggregate(price_avg=Avg("price"), price_max=Max("price"), price_min=Min("price"))
    # print(ret)
    # print(ret.get("price_max"), type(ret.get("price_max")))

    # 分组查询

    # 查询每一本书的作者个数
    # ret = models.Book.objects.all().annotate(author_num=Count("author"))
    # # print(ret)
    # for book in ret:
    #     print("书名：{}，作者数量：{}".format(book.title, book.author_num))

    # 查询作者数量大于1的书
    # ret = models.Book.objects.all().annotate(author_num=Count("author")).filter(author_num__gt=1)
    # print(ret)

    # 查询各个作者出的书的总价格
    # ret = models.Author.objects.all().annotate(price_sum=Sum("books__price")).values_list("name", "price_sum")
    # ret = models.Author.objects.all().annotate(price_sum=Sum("books__price"))
    # print(ret)
    # for i in ret:
    #     print(i, i.name, i.price_sum)
    # print(ret.values_list("id", "name", "price_sum"))

    # F和Q
    # ret = models.Book.objects.filter(price__gt=9.99)
    # print(ret)

    # 查询出 库存数 大于 卖出数的 所有书（两个字段做比较）
    from django.db.models import F
    # ret = models.Book.objects.filter(kucun__gt=F("maichu"))
    # print(ret)
    # 刷单 把每一本书的卖出数都乘以3
    # obj = models.Book.objects.first()
    # obj.maichu = 1000 * 3
    # obj.save()
    # 具体的对象没有update()，QuerySet对象才有update()方法。

    # models.Book.objects.update(maichu=(F("maichu")+1)*3)

    # 给每一本书的书名后面加上 第一版
    # from django.db.models.functions import Concat
    # from django.db.models import Value
    #
    # models.Book.objects.update(title=Concat(F("title"), Value("第一版")))


    # Q查询
    from django.db.models import Q
    # 查询 卖出数大于1000，并且 价格小于100的所有书
    # ret = models.Book.objects.filter(maichu__gt=1000, price__lt=100)
    # print(ret)
    # 查询 卖出数大于1000，或者 价格小于100的所有书
    # ret = models.Book.objects.filter(Q(maichu__gt=1000) | Q(price__lt=100))
    # print(ret)
    # Q查询和字段查询同时存在时， 字段查询要放在Q查询的后面
    # ret = models.Book.objects.filter(Q(maichu__gt=1000) | Q(price__lt=100), title__contains="金老板")
    # print(ret)


    # Django ORM 事务

    # try:
    #     from django.db import transaction
    #
    #     with transaction.atomic():
    #         # 先创建一个出版社
    #         new_publisher = models.Publisher.objects.create(name="火星出版社")
    #         # 创建一本书
    #         models.Book.objects.create(
    #             title="橘子物语",
    #             price=11.11,
    #             kucun=10,
    #             maichu=10,
    #             publisher_id=1000  # 指定一个不存在的出版社id
    #         )
    # except Exception as e:
    #     print(str(e))

    # 没有指定原子操作
    # try:
    #
    #     # 先创建一个出版社
    #     new_publisher = models.Publisher.objects.create(name="火星出版社")
    #     # 创建一本书
    #     models.Book.objects.create(
    #         title="橘子物语",
    #         price=11.11,
    #         kucun=10,
    #         maichu=10,
    #         publisher_id=1000  # 指定一个不存在的出版社id
    #     )
    # except Exception as e:
    #     print(str(e))

    # 执行原生SQL
    # 更高灵活度的方式执行原生SQL语句
    # from django.db import connection
    # cursor = connection.cursor()  # cursor = connections['default'].cursor()
    # cursor.execute("SELECT * from app01_book where id = %s", [1])
    # ret = cursor.fetchone()
    # print(ret)


    # 在QuerSet查询的基础上自己指定其他的SQL语句(了解即可)
    ret = models.Book.objects.extra(
        # 把出版社计数 赋值给newid
        select={'newid': 'select count(1) from app01_publisher where id>%s'},
        select_params=[1, ],

        where=["app01_book.id=%s"],

        params=[1, ],
        tables=['app01_publisher']
    )

    print(ret)
    for i in ret:
        print(i)


