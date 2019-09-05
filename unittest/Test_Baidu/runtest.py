import unittest
from HTMLTestRunner import HTMLTestRunner
import time

test_dir='./test_case'
discovery=unittest.defaultTestLoader.discover(test_dir,pattern="test*.py")

if __name__ == '__main__':
    #定义存放报告的文件夹
    report_dir=r"./test_report"
    #时间格式化
    now=time.strftime('%Y-%m-%d %H_%M_%S')
    #报告文件完整路径
    report_name=report_dir+'/'+now+' result.html'

    #打开文件在报告文件中写入测试结果
    with open(report_name,'wb') as f:
        runner=HTMLTestRunner(stream=f,title='Test Report',description='Test case result')
        runner.run(discovery)
    f.close()
    # runner=unittest.TextTestRunner()
    # runner.run(discovery)