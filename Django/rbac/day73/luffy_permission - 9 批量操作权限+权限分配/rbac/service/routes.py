from django.conf import settings
from django.utils.module_loading import import_string
from django.urls import RegexURLResolver, RegexURLPattern
from collections import OrderedDict


def recursion_urls(pre_namespace, pre_url, urlpatterns, url_ordered_dict):
    # None, "/", urlpatterns, url_ordered_dict
    # None, '/^'
    # rbac, '/^'

    for item in urlpatterns:
        if isinstance(item, RegexURLResolver):
            if pre_namespace:
                if item.namespace:
                    namespace = "%s:%s" % (pre_namespace, item.namespace,)
                else:
                    namespace = pre_namespace
            else:
                if item.namespace:
                    namespace = item.namespace
                else:
                    namespace = None
            recursion_urls(namespace, pre_url + item.regex.pattern, item.url_patterns, url_ordered_dict)
        else:
            if pre_namespace:
                name = "%s:%s" % (pre_namespace, item.name,)  # rbac:role_list
            else:
                name = item.name
            if not item.name:
                raise Exception('URL路由中必须设置name属性')

            url = pre_url + item._regex  # /login/    /role/list/
            url_ordered_dict[name] = {'name': name, 'url': url.replace('^', '').replace('$', '')}


def get_all_url_dict(ignore_namespace_list=None):
    """
    获取路由中
    :return:
    视图      RegexURLPattern
    include   RegexURLResolver

    """
    ignore_list = ignore_namespace_list or []
    url_ordered_dict = OrderedDict()

    md = import_string(settings.ROOT_URLCONF)
    print(md.urlpatterns)
    urlpatterns = []

    for item in md.urlpatterns:
        if isinstance(item, RegexURLResolver) and item.namespace in ignore_list:
            continue
        urlpatterns.append(item)
    recursion_urls(None, "/", urlpatterns, url_ordered_dict)
    return url_ordered_dict
