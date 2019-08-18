# 序列化
# 标准化 --> 变得标准
# 序列化 --> 变成序列

# 序列 --> 按照顺序排列的
# json模块
# import json
# dic = {"operate":'login','username':'alex','password':'bigsb'}
# ret = json.dumps(dic)
# print(dic)
# print(ret,type(ret)) # 通过字符串--> 字节
# byte_8 = ret.encode('utf-8')
# print(byte_8)

# dic -json.dumps-> json格式的str -encode-> 字节 -->在网络上传递了
# 字节 -decode-> 字符串 -->
# str8 = byte_8.decode('utf-8')
# print(str8)
# ret = json.loads(str8)  // 反序列化过程  把字符串转换成字典或者其他数据类型
# print(ret)

# 1.网络传输不认识字典   2.我们的文件操作不认识字典
# import json
# dic = {'北京':{'朝阳':{},'海淀':{}}}
# text= json.dumps(dic,ensure_ascii=False)   # 序列化的过程 把字典/其它数据类型转换成字符串
# print(text)
# with open('city',mode = 'w',encoding='utf-8') as f:
#     f.write(text)

# with open('city',encoding='utf-8') as f:
#     str_d = f.read()
#     print(str_d)
#     dic = json.loads(str_d)
# print(dic)

# 1.写到文件里的是中文出现编码   ensure_ascii=False
# 2.为什么在json中不能放集合

# json数据类型是一个特殊的字符串
# 在任何语言中它的type都必须是字符串
# 但是还要满足一些要求 : key必须是字符串,且value只能是:字典 列表 字符串 数字 bool值

# json是所有的编程语言都公认的一种数据类型
# 如果是python语言要给java语言发送信息, 那么就可以转换成json格式,java经过一系列转换就可以获取到字典数据了






# pickle模块
