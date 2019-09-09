import unittest
from model import function,myunit
from page_object.LoginPage import *
from time import sleep

class LoginTest(myunit.StartEnd):
    # 用户名与密码正确的情况
    def test_login1_normal(self):
        print('test_login1_normal 开始测试')
        po=LoginPage(self.driver)
        po.Login_action('test','123456')
        sleep(2)

        self.assertEqual(po.type_loginPass_hint(),'我的空间')
        function.insert_img(self.driver,'test_login1_normal.png')
        print('测试结束')

    # 用户名正确密码错误
    def test_login2_passwdError(self):
        print('test_login2_passwdError 开始测试')
        po=LoginPage(self.driver)
        po.Login_action('test','1')
        sleep(2)

        self.assertEqual(po.type_loginFail_hint(),'')
        function.insert_img(self.driver,'test_login2_passwdError.png')
        print('测试结束')

    #用户名密码为空
    def test_login3_empty(self):
        print('test_login3_empty 开始测试')
        po=LoginPage(self.driver)
        po.Login_action('','')
        sleep(2)

        self.assertEqual(po.type_loginFail_hint(),'')
        function.insert_img(self.driver,'test_login3_empty.png')
        print('测试结束')
if __name__ == '__main__':
    unittest.main()