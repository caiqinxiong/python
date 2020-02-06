from django.db import models

class UserInfo(models.Model):
    nickname = models.CharField(max_length=32)
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=64)
    gender_choices = (
        (1,'男'),
        (2,'女'),
    )
    gender = models.IntegerField(choices=gender_choices)

    m = models.ManyToManyField('UserInfo')

"""
1  女
2  女
3  女
4  男
5  男
a1 = 2
a2 = 5
"""
# related_query_name
# obj对象男.b_set.all()
# obj对象女.a_set.all()
# related_name
# obj对象男.a.all()
# obj对象女.b.all()
# class U2U(models.Model):
#     g = models.ForeignKey('UserInfo',related_name='boys')
#     b = models.ForeignKey('UserInfo',related_name='girls')

# U2U.objects.create(g_id=a1,b_id=a2)
# related_query_name，related_name



# class UserType(models.Model):
#     title = models.CharField(max_length=32)
#
# class User(models.Model):
#     username = models.CharField(max_length=32)
#     ut = models.ForeignKey('UserType',related_query_name='xxxx')

# 反向：
# related_name='xxxx'
#   user_set ==> xxxx
# related_query_name='xxxx'
#   user_set ==> xxxx_set



# FK自关联

class Comment(models.Model):
    """
    评论表
    """
    news_id = models.IntegerField()            # 新闻ID
    content = models.CharField(max_length=32)  # 评论内容
    user = models.CharField(max_length=32)     # 评论者
    reply = models.ForeignKey('Comment',null=True,blank=True,related_name='xxxx')
"""
   新闻ID                         reply_id
1   1        别比比    root         null
2   1        就比比    root         null
3   1        瞎比比    shaowei      null
4   2        写的正好  root         null
5   1        拉倒吧    由清滨         2
6   1        拉倒吧1    xxxxx         2
7   1        拉倒吧2    xxxxx         5
"""
"""
新闻1
    别比比
    就比比
        - 拉倒吧
            - 拉倒吧2
        - 拉倒吧1
    瞎比比
新闻2：
    写的正好
"""















