
'''
unittest

'''




import requests
import unittest
from HTMLTestRunner import HTMLTestRunner
response = requests.get('https://www.v2ex.com/api/site/info.json')
# print(response.json()['title'])

class MyCase(unittest.TestCase):

    def test_case_01(self):
        self.assertEqual(response.json()['title'], 'V2EX')
        # self.assertEqual(response.json()['slogan'], '222222way to explore')

    # def test_case_02(self):
    #     self.assertEqual(response.json()['title'], 'V2Ee')


if __name__ == '__main__':
    # unittest.main()
    suite = unittest.makeSuite(MyCase)
    # print(1111111, suite)
    f = open('report.html', 'wb')
    HTMLTestRunner(
        stream=f,
        title='测试用例报告的title',
        description="描述xxxxxxxxx",
        verbosity=2
    ).run(suite)


