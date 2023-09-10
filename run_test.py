"""
=================================================
Author : Athena
Time : 2023/8/20 13:15 
=================================================
"""
import  unittest

import settings

from BeautifulReport import BeautifulReport

if __name__ == '__main__':
    # 1、收集用例并返回 测试套件，testcases用例文件夹，返回能够找到的所有用例，封装成一个测试套件
    ts = unittest.TestLoader().discover('testcases')
    # 运行器运行并生成报告
    # with open('reports\mall项目接口测试报告.html','wb') as f:
    #     runner = HTMLTestRunner(stream=f)
    #     runner.run(ts)
    br = BeautifulReport(ts)
    # br.report(description='mall项目',filename = 'reports/mall接口测试报告.html')
    # ts = unittest.TestLoader().discover('testcases')
    # br = BeautifulReport(ts)
    # br.report(**config['report'])
    br.report(**settings.REPORT_CONFIG)