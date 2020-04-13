import requests

res = requests.get('https://15201446433-1585663305-1301483313.cos.ap-chengdu.myqcloud.com/1585663357163_tourist.jpg')
print(res.content)