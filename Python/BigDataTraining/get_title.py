import requests
from lxml import etree
import os
import json
# 1. 地址(国家体育局统计网站)
url = "http://www.xueti.com/chengkao/50096.html"
# 2. 发起请求
response = requests.get(url)
content = response.content.decode()
# 3. 提取数据
html = etree.HTML(content)
# //代表路径的开始
title = html.xpath("//img/@title")
print(title)