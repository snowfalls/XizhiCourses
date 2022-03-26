# 将整块绘图区域分割为4个区域，分别绘制出x=[0,1,2,3,4]和y=[5,8,7,6,3]
# 数据对应的折线图，条形图，直方图和散点图
import matplotlib.pyplot as plt
fig,ax=plt.subplots(2,2)

x=[0,1,2,3,4,5,6,7,8,9]
y=[5,8,7,6,3,10,9,2,7,9]
ax[0,0].plot(x,y)
ax[0,1].bar(x,y)
ax[1,0].hist(y,bins=4)
ax[1,1].scatter(x,y)
plt.show()