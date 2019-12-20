# -*- coding: utf-8 -*-
# __author__ = "maple"


import unittest

class MyTestCase(unittest.TestCase):

    def setUp(self):
        print("用例执行之前要做的事儿")

    def test_case_01(self):
        self.assertEqual(1, 1)

    def tearDown(self):
        print("用例执行之后要做的事儿")
    def test_case_02(self):
        self.assertTrue(0)
    #
    # def test_case_03(self):
    #     self.assertTrue(1)




if __name__ == '__main__':
    # case = MyTestCase(methodName='xxxTest')
    # case.run()
    unittest.main()






