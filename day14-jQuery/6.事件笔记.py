# jq对象.click(
#     function (){
#         出发了click事件的逻辑
# }
# )

# $('input').focus(function()
# {
# $('input').css('background-color', 'yellow')
# }) // 获取焦点
# $('input').blur(function()
# {
# $('input').css('background-color', 'white')
# }) // 失去焦点

# 事件冒泡
# 当某一个子元素出发了事件之后,这个事件会一直向上一层父元素冒泡
# 如果此时父元素也对这个事件绑定了方法,那么会一直向上触发父元素的事件
# 阻止事件冒泡的方法:
    # 在function中return false
    # 在function中接收event参数,并执行event.stopPropergation()

# 事件委托
    # 在一个元素还没有出现之前,就可以为它绑定一些事件
# $('div').on('click', 'button', function()
# {
#     alert('点击我了')
# })
# 其中div是一个已经存在的父级元素,button这里可以替换成任意的子元素选择器

# 肖峰
#