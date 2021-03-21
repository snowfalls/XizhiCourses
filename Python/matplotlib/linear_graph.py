import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
font_set=FontProperties(fname=r"D:\课程材料\字体\simsun.ttc",size=20)
dataX=[1,2,3,4,1]
dataY=[2,4,4,2,2]
plt.plot(dataX, dataY)
plt.title("绘制直线",FontProperties=font_set)
plt.xlabel("X轴",FontProperties=font_set)
plt.ylabel("Y轴",FontProperties=font_set)
plt.show()