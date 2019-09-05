from selenium import webdriver
from time import sleep


class Login():
    def user_login(self,driver,username,passwd):
        driver.find_element_by_css_selector(
            'body > table.top > tbody > tr > td > table > tbody > tr > td:nth-child(1) > form > input:nth-child(3)').clear()
        driver.find_element_by_css_selector(
            'body > table.top > tbody > tr > td > table > tbody > tr > td:nth-child(1) > form > input:nth-child(3)').send_keys(username)

        driver.find_element_by_css_selector(
            'body > table.top > tbody > tr > td > table > tbody > tr > td:nth-child(1) > form > input:nth-child(4)').clear()
        driver.find_element_by_css_selector(
            'body > table.top > tbody > tr > td > table > tbody > tr > td:nth-child(1) > form > input:nth-child(4)').send_keys(passwd)

        driver.find_element_by_css_selector(
            'body > table.top > tbody > tr > td > table > tbody > tr > td:nth-child(1) > form > input:nth-child(5)').click()
        sleep(2)
    def user_logout(self,driver):
        driver.find_element_by_xpath('/html/body/table[1]/tbody/tr/td/table/tbody/tr/td[1]/a[6]').click()
        driver.switch_to.alert.accept()

if __name__=='__main__':
    username=input('用户名：')
    passwd=input('密码：')

    driver=webdriver.Chrome()
    driver.get('http://localhost')
    driver.implicitly_wait(10)

    Login().user_login(driver,username,passwd)
    sleep(4)
    Login().user_logout(driver)

    sleep(3)
    driver.quit()