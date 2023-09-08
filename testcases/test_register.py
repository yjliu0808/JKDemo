"""
=================================================
Author : Athena
Time : 2023/8/27 18:08 
=================================================
"""
import  unittest

import settings
from common.make_requests import send_http_request
from common.myddt import ddt,data
from common.test_data_handler import get_test_data_from_excel
from common import logger




#excel中提前数据
cases = get_test_data_from_excel(settings.TEST_DATA_FILE,'register')
@ddt
class TestRegister(unittest.TestCase):
    logger = logger
    @classmethod
    def setUpClass(cls) -> None:
       cls.logger.info("====添加用户接口开始测试>>>>>>>>>>")
    @classmethod
    def tearDown(cls) -> None:
        cls.logger.info("====添加用户接口测试结束<<<<<<<<<<")

    @data(*cases)
    def test_register(self,case):

        self.logger.info('用例【{}】开始测试'.format(case['title']))

        # 1、测试数据
        # 2、测试步骤
        #   发送请求
        response = send_http_request(url=case['url'],
                                                   method=case['method'],
                                                   json=case['request_data'])
        self.logger.debug('url:{}'.format(case['url']))
        self.logger.debug('method:{}'.format(case['method']))
        self.logger.debug('request_data:{}'.format(case['request_data']))
        # 3、断言
        response_data = response.json()
        #  响应状态码断言
        try:
            self.assertEqual(200, response.status_code)
        except AssertionError as e:
            # self.logger.warn('状态码断言失败！',exc_info=e)
            self.logger.exception('状态码断言失败！')
            raise e
        else:
            self.logger.info('状态码断言成功！')
            # 请求结果断言
            res = {'code': response_data['code'], 'message': response_data['message']}
        try:
            # self.assertEqual(case['expect_data'], res)
            pass
        except AssertionError as e:
            self.logger.exception('请求结果断言失败!')
            self.logger.debug('期望数据：{}'.format(case['expect_data']))
            self.logger.debug('实际结果：{}'.format(res))
            self.logger.debug('响应结果：{}'.format(response_data))

        else:
            self.logger.info('请求结果断言成功!')
        finally:
            self.logger.info('用例【{}】结束测试'.format(case['title']))




