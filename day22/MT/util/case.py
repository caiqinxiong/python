"""
1. 获取用例列表
2. 循环每个用例
    1. 从字段中取出相应的数据,发请求
    2. 处理请求结果
    3-1. 做断言
    3-2. 修改数据库字段
    4. 生成测试报告
    5. 给前端返回测试报告
"""
import json
import requests
import unittest
import os
from MT.settings import BASE_DIR
from HTMLTestRunner import HTMLTestRunner
from app01 import models

class MyCaseTest(unittest.TestCase):

    def runTest(self):
        self.assertEqual(self.a, self.b)


class Worker(object):

    def __init__(self, case, case_list=[]):
        self.case = case
        self.case_list = case_list

    def handle(self):
        """ 负责所有的操作 """
        # 1. 发请求
        res = self.send_msg()
        # 2. 生成用例
        self.create_report(res)


    def update_data(self, res):
        """ 更新数据库"""
        status = res[-1]['status']
        if status:  # 断言成功
            models.Case.objects.filter(pk=self.case.pk).update(
                case_execute_status=1
            )



    def create_report(self, res):
        """ 生成测试用例 """

        # ({'success': True}, {'success': True}, {'status': 1})
        print(33333333333333333, res)
        case_obj = MyCaseTest()
        case_obj.a, case_obj.b, _ = res
        self.case_list.append(case_obj)

    def send_msg(self):
        """ 发送请求 """
        # print(self.case)
        response = requests.request(
            method=self.case.case_method,
            url=self.case.case_url,
            # params=self.case.case_params
        )
        content_type = response.headers['Content-Type']
        # content_type = content_type.split(';')[0].split("/")[-1]
        if ';' in content_type:
            content_type = content_type.split(';')[0].split("/")[-1]
        else:
            content_type = content_type.split("/")[-1]
        if hasattr(self, '_check_{}'.format(content_type)):
            res = getattr(self, '_check_{}'.format(content_type))(response)
        # print(3333333, res)
        return res
    def _check_json(self, response):
        """" 处理json类型的响应结果 """
        response = response.json()
        # print(111111, response)
        case_expect = json.loads(self.case.case_expect)
        # print(222222, case_expect)
        res = None
        for k in case_expect:
            if case_expect[k] != response[k]:
                res = ({k:case_expect[k]}, {k:response[k]}, {"status":0})
                break
        else:
            res = ({k: case_expect[k]}, {k: response[k]}, {"status":1})  # 用例通过
        return res
    def _check_params(self):
        """ 处理请求携带的参数 """
        # self.case.case_params
        pass


def report(l):
    """  生成测试用例报告 """
    suite = unittest.TestSuite()
    suite.addTests(l)
    file_path = os.path.join(BASE_DIR, 'static', 'report', 'report.html')
    f = open(file_path, 'wb')
    HTMLTestRunner(
        stream=f,
        title='用例报告',
        description="用例报告描述",
        verbosity=2
    ).run(suite)

    return file_path

def run(case_list):
    """ 处理发请求和返回数据 """
    l = []
    for case in case_list:
        Worker(case, l).handle()

    return report(l)


if __name__ == '__main__':
    res = requests.request(method='get', url='https://cnodejs.org/api/v1/topics')
    print(res.headers)
    res = requests.request(method='get', url='https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1577018852541&di=6f5e8123755af7dea48bf5effef679eb&imgtype=0&src=http%3A%2F%2Fa2.att.hudong.com%2F54%2F18%2F01300000166733121170184850746.jpg')
    print(res.headers)