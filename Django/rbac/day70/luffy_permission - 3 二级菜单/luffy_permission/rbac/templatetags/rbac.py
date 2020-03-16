from django import template
from django.conf import settings
import re

register = template.Library()


@register.inclusion_tag('menu.html')
def menu(request):
    menu_dict = request.session[settings.MENU_SESSION_KEY]

    return {'menu_list': menu_dict.values()}
