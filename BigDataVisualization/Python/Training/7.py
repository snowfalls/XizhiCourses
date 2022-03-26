import numpy as np 
import matplotlib.pyplot as plt
x=np.linspace(0,10,100)
y=2*np.cos(x)**5 + 3*np.sin(x)**3
fig, axes=plt.subplots(2,3,figsize=(10,6),facecolor='#ccddef')
fig.suptitle('Photo',fontsize=20)
axes[0,0].plot(x,y)
axes[0,1].bar(x,y*y)
axes[0,2].hist(y,bins=30)
axes[1,0].scatter(x,y)
axes[1,1].barh(x,y)
axes[1,2].pie([1,2,3,4,5],labels=['A','B','C','D','E'])
ax1=axes[0,0]
ax1.set(xlim=[-10,12],ylim=[-6,4],facecolor='#ffeedd')
ax1.grid(True)
fig.subplots_adjust(left=0.2,bottom=0.1,right=0.8,top=0.8,hspace=0.5)
plt.show()