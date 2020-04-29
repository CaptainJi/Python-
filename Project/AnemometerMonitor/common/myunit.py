import unittest
from driver import *


class StartEnd(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = browser()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def setDown(self):
        self.driver.quit()
