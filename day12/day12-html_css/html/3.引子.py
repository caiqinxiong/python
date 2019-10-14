# B/S架构
# socket
# html 约束文档中文字的框架的(字体大小 是否换行)
# css 给这些基础文字框架加上好看的样式
# javascript -js 能够让网页动起来

# 双边标记 有开始就有闭合
# 单边标记 只有一个标记,自闭和

# html页面的结构
    # head :在网页部分不显示的
        # meta 编码 渲染需要的引擎 搜索关键字 显示的简介
        # title 网页的标签栏的显示
    # body
        # 空白折叠 对换行符和空格都不敏感
            # <br>  &nbsp;
        # 块级标签(h1) 内联标签(span)
        # 内联标签
            # br  span
            # <img src="timg.jpg" alt="荷官图片">
                # src 可以使用本地的路径,也可以使用网络地址
                # alt 在图片加载失败的时候显示概要信息
                # height="400px"  图片的高
                # width="481px"   图片的宽
                # align
            # <a href="http://www.baidu.com" title="baidu知道" target="_blank">百度一下</a>
                # href 就是链接的地址
                # title 是鼠标悬浮的时候显示提示内容
                # target  _blank表示在新的页面打开,_self默认的,表示在当前页面打开
                # 锚链接 在整个页面上埋下一个锚点,在点击a标签的时候可以跳转到页面的锚点中去
                    # <a href="#top" title="back">回到顶部</a>
                    # 在整个页面中必须有一个叫做top的id对应的标签
        # 块级标签
            # 标题标签 h1-h6
            # 列表
                # ul标签 无序的列表  type(disc 默认实心圆,square 实心方,circle 空心圆,none无符号)
                #           <ul type="disc">
                #             <li>立立</li>
                #             <li>松松</li>
                #             <li>老王</li>
                #             <li>查查</li>
                #         </ul>

                # ol标签 有序列表 type(1 A a i I) start表示开始的位置
                #         <ol start='2'>
                #             <li>立立</li>
                #             <li>松松</li>
                #             <li>老王</li>
                #             <li>查查</li>
                #         </ol>

                # dl标签 定义列表
'''
                        <dl>
                            <dt>姓名</dt>
                            <dd>alex</dd>
                            <dd>wusir</dd>
                            <dd>小强</dd>
                            <dt>性别</dt>
                            <dd>不详</dd>
                            <dd>女</dd>
                            <dd>男</dd>
                        </dl>
'''
            # 表格
                # <table border='1px' cellpadding='10px' cellspacing='5px'>
                    # <thead>
                        # <tr>
                            #<th>标题内容</th>
                            #<th>标题内容</th>
                            #<th>...</th>
                        #</tr>
                    # </thead>
                    # <tbody>
                        # <tr>  一个tr代表一行
                        #     <td colspan = 2>表格内容</td>
                        #     <td rowspan = 2>表格内容</td>
                        #     <td>...</td>
                        # </tr>
                    # </tbody>
                # </table>
           # div标签
