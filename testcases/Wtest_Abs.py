"""
=================================================
Author : Athena
Time : 2023/8/24 17:02 
=================================================
"""

import unittest
from common.myddt import ddt,data
cases = [
    {'title':'负数','data':-1,'expect_data':1},
    {'title':'0','data':0,'expect_data':0},
    {'title':'正数','data':1,'expect_data':1},
    {'title':'正数100','data':100,'expect_data':100}
]
@ddt
class TestAbs(unittest.TestCase):
    name='测试abs函数'
    def setUp(self):
        print("方法之前执行2")

    def tearDown(self):
        print("方法之后执行3")

    @classmethod
    def setUpClass(cls) :
        print("类之前执行1")

    @classmethod
    def tearDownClass(cls):
        print("测试类之后执行4")

    @data(*cases)
    def test_A(self,case):
        '''

        :return:
        '''
        #1.测试数据
        #2、测试步骤
        res = abs(case['data'])
        #3、断言
        self.assertEqual(case['expect_data'],res)
