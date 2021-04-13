import matplotlib.pyplot as plt 
import numpy as np
plt.rcParams['font.sans-serif']=['SimHei']
plt.title("饼图")
labels='计算机系','机械系','管理系','社科系'
sizes=[45,30,15,10]
explode=(0,0.0,0,0)
explode=(0,0.1,0,0) #set up the distance of the sector
plt.pie(sizes,explode=explode,labels=labels,autopct='%1.1f%%',shadow=False,counterclock=False,startangle=90)
plt.show()