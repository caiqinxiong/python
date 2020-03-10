# -*- coding: utf-8 -*-
__author__ = 'caiqinxiong_cai'
#2020/3/10 11:07
# https://blog.csdn.net/bocai_xiaodaidai/article/details/94395604
# xadmin全局配置
import xadmin
from xadmin import views
from . import models

class BaseSetting(object):
    """xadmin的基本配置"""
    enable_themes = True  # 开启主题切换功能
    use_bootswatch = True  # 支持切换主题

xadmin.site.register(views.BaseAdminView, BaseSetting)

class GlobalSettings(object):
    """xadmin的全局配置"""
    site_title = "SCM发布系统"  # 设置站点标题
    site_footer = "北京宜搜天下科技有限公司"  # 设置站点的页脚
    menu_style = "accordion"  # 设置菜单折叠
    global_search_models = [models.User,models.ReleaseInfo]
    # 设置models的全局图标, User, ReleaseInfo 为表名
    global_models_icon = {
        models.User: "glyphicon glyphicon-user", models.ReleaseInfo: "fa fa-cloud"
    }  # 设置models的全局图标

xadmin.site.register(views.CommAdminView, GlobalSettings)

class UserAdmin(object):
    # 在列表中显示 username email 两个字段
    list_display = ['username', 'email','createtime','sex']
    # 根据 username 字段 搜索
    search_fields = ['username']
    list_filter = ['username'] # 过滤器
    # 显示还原按钮，删除修改的信息可以还原
    reversion_enable = True

    def get_readonly_fields(self, **kwargs):
        """  重新定义此函数，限制普通用户所能修改的字段  """
        print(self.org_obj)
        if self.user.is_superuser:
            self.readonly_fields = ['email',] # 管理员也不能修改的字段
        return self.readonly_fields

    readonly_fields = ('email',) # 普通用户不能修改的字段



xadmin.site.register(models.User, UserAdmin)

class GroupAdmin(object):
    list_display = ['gname','createtime','u2g']
    search_fields = ['gname']
    list_filter = ['gname']
    # 显示还原按钮，删除修改的信息可以还原
    reversion_enable = True
xadmin.site.register(models.Group,GroupAdmin)

class ProjectAdmin(object):
    list_display = ['pname','kname']
    search_fields = ['pname']
    list_filter = ['pname']
    # 显示还原按钮，删除修改的信息可以还原
    reversion_enable = True
xadmin.site.register(models.Project,ProjectAdmin)

class ReleaseInfoAdmin(object):
    list_display = ['taskname','svnversion','branch','release_info','issue']
    search_fields = ['taskname']
    list_filter = ['taskname']
    # 显示还原按钮，删除修改的信息可以还原
    reversion_enable = True
    preserve_filters = False # 默认情况下，当你对目标进行创建、编辑或删除操作后，页面会依然保持原来的过滤状态

    list_per_page = 20 #每页显示20个

xadmin.site.register(models.ReleaseInfo,ReleaseInfoAdmin)



'''
 
xadmin 可以使用的页面样式控制基本与Django原生的admin一直。
 
list_display         列表展示的字段
 
preserve_filters  默认情况下，当你对目标进行创建、编辑或删除操作后，页面会依然保持原来的过滤状态。将preserve_filters设为False后，则会返回未过滤状态。
 
prepopulated_fields  设置预填充字段。不接收DateTimeField、ForeignKey和ManyToManyField类型的字段。
 
view_on_site  这个属性可以控制是否在admin页面显示“View site”的链接。这个链接主要用于跳转到你指定的URL页面。
 
free_query_filter 属性: 默认为 True , 指定是否可以自由搜索. 如果开启自由搜索, 用户可以通过 url 参数来进行特定的搜索, 
search_fields        可以通过搜索框搜索的字段名称，xadmin使用的是 模糊查询，存在外键 同 list_filter 一样  注意：只能包括 字符类型，不能有 非字符类型 如：SBBH-20180515-0002
list_filter          可以进行过滤操作的列，例如：存在外键字段class ---》student__class 获取值
ordering             默认排序的字段
readonly_fields      在编辑页面的只读字段
exclude              在编辑页面隐藏的字段
list_editable        在列表页可以快速直接编辑的字段
show_detail_fileds   在列表页显示详情信息
refresh_times        指定列表页的数据定时刷新   例如：refresh_times=(3,5)
list_export          控制列表页导出数据的类型
show_bookmarks       控制是否显示书签功能
data_charts          控制显示图标的样式
model_icon           配置表的图标，可以在 awesome 上下载最新的font-awesome.css 替换，并寻找相应的icon书写
fieldsets          ，详细页面时，使用fieldsets标签对数据进行分割显示
empty_value_display = "列数据为空时，显示默认值"
#  列聚合，可用的值："count","min","max","avg",  "sum"
aggregate_fields = {"expire": "max"}
 
# 显示还原按钮，删除修改的信息可以还原
reversion_enable = True
 
# 添加数据时候，一步一步提供数据
wizard_form_list = [
    ("基础信息", ("name", "contact", "telphone", "address")),
    ("其它信息", ("customer_id", "expire", "description")),
]
 
fields               表单显示内容, 不包含在内的字段不能编辑
filter_horizontal    从‘多选框’的形式改变为‘过滤器’的方式，水平排列过滤器，必须是一个 ManyToManyField类型，且不能用于 ForeignKey字段，默认地，管理工具使用下拉框 来展现外键 字段
 
raw_id_fields       将ForeignKey字段从‘下拉框’改变为‘文本框’显示
 
relfield_style      后台自定义不是下拉选择框，而是搜索框（解决了为什么用户不是下拉框的问题。。） relfield_style = 'fk-ajax'
exclude             在编辑和查看列表时指定不显示的字段
list_editable       列表显示的时候，指定的字段可以直接页面一键编辑
list_display_links   设置默认可编辑字段
list_per_page = 20   每页显示20个
actions = ('ocr_action', 'excel_action', 'auto_excel_action') 在类中自定义的函数方法
auto_excel_action.short_description='自动化导入数据文件'         函数名描述
 
object_list_template = "test.html"   自定义页面
 
data_charts          图表，该属性为dict类型，key为图表的标示名称，value为图表的具体设置属性
data_charts = {
        "user_count": {'title': u"约运动",
                       "x-field": "sport_time", 
                       "y-field": ("people_nums",),
                       },
    }
 
图表属性：
 
　　title :   图表的显示名称
　　x-field : 图表的 X 轴数据列, 一般是日期, 时间等
　　y-field : 图表的 Y 轴数据列, 该项是一个 list, 可以同时设定多个列, 这样多个列的数据会在同一个图表中显示
　　order : 排序信息, 如果不写则使用数据列表的排序
 
    # 导出类型
    list_export = ('xls', 'xml', 'json')   list_export设置为None来禁用数据导出功能
    #导出字段
    list_export_fields = ('start_people', 'sport', 'sport_time')

'''