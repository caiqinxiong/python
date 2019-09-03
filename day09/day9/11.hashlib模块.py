import hashlib
# 密码不能明文存储
# 获取到整个用户登录信息文件了所有的密码都泄露了
md5 = hashlib.md5(('只有我知道,别人不知道的秘密的字符串%s'%'alex').encode('utf-8'))
md5.update(b'123456')
ret = md5.hexdigest()
print(ret)

# e10adc3949ba59abbe56e057f20f883e     32位
# '123456'这个字符串通过md5这个算法加密之后的结果

# afdc71bd7bc87c2c0205421d9e2b5359
# ('123456'这个字符串通过md5这个算法+特有的字符串)加密之后的结果


# md5 = hashlib.sha1()
# md5.update(b'123456')
# ret = md5.hexdigest()
# print(ret)
# 7c4a8d09ca3762af61e59520943dc26494f8941b  40位
# '123456'这个字符串通过sha1这个算法加密之后的结果


# 对比两个文件是否一致
# import hashlib
# md5 = hashlib.md5()
# md5.update('你好你好你好再见'.encode('utf-8'))
# ret = md5.hexdigest()
# print(ret)

# 7c5368a646b1d58cecf51dc99a8ec53c
# 7c5368a646b1d58cecf51dc99a8ec53c
# import hashlib
# md5 = hashlib.md5()
# md5.update('你好你好'.encode('utf-8'))
# md5.update('你'.encode('utf-8'))
# md5.update('好'.encode('utf-8'))
# md5.update('再见'.encode('utf-8'))
# ret = md5.hexdigest()
# print(ret)

import hashlib
def get_md5(file):
    md5 = hashlib.md5()
    with open(file,'rb') as f:
        content = f.read()
        md5.update(content)
    ret = md5.hexdigest()
    return ret
ret = get_md5(r'F:\python自动化27期\day9\5.网络通信协议.py') == get_md5(r'F:\python自动化27期\day9\5.网络通信协议2.py')
print(ret)
