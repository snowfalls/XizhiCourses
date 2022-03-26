# 实现从-pi到pi区间的正弦函数区间的曲线图，要求用平滑的曲线进行连接，
# y轴的刻度以0.1为间隔，x轴以0.1为间隔。
import matplotlib.pyplot as plt
import numpy as np

x=np.arange(-np.pi, np.pi, 0.1)
y=np.sin(x)
z=np.cos(x)
plt.plot(x,y)
plt.plot(x,z,color="red")
plt.legend(["sin","cos"], loc="upper right")
xx=np.arange(-np.pi, np.pi, 0.5)
yy=np.arange(-1, 1, 0.1)
plt.xticks(xx,rotation=40)
plt.yticks(yy)
print(xx)
print(yy)
plt.show()