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

    for i in ret:
        ordered_dict[i] = menu_dict[i]

    for item in ordered_dict.values():

        item['class'] = 'hide'

        for i in item['children']:
            if re.match(r'^{}$'.format(i['url']), request.path_info):
                i['class'] = 'active'
                item['class'] = ''

    return {'menu_list': ordered_dict.values()}
