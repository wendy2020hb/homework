from Base.base import Base
from Page.pageElements import PageElements

class SettingPage(Base):

    def __init__(self):
        super().__init__()

    # 点击搜索按钮
    def click_search_btn(self):
        self.click_ele(PageElements.search_btn)