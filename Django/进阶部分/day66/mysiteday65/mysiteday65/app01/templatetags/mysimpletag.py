from django import template

register = template.Library()


@register.simple_tag(name="yimi")
def my_sum(arg1, arg2, arg3):
    return "{} {} {}".format(arg1, arg2, arg3)



@register.inclusion_tag('results.html')
def show_results(n):
    n = 1 if n < 1 else int(n)
    data = ["第{}项".format(i) for i in range(1, n+1)]
    return {"results": data}