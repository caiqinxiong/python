# js语法
# ECMAscript
    # 变量
    # 基础数据类型 : number string boolean object array json
    # 运算符 : b=a++ b=++a 1=='1' 1===1
    # 流程控制
        # if(条件){
            # 条件满足之后的逻辑
        # }
        # else if(条件){
            # 条件满足之后的逻辑
        # }
        # else{
            # 上面条件都不满足之后的逻辑
        # }

        # for(var i=0;i<10;i++){
        # }
        # for(i in arry){
        # }

        # while(条件){
        # }
    # 定义函数
        # function 函数名(){
            # arguments
        # }
# Bom 浏览器对象模型
    # location.href
    # history.back()/history.forward()
    # history.go(-1)/history.go(1)
# Dom 文档对象模型
    # 创建标签 :document.createElement('标签的名字')
    # 查找标签 : 按照id 按照class 按照标签名查
    # 间接查找 : 父子兄弟
    # 操作节点 : 节点的增加 删除 替换
    # 值操作 : .innerText='要放在标签里的值'=  .innerHTML='<p>要放在标签里的整个标签内容</p>'
    # 属性操作
    # 类操作
    # 值操作
    # 样式操作

    # 事件 onclick事件
        # 找到一个标签的dom对象  :直接查找\间接查找
        # 给这个dom对象绑定一个事件
            # dom_obj.onclick = function(){
            # }

            # dom_obj.onclick = 函数名()
            # function 函数名(){
            # }
        # 给这个事件写一个动作函数
            # 动作就是函数内部的内容
