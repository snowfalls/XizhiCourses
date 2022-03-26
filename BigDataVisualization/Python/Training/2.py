import numpy as np 
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['Microsoft YaHei']
GDP=[32679,30320,20363,18809]
plt.bar(range(4),GDP,align='center',color='red',alpha=1)
plt.ylabel("GDP")
plt.title('2018年四个直辖市的GDP对比')
plt.xticks(range(4),['上海市','北京市','重庆市','天津市'])
plt.ylim([10000,35000])
plt.show()