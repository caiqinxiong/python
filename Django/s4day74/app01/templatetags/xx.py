from django import template

register = template.Library()

@register.filter
def my_upper(value,arg):
    return value + arg
@register.filter
def my_bool(value):
    return False


@register.simple_tag
def my_lower(value,a1,a2,a3):

    return value + a1 + a2 + a3