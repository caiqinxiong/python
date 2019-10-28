# 操作标签的增 删 改 复制
    # 增
    # 父子关系
    #    append appendTo
        # jq.append(dom对象/jq对象/写好的标签字符串) 表示在jq对象中添加一个标签
        # jq对象.appendTo(父级标签选择器/标签字符串/jq对象/dom对象)
    #    prepend prependTo
        # 父jq对象.prepend(子元素)
        # 子jq对象.prependTo(父元素)
    # 兄弟关系
    #    after insertafter
        # 旧.after(新)
        # 新.insertafter(旧)
    #    before insertbefore
        # 旧.before(新)
        # 新.insertbefore(旧)
    # 删
        # remove 删除标签也删除事件
        # detach 删除标签但不删除事件
        # empty  清空标签内的子标签
    # 改
        # 旧的.replacewith(新)
        # 新的.replaceAll(旧)
    # 复制
        # clone()     单纯的克隆标签但不克隆事件
        # clone(true) 克隆标签包括标签所带事件
# 操作标签的文本
    # jq.text('要写的文本')
    # jq.html('要写的标签内容')
# 操作标签的属性
    # attr('class')     获取当前class的值
    # attr('class','value') 设置class的值
    # removeAttr('readonly') 删除readonly属性
    # prop('checked')   选中返回true 没选中返回false
# 操作标签的类
    # addclass('类名')    添加一个类
    # removeclass('类名') 删除一个类
    # toggleclass('类名') 有就删除 没有就添加
# 操作标签的值 - 针对表单标签
    # val()    如果不传参数表示获取value属性的值
    # val(值)  如果传参数,表示设置value属性的值
    # $(':checkbox').val([2])
    # 对于radio\checkbox\select标签,所有的修改选中的状况都需要把要选中的值放到数组中
# 操作标签的css样式
    # css('样式名')
    # css('样式名','样式值')
    # css({'样式名':'样式值'})
# jq绑定事件
'''
<body>
<button>点击</button>
</body>
<script>
    $('button').click(
        function () {
            alert('click')
        })
</script>
'''

# 添加 移除 按钮和事件绑定操作ul标签