# import re
# from urllib.request import urlopen
#
# ret = urlopen('https://movie.douban.com/top250?start=0&filter=')
# html_content = ret.read().decode('utf-8')
#
# pattern = '<div class="item">.*?<div class="pic">.*?<em .*?>(?P<id>\d+).*?<span class="title">(?P<title>.*?)</span>' \
#           '.*?<span class="rating_num" .*?>(?P<rating_num>.*?)</span>.*?<span>(?P<comment_num>.*?)评价</span>'
# ret = re.finditer(pattern,html_content,flags=re.S)
# for i in ret:
#     print(i.group('id'),i.group('title'),i.group('rating_num'),i.group('comment_num'))


import re
import json
from urllib.request import urlopen

def getPage(url):
    response = urlopen(url)
    return response.read().decode('utf-8')

def parsePage(s):
    com = re.compile(
        '<div class="item">.*?<div class="pic">.*?<em .*?>(?P<id>\d+).*?<span class="title">(?P<title>.*?)</span>'
        '.*?<span class="rating_num" .*?>(?P<rating_num>.*?)</span>.*?<span>(?P<comment_num>.*?)评价</span>', re.S)

    ret = com.finditer(s)
    for i in ret:
        yield {
            "id": i.group("id"),
            "title": i.group("title"),
            "rating_num": i.group("rating_num"),
            "comment_num": i.group("comment_num"),
        }


def main(num):
    url = 'https://movie.douban.com/top250?start=%s&filter=' % num
    response_html = getPage(url)
    ret = parsePage(response_html)
    print(ret)
    f = open("move_info7", "a", encoding="utf8")

    for obj in ret:
        print(obj)
        data = str(obj)
        f.write(data + "\n")

count = 0
for i in range(10):
    main(count)
    count += 25