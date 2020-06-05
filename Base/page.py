from Page.settingPage import SettingPage
from Page.searchPage import SearchPage

# 管理所有页面类
class Page:

    # 返回设置页面实例化对象
    @classmethod
    def get_setting_page(self):
        return SettingPage()

    @classmethod
    # 返回搜索页面实例化对象
    def get_search_page(self):
        return SearchPage()