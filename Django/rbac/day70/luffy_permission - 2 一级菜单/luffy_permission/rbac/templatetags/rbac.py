from django import template
from django.conf import settings
import re

register = template.Library()


@register.inclusion_tag('menu.html')
def menu(request):
    # 当前的url
    url = request.path_info
    menu_list = request.session[settings.MENU_SESSION_KEY]
    for i in menu_list:
        if re.match("^{}$".format(i['url']), url):
            i['class'] = 'active'

    return {'menu_list': menu_list}
