# jquery的导入
# jquery查找标签
    # jquery对标签的查找完全可以复用选择器规则
    # 通过jquery对象转换成dom对象 jq_obj[index]
# 选择器语法查找
    # 标签选择器
        # $('p')        标签选择器
        # $('.para1')   类选择器
        # $('#container')   id选择器
        # $('*')         通用选择器
        # $('p.para1')   交集选择器
        # $('div,p')   并集选择器
    # 层级选择器
        # $(div p) 后代选择器 : 找到子孙中符合条件的
        # $(div>p)子代选择器 : 找子代中符合条件的
        # $(div+p)毗邻选择器 : 找紧邻的下一个
        # $(div~p)弟弟选择器 : 找某一个标签下的所有xxx标签
    # 属性选择器
        # $('[属性名]')  $('[href]')
        # $('[属性名='属性值']')  $('[href='http://www.baidu.com']')
        # $('[属性名^='属性值']')  $('[href^='http')
        # $('[属性名$='属性值']')  $('[href$='com')
        # $('[属性名*='属性值']')  $('[href*='baidu')
        # $('[属性名!='属性值']')  $('[href!='baidu')

# 筛选器
    # $(选择器:筛选器)
    # 根据索引筛选
        # $('p:first')
        # $('p:last')
        # $('p:even')
        # $('p:odd')
        # $('p:eq(index)')
        # $('p:gt(index)')
        # $('p:lt(index)')
    # not 筛选不包含某选择器要求的xxx
        # $('p:not(.para3)')
    # has 通过子代找当前
        # $('li:has(a)')
    # 表单筛选器,根据type进行筛选
        # $('input:type类型:选中情况')
        # $('input:radio:checked')
        # $('input:text:disabled')
        # $('input:text')
        # $('input:password')
        # input中没有date筛选器
        # $(':selected')
        # $('option:selected')
# 标签的筛选方法
    # 兄弟 : siblings()
    # 弟弟 : next() nextAll() nextUntil()
    # 哥哥 : prev() preAll() prevUntil()

    # 祖辈 :parent() parents() parentsUntil()
    # 子  :children()

# 过滤方法
    # .first()
    # .last()
    # .eq(index)
    # .not('#disable')
    # .filter('.para1')
    # .find('a')
    # .has('a')

