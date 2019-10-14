# css语言
    # 专门配合着html标签使用的
    # 能够给丑陋的标签加上适当的美观样式

# 引入css样式的方式
    # 行内引入 尽量避免使用
        # <span style="color: green;background-color: red;">你好,世界</span>
    # style标签引入
        # <style>
        #     span{
        #         color: green;
        #         background-color: red;
        #     }
        # </style>
    # link引入外部的css文件  推荐使用的
        # <link rel="stylesheet" href="demo1.css">
        # demo1.css
            # span{
            #      color: green;
            #      background-color: red;
            #  }
    # 样式引入的优先级 行内样式优先，link和style的样式谁写在后面谁优先生效

# 基础样式
    # span{
    #     color: pink;       设置字体颜色
    #     background-color: blue;
    #     width: 300px;     不生效（行内元素）
    #     height: 200px;    不生效（行内元素）
    # }
    # div{
    #     background-color: #ffe0ff;  设置背景色
    #     width: 400px;      设置宽度
    #     height: 200px;     设置高度
    # }

# html中的颜色 ：rgb表示  red  green blue 光谱三原色
    # 单词表示 ： red green blue yellow pink purple
    # 十六进制表示法 : #FFFFA3  #FFDDAA -简写->#FDA
    # rgb表示法 : rgb(255,255,163)
    # rgba表示法 : rgba(0,0,0,0.5)  表示透明度

# 选择器 用来从body的大量标签中筛选出我想改变样式的标签
    # 标签选择器 span div p input a li ul
    # 类选择器 class='类名'  .类名
    # id选择器 id = '唯一标识'  #id名    id在全网页不能重复
    # 优先级 : 行内1000 > id100 > class类10 > 标签1 > 继承0

# 高级的选择器
    # 后代选择器 div p  表示div中的所有p标签都被选择
    # 子代选择器 div>span  表示div子代中的所有span标签都被选择
    # 毗邻选择器 p+span 只找p标签后面一个span标签
    # 弟弟选择器 p~span 找到p之后的所有span
    # 并集选择器 ul,ol,p 找到这三个标签,给他们设置统一的样式
    # 交集选择器 div.div2 表示类名必须是div2的div标签才能使用这个样式
    # 属性选择器
'''
         a[title]{
            color: lightgreen;
        }
        a[href='http://www.jd.com']{
            color: lightblue;
        }
'''
    # 伪类选择器 html4
        # a:link a标签没有被访问的时候   a:visited a标签被访问的时候   a:active 鼠标按下a的时候
        # input:focus input获取到鼠标的焦点时
        # :hover 鼠标悬浮时
    # 伪元素选择器
        # after
        # first letter
        # before

# 更多样式
    # 字体样式
        # font-family
        # font-weight :字体粗细
        # font-size :控制字体大小
    # 文本样式
        #.title{
        #     text-align: center;   /*控制文本水平居中*/
        #     text-decoration: line-through; /*underline overline*/
        #     /*text-indent: 2em;     !*缩进*!*/
        #     line-height: 100px;    /*控制文本在line-height的高度上垂直就居中*/
        #     height: 100px;
        #     background-color: lightgoldenrodyellow;
        # }
    # 背景图片
        # 背景图片
        # div{
#             height: 500px;
#             background-color:lightgoldenrodyellow;
#             background-image: url('p0.jpg');
#             background-repeat: no-repeat;
#             /*background-repeat: repeat-x;*/
#             /*background-repeat: repeat-y;*/
#             background-position: right bottom ;   /* right/left/center  top/center/bottom*/
#             background-size: 400px;
#         }

    # 边框 border
'''
        div{
            height: 300px;
            width: 200px;
            background-color:lightgoldenrodyellow;
            /*border: solid red 10px;*/
            /*border-style: solid;*/
            /*border-style: dashed;*/
            /*border-style: dotted;*/
            /*border-style: double;*/
            /*border-color: palevioletred blue yellow gray;*/
            /*border-width: 10px 5px 20px 30px;*/
            border-top:solid blue 5px;
            border-left:solid gray 5px;
            border-right:solid gray 5px;
            border-bottom:solid gray 5px;
            }
'''

    # 圆角 border_radius
        # border-radius: 50%; 调整圆角
        # border-radius: 40px; 调整圆角

    # 块 行内块和 内联的互相转换
        # 很少把块或者行内块 转换成内联
        # 内联转块/行内块
        # display : inline/inline-block/block
'''
       a{
            background-color: rgb(51,51,51);
            color: lightgoldenrodyellow;
            height: 38px;
            width: 80px;
            display: inline-block;
            /*display: block;*/
            line-height: 38px;
            text-align: center;
            text-decoration: none;
        }
        li{
            display: inline-block;
        }
'''
    # 盒模型
        # width height 表示内容部分的宽\高
        # padding  表示内边距部分的宽度
        # border 表示边框的宽度
        # width +2*padding+2border = 盒子的整体宽度
        # height +2*padding+2border = 盒子的整体高度
        # margin 表示盒子的外边距
            # 上下盒子之间设置会发生塌陷
            # 父子盒子之间设置也会发生塌陷
    # 浮动
        # 脱离标准文档流 脱标
        # 浮动到独立的位置上
        # float:left/right
        # 清除浮动,避免父元素缩水
            # clear:both
            # 伪元素清除发 自定义cleardix类
    # 定位
        # 相对定位(relative) : 移动但还是占有原来的位置 相对于自己原来的位置进行移动
        # 绝对定位(absolute) : 相对于上一级设置了position的元素移动,如果上一级没有设置,会相对于整个页面移动
        # 固定定位(fixed): 相对于整个浏览器窗口固定在一个位置上,不随着滚动条的移动发生位置变化
    # z-index
    # opacity
        # 标签的背景和内容整体变透明
        # rgba 是背景颜色变透明
