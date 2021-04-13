import numpy as np 
import matplotlib.pyplot as plt 
plt.rc("font", family='SimHei', size=15)
plt.title("男女爱好人数分布图")
num=np.array([14325, 9403, 13227, 18651])
ratio=np.array([0.75,0.6,0.22,0.1])
men=num*ratio
women=num*(1-ratio)
x=['足球','游泳','看剧','逛街']
width=0.5
idx=np.arange(len(x))
plt.bar(idx,men,width,color='red',label='男性用户')
plt.bar(idx,women,width,bottom=men,color='gray',label='女性用户')
plt.xlabel('应用类别')
plt.ylabel('男女分布')
plt.xticks(idx+width/2, x, rotation=40)
for a,b in zip(idx,men):
    plt.text(a,b+0.05,'%.0f' % b, ha='center', va='bottom', fontsize=12)
for a,b,c in zip(idx,women,men):
    plt.text(a,b+c+0.5, '%.0f'%b, ha='center',va='bottom',fontsize=12)
plt.legend()
plt.show()