from aip import AipOcr


def initial():
    """ 初始化连接 """
    APP_ID = '16777849'
    API_KEY = 'w9qfqiWNYBVjEaKxn3axyG4w'
    SECRET_KEY = 'pRUFf8yB20d1FptShqsuYwKEVUP6GtAK'
    return AipOcr(APP_ID, API_KEY, SECRET_KEY)

def get_file_content(filePath):
    """ 读取图片 """
    with open(filePath, 'rb') as f:
        return f.read()

if __name__ == '__main__':
    client = initial()
    image = get_file_content('a.png')
    res1 = client.basicGeneral(image)  # 调用通用文字识别, 图片参数为本地图片
    # res2 = client.basicAccurate(image)  # 调用通用文字识别（高精度版）
    # 调用通用文字识别, 图片参数为远程url图片
    # res3 = client.basicGeneralUrl('https://img2018.cnblogs.com/blog/1168165/201906/1168165-20190623215706582-962703809.png')
    print(res1)  # 返回结果
    for text in res1['words_result']:
        print(text['words'])