from django.shortcuts import render,HttpResponse
from app01 import models
# Create your views here.

# def test(request):
#     # models.U2U.objects.create(b_id=2,g_id=6)
#     # models.U2U.objects.create(b_id=1,g_id=6)
#     # models.U2U.objects.create(b_id=1,g_id=4)
#     # models.U2U.objects.create(b_id=1,g_id=5)
#
#     # boy = models.UserInfo.objects.filter(gender=1,id=2).first()
#     # girl = models.UserInfo.objects.filter(gender=2,id=6).first()
#     # models.U2U.objects.create(b=boy,g=girl)
#
#     # UserInfo对象
#     # xz = models.UserInfo.objects.filter(id=1).first()
#     # # 和徐峥有关系的所有信息：U2U列表[U2U对象，2U对象，2U对象，]
#     # result = xz.girls.all()
#     # for u in result:
#     #     # U2U对象
#     #     print(u.g.nickname)
#
#     # 查男生
#     # xz = models.UserInfo.objects.filter(id=1).first()
#     # u = xz.m.all()
#     # for row in u:
#     #     print(row.nickname)
#     # 查女神
#     # xz = models.UserInfo.objects.filter(id=4).first()
#     # v = xz.userinfo_set.all()
#     # for row in v:
#     #     print(row.nickname)
#     return HttpResponse('...')


def test(request):
    print('执行视图函数')
    return HttpResponse('...')