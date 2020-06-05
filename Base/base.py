# 定义基类
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from Base.driver import Driver


class Base():
    # 定义初始化方法，获取driver
    def __init__(self):
        self.driver = Driver.get_app_driver()

    # 定位单个元素的方法
    def find_ele(self, loc, timeout=5, poll_frequency=1.0):
        # ele = WebDriverWait(self.driver, 10, 0.5).until(lambda x: x.find_element(*loc))
        print("loc的打印结果为：",loc)
        print("timeout的值为：",timeout)
        return WebDriverWait(self.driver, timeout, poll_frequency).until(lambda x: x.find_element(*loc))

    # 定位多个元素的方法
    def find_eles(self, loc, timeout=5, poll_frequency=1.0):
        return WebDriverWait(self.driver, timeout, poll_frequency).until(lambda x: x.find_elements(*loc))

    # 点击元素的方法
    def click_ele(self, loc, timeout=5, poll_frequency=1.0):
        self.find_ele(loc, timeout, poll_frequency).click()

    # 向文本框输入内容的方法
    def send_keys(self, loc, text, timeout=5, poll_frequency=1):
        # 定位元素对象
        ele = self.find_ele(loc, timeout, poll_frequency)
        # 清空内容
        ele.clear()
        # 输入内容
        ele.send_keys(text)


if __name__ == '__main__':
    base = Base()
    path = (By.ID, "com.android.settings:id/search")
    base.click_ele(path)
    time.sleep(1)
    base.driver.quit()












