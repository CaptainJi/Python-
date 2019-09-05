from calculator import *
import unittest

class TestMath(unittest.TestCase):
    #环境准备
    def setUp(self):
        print('Test Start')

    def test_add1(self):
        j = Math(5, 10)
        self.assertNotEqual(j.add(),12)
    def test_assertTrue(self):
        j=Math(5,10)
        self.assertTrue(j.add()>16)

    def test_assertEqual(self):
        j=Math(5,10)
        self.assertEqual(j.add(),12)
    #测试收尾
    def tearDown(self):
        print('Test end')

if __name__=='__main__':
    #构造测试集
    suite=unittest.TestSuite()
    suite.addTest()
    skip=unittest.skip('')
    #运行测试
    runer=unittest.TextTestRunner()
    runer.run(suite)