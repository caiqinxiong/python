from django import template
from django.conf import settings
import re
from collections import OrderedDict

register = template.Library()


@register.inclusion_tag('menu.html')
def menu(request):
    ordered_dict = OrderedDict()

    menu_dict = request.session[settings.MENU_SESSION_KEY]

    ret = sorted(menu_dict, key=lambda x: menu_dict[x]['wight'], reverse=True)

    for key in ret:

        item = ordered_dict[key] = menu_dict[key]

        item['class'] = 'hide'

        for i in item['children']:

            if i['id'] == request.current_menu_id:
                # if i['id'] == getattr(request,settings.CURRENT_MENU_ID):
                i['class'] = 'active'
                item['class'] = ''

    return {'menu_list': ordered_dict.values()}


@register.inclusion_tag('breadcrumb.html')
def breadcrumb(request):
    return {'breadcrumb_list': request.breadcrumb_list}


@register.filter
def has_permission(request, name):
    permission_dict = request.session[settings.PERMISSION_SESSION_KEY]
    if name in permission_dict:
        return True
