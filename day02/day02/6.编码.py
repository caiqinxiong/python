# n进制   一位最多能表示0~(n-1)
# 0101010101111001

# print(100)
# print(bin(100)) # 十进制转二进制
# print(oct(100)) # 十进制转八进制
# print(hex(100)) # 十进制转十六进制

# print('hello world')
# 内存 ：二进制
# 硬盘山

# 二进制         -->    23533334030232120
# 1010101010
# print(bin(5))
# 0001011100000101
# 用固的长度
# A 65
#
# a 97
# {
# }
# [
# 0-255
# 8位2进制
# 11111111 -->255
# 00000000 -->0

# 0、1 1位  1bit   比特、位
# 8位 8bit  1byte  字节
# 1024字节  1kb
# 1024kb    1mb
# 1024mb    1gb
# 1024gb    1tb

# ascii码
# 中国 gb2312
# 万国码 unicode
# 中国 gbk
# utf8 可变长的编码

# 4个字节 4个字节表示一个文字
# 4*8 = 32位
# print(2 **32)
# 00000000 01010101 01010010 01010111
# 01110000 01010101 01010010 01010111
# 00000000 00000000 00000000 00001100

# utf8 可变长的编码
    # 英文字母 8位  1byte
    # 欧洲文字 16位 2bytes
    # 中国文字 24位 3bytes

# 编码使用在哪儿的？
    # unicode ：程序的内存里的
        # print('你好，中国')
    # utf-8：存在文件里或者在网络上传输的时候
        # unicode ———> utf8

# 编码的转换
# s = '你好，中国'
# print(s.encode('utf-8'))  # unicode-->utf-8
# b = b'\xe4\xbd\xa0\xe5\xa5\xbd\xef\xbc\x8c\xe4\xb8\xad\xe5\x9b\xbd'
# print(b.decode('utf-8'))

# s = '你好，中国'
# print(s.encode('GBK'))  # unicode-->utf-8
# b = b'\xc4\xe3\xba\xc3\xa3\xac\xd6\xd0\xb9\xfa'
# print(b.decode('gbk'))