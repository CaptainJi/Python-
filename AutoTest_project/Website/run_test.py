import unittest
from function import *
from BSTestRunner import BSTestRunner
import time

report_dir='./test_report'
test_dir='./test_case'

print('开始运行测试用例')
discover=unittest.defaultTestLoader.discover(test_dir,pattern='test_login.py')

now=time.strftime('%Y-%m-%d %H_%M_%S')
report_name=report_dir+'/'+now+'result.html'

print('开始生成报告……')
with open(report_name, 'wb') as f:
    runner=BSTestRunner(stream=f,title='测试报告',description='登录测试')
    runner.run(discover)
    f.close()

print('查找最新的报告')
latest_report=latest_report(report_dir)

# print('发送报告邮件……')
send_mail(latest_report)

# print('完成')
