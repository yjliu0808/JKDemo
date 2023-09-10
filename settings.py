"""
=================================================
Author : Athena
Time : 2023/9/3 16:59 
=================================================
"""
import  os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
#日志模块
LOG_CONFIG = {
    'name': 'mall',
    'filename':os.path.join(BASE_DIR,'logs/mall.log'),
    'mode':'a',
    'debug': 'true',
    'encoding':'utf-8'
}
#测试数据配置
TEST_DATA_FILE = os.path.join(BASE_DIR,'resource/testcase.xlsx')

REPORT_CONFIG = {
    'description':'mall商城',
    'filename':'reports/mall.html'
}
if __name__ == '__main__':
    print(BASE_DIR)
    print(TEST_DATA_FILE)
    print(REPORT_CONFIG.values())
