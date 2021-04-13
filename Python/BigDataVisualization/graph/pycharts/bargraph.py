from pyecharts import Bar
v1 = [70, 85, 95, 64]
v2 = [50, 100, 85, 73]
str1 = ['数学','物理','化学','英语']
bar1 = Bar('柱状图','分数', background_color='blue')
bar1.add('成绩',str1,v1,is_more_utils=True, is_stack=False)
bar1.add('成绩2',str1,v2,is_more_utils=True, is_stack=False)
bar1.render()