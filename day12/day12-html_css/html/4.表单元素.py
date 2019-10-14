# form表单
    # input标签 :
        # type属性 描述input框的类型 包括 text password radio checkbox submit
                                        # reset button hidden file date
        # name : 提交数据之后以name属性为依据
        # value :用户选择或者输入的值以value属性为依据
        # readonly : 给text和password框设置readonly 数据可以提交但是不能修改
        # disable : 给所有的input框都可以设置disable 表示不能修改数据也不提交
        # placeholder : 给text或者password框添加提示,当输入框获取到焦点时提示自动消失
        # 示例
        # 用户名 : <input type="text" name = 'username' value = 'alex' readonly>
        # 密  码 : <input type="password" name = 'passwd'>
        # <input type="radio" name = 'sex' value="m" checked> 男
        # <input type="radio" name = 'sex' value="f"> 女
        # <input type="checkbox" name = 'hobby' value="1" checked disabled> 抽烟
        # <input type="checkbox" name = 'hobby' value="2"> 喝酒
        #  <input type="checkbox" name = 'hobby' value="3"> 烫头
        #  <input type="submit">
    # lable标签
        # lable 的 for关联一个输入款的id,如果点击lable中的文字,这个输入框会自动获取到焦点
    # button标签
        # 在form表单内部外部都可以使用
            # 在内部表示提交
            # 在外部只普通按钮
    # textarea 文本域
        # <textarea name="content" id="" cols="30" rows="10"></textarea>
        # name : 提交数据之后以name属性为依据
        # cols : 表示的是文本域的宽度
        # rows : 表示的是文本域的高度
    # select
    #      <select name="city" size="3" multiple>
    #         <option value="1">北京</option>
    #         <option value="2" selected>上海</option>
    #         <option value="3">天津</option>
    #         <option value="4">广州</option>
    #     </select>