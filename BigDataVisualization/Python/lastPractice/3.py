# 使用pyqtgraph绘制出y=x^x函数的曲线和y=x^x^x在[-2,2]区间上的曲线
# 并用文字标注其相交的点
import pyqtgraph as pg
import matplotlib.pyplot as plt
import numpy as np

plot = pg.plot()
plot.setWindowTitle('DOTS')

app = pg.mkQApp()
x = np.arange(-2,2,0.01)
y = x**2
z = x**3

plot.plot(x,y,pen='r')
plot.plot(x,z,pen='g')
plot.plot([0,],[0,], symbolSize=10)
plot.plot([1,],[1,], symbolSize=10)
text = pg.TextItem(text='交点1:(0,0)',anchor=(0.5,-0.3),border='w', fill=(0, 0, 255, 100))
plot.addItem(text)
text.setPos(0, 0)
text2 = pg.TextItem(text='交点2:(1,1)',anchor=(0.5,-0.5),border='w', fill=(0, 0, 255, 100))
plot.addItem(text2)
text.setPos(1, 1)


app.exec_()