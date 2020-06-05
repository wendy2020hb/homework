import os

import yaml
# 读取yaml文件
with open("./bb.yaml", "r", encoding='utf-8') as f:
    # 解析yaml文件，返回字典
    data = yaml.safe_load(f)
    print("读取yaml文件返回的数据类型为：", type(data))
    print("返回数据为：", data)