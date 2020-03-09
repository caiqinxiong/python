__author__ = 'Luzaofa'
__date__ = '2018/11/9 20:45'

import xadmin

from xadmin import views

from plug_ins.models import MenuOne, MenuTwo, MenuThe


class BaseSetting(object):
    """
    配置主题
    """
    enable_themes = True
    use_bootswatch = True


class GlobalSetting(object):
    """
    配置抬头和尾部，以及列表显示
    """
    site_title = '我的后台管理系统'
    site_footer = '仅供交流学习之用'
    menu_style = 'accordion'

    # 自定义菜单
    def get_site_menu(self):
        return [
            {
                'title': '用户自定义功能',
                'menus': (
                    {
                        'title': '功能一',
                        'icon': 'fa fa-smile-o',
                        'url': '/xadmin/plug_ins/menuone/',
                        'perm': self.get_model_perm(MenuOne, 'view')
                    },
                    {
                        'title': '功能二',
                        'icon': 'fa fa-smile-o',
                        'url': '/xadmin/plug_ins/menutwo/',
                        'perm': self.get_model_perm(MenuTwo, 'view')
                    },
                    {
                        'title': '功能三',
                        'icon': 'fa fa-smile-o',
                        'url': '/xadmin/plug_ins/menuthe/',
                        'perm': self.get_model_perm(MenuThe, 'view')
                    },
                )
            }
        ]


xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSetting)
