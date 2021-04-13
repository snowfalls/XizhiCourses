import matplotlib.pyplot as plt
import numpy as np
theta=np.arange(0, 2*np.pi, 0.02)
ax1=plt.subplot(121,projection='polar')
ax1.plot(theta,theta/6,'--',lw=2)
plt.show()