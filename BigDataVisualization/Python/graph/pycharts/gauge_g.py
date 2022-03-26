from pyecharts import Gauge
gauge = Gauge("仪表盘图")
gauge.add("业务指标","完成率", 80)
gauge.render()