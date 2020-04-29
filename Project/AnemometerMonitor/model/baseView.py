# 封装基础类，如：获取元素、截图
class BaseView(object):
    def __init__(self, driver):
        self.driver = driver

    # 获取元素
    def find_element(self, *loc):
        return self.driver.find_element(*loc)

    # 获取元素集
    def find_elements(self, *loc):
        return self.driver.find_elements(*loc)

