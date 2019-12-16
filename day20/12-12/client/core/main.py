import requests
import json

from conf import settings
from lib.import_class import get_class


def run():
    cls = get_class(settings.ENGINE_DICT.get(settings.ENGINE))
    obj = cls()
    obj.handler()
    # info = {'disk': {'1':{'x':'x'},'2':{'x':'x'}}, 'cpu': {'xx':{}}}
    # response = requests.post(
    #     url='http://127.0.0.1:8000/api/asset/',
    #     data=json.dumps(info).encode('utf-8'),
    #     # json=info
    # )
    #
    # print(response.content,type(response.content))
    # print(response.text,type(response.text))
    # print(response.json(),type(response.json()))
