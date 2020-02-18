from django import template

# 生成一个注册的实例，必须写成是register
register = template.Library()


@register.inclusion_tag("ul.html")
def show_ul(num):
    num = 1 if num < 1 else int(num)
    data = ["第{:0>3}号技师".format(i) for i in range(1, num+1)]
    return {"data": data}
