# 1.拾遗
    # pass语句
    # 格式化输出
        # %s
        # '其他内容%s其他%s内容'%(变量,变量2)
    # 运算符
        # 算数运算符 + - * / % //
        # 比较运算符 > < >= <= == !=
        # 赋值运算符（新）
            # =
            # +=
            # -=
            # *=
            # /=
            # %=
        # 逻辑运算符（新）
            # and 与
            # or  或
            # not 非
            # 优先级 括号>not>and>or
        # 身份运算符（新） :判断的是两个变量的内存地址
            # is
            # is not
            # 如果两个变量的内存地址相等，值一定相等
# 2.编码
    # 编码的种类 ： ascii、gbk、unicode、utf8
    # UNICODE --> UTF8 'ABC'.encode('utf-8')
    # UNICODE <-- UTF8 b'\xe6\xe8\xe7'.decode('utf-8')
# 3.基本数据类型
    # bool int float
    # list
        # 索引
            # 正数 0~n
            # 倒数 -1~-m
        # 切片 有步长，步长可以省略，顾头不顾尾
            # [start:end:step]
            # [::] [:]
            # [:3]
            # [:3:1] [:3:2] [4:9]
            # [::-1] 完全反转列表
        # 增 append 向末尾添加值
        # 删 lst.remove('值') lst.pop()删掉列表的最后一个值
        #    lst.clear()    del lst[8]
        # 修改 lst[索引] = 新的值
        # 值的引用
        # 浅拷贝
    # 通用的操作
        # in /not in
        # len(lst) 查看列表的长度
        # 获取列表中的每一个元素
            # for  break continue else
                # 都是循环一个固定的数据类型 —— 迭代的过程
            # while break continue else
                # 根据一个条件进行循环
    # str
        # 索引
        # 切片
        # 循环
        # 大小写的转换 upper
        # 分割和合并 split join
        # 替换 replace
        # 去掉边界上的内容 strip()   strip('<>')
        # 开始和结尾 startswith  endswith
        # 字符串的组成 isdigit
    # tuple 元组（元素1,元素2）
        # 不可变的序列
        # 可以切片
        # 可以循环
        # 可以使用索引查看
    # dict 字典 {'k1':'v1',123:'v2',(1,2):['alex','83']}
        # key有要求，不能是列表字典也不能重复
        # 可以循环，并且循环取到的key
        # 增
            # d['不存在的key'] = 值
        # 删
            # d.pop('key')
            # del d['key']
        # 改
            # d['存在的key'] = 新的值
        # 查
            # d['存在的key']
            # d.get('不知道存不存在的key')
    # range
        # print(range(1,100))
        # for i in range(0,101,2):
        #     print(i)