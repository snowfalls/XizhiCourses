from pyecharts import Gauge
gauge = Gauge("仪表盘图例")
gauge.add("业务指标", "完成率", 90)
gauge.render()