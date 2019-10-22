# 定义变量:
    # 变量名由 数字 字母 下划线 $组成
    # var 变量名 = 变量的值
# 可以定义变量先不赋值 var a;
# 基础的数据类型
    # 查看类型 typeof 变量/typeof(变量)
    # 数字类型 number
        # 整数 和 小数
    # 字符串 string
        # '字符串1' "字符串2"
        # length
        # 去空白 切割 切片 大小写转换
    # 布尔值 Boolean
        # true false
        # 布尔值 : Boolean(值)
        # false : 0,undefined,'',null,NaN
        # true : [] {}
    # 数组对象
        # var a = [1,2,3,4]
    # 对象
        # var obj = {}
        # var obj.属性名 = 属性值
    # json对象
        # json对象 = JSON.stringpy(obj对象)
        # obj = JSON.parse(json对象)
    # 日期对象 Date对象
        # var obj = new Date()
        # var obj = new Date(2019,10,20,12,12,12)
    # 正则对象 RegExp对象
        # var re = new RegExp('\\d');
        # var re2 = /^1[3-9]\d{9}$/
        # re2.test('待匹配的字符串')
        # re2.test('13737373377')
        # 字符串使用正则 g表示匹配多个,i表示不区分大小写
            # str.match(/正则表达式/gi)
            # str.search(/正则表达式/i)
    # Math 数学对象
        # 求100-200之间的随机数 :100+Math.random()*(200-100)
    # 数据类型的转换
        # 字符串转数字
            # parseInt
            # parseFloat
        # 数字转字符串
            # String(数字)
            # 数字变量.tostring()
        # boolean转换
            # Boolean(任意数据)
# 流程控制
    # if
    # for(var i=0,i<=xxx,i++) 推荐你使用
    # while
    # a>b ? a:b
# 函数
    # function 函数名(){
    #     函数体
    #     return 一个值
    # }
    # 函数名()

    # 1. 函数只能有一个返回值
    # 2. 函数的参数和接收与否没有直接关系

# foreach
# map
