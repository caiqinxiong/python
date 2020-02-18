from django.shortcuts import render

# Create your views here.
from app01 import models


def books(request):
    # 从URL取参数
    page_num = request.GET.get("page")
    print(page_num, type(page_num))

    # 总数据是多少
    total_count = models.Book.objects.all().count()


    # # 每一页显示多少条数据
    # per_page = 10
    #
    # # 总共需要多少页码来展示
    # total_page, m = divmod(total_count, per_page)
    # if m:
    #     total_page += 1
    # try:
    #     page_num = int(page_num)
    #     # 如果输入的页码数超过了最大的页码数，默认返回最后一页
    #     if page_num > total_page:
    #         page_num = total_page
    # except Exception as e:
    #     # 当输入的页码不是正经数字的时候 默认返回第一页的数据
    #     page_num = 1
    #
    # # 定义两个变量保存数据从哪儿取到哪儿
    # data_start = (page_num-1)*10
    # data_end = page_num*10
    #
    # # 页面上总共展示多少页码
    # max_page = 11
    # if total_page < max_page:
    #     max_page = total_page
    #
    # half_max_page = max_page // 2
    # # 页面上展示的页码从哪儿开始
    # page_start = page_num - half_max_page
    # # 页面上展示的页码到哪儿结束
    # page_end = page_num + half_max_page
    # # 如果当前页减一半 比1还小
    # if page_start <= 1:
    #     page_start = 1
    #     page_end = max_page
    # # 如果 当前页 加 一半 比总页码数还大
    # if page_end >= total_page:
    #     page_end = total_page
    #     page_start = total_page - max_page +1
    #
    # all_book = models.Book.objects.all()[data_start:data_end]
    #
    # # 自己拼接分页的HTML代码
    # html_str_list = []
    # # 加上第一页
    # html_str_list.append('<li><a href="/books/?page=1">首页</a></li>')
    #
    # # 判断一下 如果是第一页，就没有上一页
    # if page_num <= 1:
    #     html_str_list.append('<li class="disabled"><a href="#"><span aria-hidden="true">&laquo;</span></a></li>'.format(page_num-1))
    # else:
    #     # 加一个上一页的标签
    #     html_str_list.append('<li><a href="/books/?page={}"><span aria-hidden="true">&laquo;</span></a></li>'.format(page_num-1))
    #
    # for i in range(page_start, page_end+1):
    #     # 如果是当前页就加一个active样式类
    #     if i == page_num:
    #         tmp = '<li class="active"><a href="/books/?page={0}">{0}</a></li>'.format(i)
    #     else:
    #         tmp = '<li><a href="/books/?page={0}">{0}</a></li>'.format(i)
    #
    #     html_str_list.append(tmp)
    #
    # # 加一个下一页的按钮
    # # 判断，如果是最后一页，就没有下一页
    # if page_num >= total_page:
    #     html_str_list.append('<li class="disabled"><a href="#"><span aria-hidden="true">&raquo;</span></a></li>')
    # else:
    #     html_str_list.append('<li><a href="/books/?page={}"><span aria-hidden="true">&raquo;</span></a></li>'.format(page_num+1))
    # # 加最后一页
    # html_str_list.append('<li><a href="/books/?page={}">尾页</a></li>'.format(total_page))
    #
    # page_html = "".join(html_str_list)
    #

    # 调用一个类
    from utils.mypage import Page
    page_obj = Page(page_num, total_count, per_page=10, url_prefix="/books/", max_page=9,)

    ret = models.Book.objects.all()[page_obj.start:page_obj.end]

    page_html = page_obj.page_html()


    return render(request, "books.html", {"books": ret, "page_html": page_html})



def depts(request):
    # 从URL取参数
    page_num = request.GET.get("page")
    print(page_num, type(page_num))
    # 总数据是多少
    total_count = models.Dept.objects.all().count()
    from utils.mypage import Page
    page_obj = Page(page_num, total_count, per_page=10, url_prefix="/depts/", max_page=11, )

    ret = models.Dept.objects.all()[page_obj.start:page_obj.end]
    print(ret)

    page_html = page_obj.page_html()
    return render(request, "dept.html", {"depts": ret, "page_html": page_html})
