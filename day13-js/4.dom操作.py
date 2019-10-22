# 查找节点
    # 直接查找
        # obj  = document.getElementById('元素的id') 永远只会找到一个标签
        # objs = document.getElementsByClassName('元素的class') 永远得到数组
        # objs = document.getElementsByTagName('元素的标签名') 永远得到属组
    # 间接查找
        # 找父亲 obj.parentElement
        # 找儿子 obj.children
        #        obj.firstElementChild
        #        obj.lastElementChile
        # 找哥哥 obj.previousElementSibling
        # 找弟弟 obj.nextElementSibling
# 操作节点本身
    # 创建节点
        # obj = document.createElement('p')
        # <p></p>
        # obj.innderText = 'p标签'
        # <p>p标签</p>
    # 添加节点
        # 父节点.appendChild(子节点对象)
        # 父节点.insertBefore(要添加的子对象,参考节点对象)
    # 删除节点
        # 父节点.removeChild(子节点对象)
    # 克隆节点
        # 节点.cloneNode()   只拷贝一层
        # 节点.cloneNode(True) 拷贝所有子节点
    # 替换节点
        # 父节点.replaceChild(新对象,旧子节点)
# 操作节点内的文本
    # innerText :  pobj.innerText = '<a>我是一个a标签</a>'
    # innerHtml :  pobj.innerHTML = '<a href="http://www.mi.com">我是一个a标签</a>'
# 操作值
    # .value
# 操作属性
    # obj.setAttribute('属性名','属性值')
    # obj.getAttribute('属性名')
    # obj.removeAttribute('属性名')
# 操作类
    # obj.classList.add('类名')
    # obj.classList.remove('类名')
    # obj.classList.contains('类名')  判断是否包含
    # obj.classList.toggle('类名')    有就去掉,没有就加上
# 操作样式
    # obj.style.样式名 = 样式值

