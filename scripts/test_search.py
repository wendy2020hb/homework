from Base.analysysData import AnalysisData
from Base.driver import Driver
from Base.page import Page
import pytest


# 解析数据方法 -先在data临时见一个py文件 方便解析数据
def get_data():
    # 存储测试数据
    data_list = []
    # 获取yaml文件数据
    data = AnalysisData.get_yaml_data("search.yml")
    for i in data.values():
        data_list.append((i.get("input"), i.get("exp")))
    return data_list


class TestSearch:

    def teardown_class(self):
        Driver.quit_app_driver()

    # 只需点击一次搜索按钮，所以将其设为类级别的工厂函数
    @pytest.fixture(scope="class", autouse=True)
    def click_search_btn(self):
        # 点击搜索按钮
        Page.get_setting_page().click_search_btn()

    @pytest.mark.parametrize("input_text,search_text", get_data())
    def test_search(self, input_text, search_text):
        # 在输入框中输入内容
        Page.get_search_page().send_search_text(input_text)
        # 获取搜索结果
        results = Page.get_search_page().get_search_results()
        # 断言搜索结果
        assert search_text in results