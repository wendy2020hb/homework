from Base.base import Base
from Page.pageElements import PageElements

class SearchPage(Base):
    def __init__(self):
        super().__init__()


    # 输入搜索内容
    def send_search_text(self, text):
        self.send_keys(PageElements.search_input, text)

    # 获取搜索结果
    def get_search_results(self):
        results = self.find_eles(PageElements.search_result)
        return [i.text for i in results]