# 创建driver类
import time

from appium import webdriver


class Driver():
    # 声明手机的driver变量为None
    app_driver = None

    # 定义类方法，创建手机驱动对象
    @classmethod
    def get_app_driver(cls):
        # 创建之前判断驱动是否已存在，不存在则创建
        if not cls.app_driver:
            # 启动参数
            desired_caps = {
                "platformName": "Android",
                "platformVersion": "5.1",
                "deviceName": "sanxing",
                "appPackage": "com.android.settings",
                "appActivity": ".Settings"
            }
            # 创建手机驱动对象
            cls.app_driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
            return cls.app_driver
        else:
            # 已存在则返回原驱动对象
            return cls.app_driver

    # 退出驱动
    @classmethod
    def quit_app_driver(cls):
        # 退出之前判断驱动是否存在，存在则退出，并将driver变量初始化为None
        if cls.app_driver:
            # 退出driver
            cls.app_driver.quit()
            # 初始化为None
            cls.app_driver = None

