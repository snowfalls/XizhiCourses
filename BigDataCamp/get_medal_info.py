# 爬虫获取数据生成json，然后用json绘图
import requests
from lxml import etree
import os
import json
# 1. 地址(国家体育局统计网站)
url = "http://www.sport.gov.cn/n318/n352/c1001013/content.html"
# 2. 发起请求
response = requests.get(url)
content = response.content.decode()
# 3. 提取数据
html = etree.HTML(content)
# //代表路径的开始
li_list = html.xpath("//div[@class='wz_con']")
country_list = []
# 循环提取信息

US = li_list[0].xpath("./p/span/text()")[1]

countries = li_list[0].xpath("./p/text()")
countries.insert(0,US)

medal_list = []
for country in countries:
    item = {}
    content = country.split()
    item['name'] = content[0]
    item['golden'] = content[1]
    item['silver'] = content[2]
    item['bronze'] = content[3]
    item['total'] = content[4]
    medal_list.append(item)

with open("medal.json", "w", encoding="utf-8") as f:
    # ensure_ascii:允许中文
    # indent：首行缩减
    json.dump(medal_list,f,ensure_ascii=False,indent=2)

# 4. 保存
print("文件保存成功")

