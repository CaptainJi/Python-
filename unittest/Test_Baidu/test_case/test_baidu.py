from selenium import webdriver
import unittest
from time import sleep

class TestBaidu(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.get('http://www.baidu.com')

    def test_baidu(self):
        driver=self.driver
        driver.find_element_by_id('kw').clear()
        driver.find_element_by_id('kw').send_keys('Selenium')
        driver.find_element_by_id('s').click()
        sleep(3)

        title=driver.title
        self.assertEqual(title,'Selenium_百度搜索')

        driver.find_element_by_link_text('Selenium(浏览器自动化测试框架)_百度百科').click()
        sleep(5)

    def tearDown(self) -> None:
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()