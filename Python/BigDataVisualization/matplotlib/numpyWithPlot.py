import matplotlib.pyplot as plt
import numpy as np 
x = np.arange(10)
y = np.sin(x)
z = np.cos(x)
plt.plot(x,y,marker="*",linewidth=3,linestyle="--",color="red")
plt.plot(x,z)
plt.title("matplotlib")
plt.xlabel("x")
plt.ylabel("y")
plt.legend(["Y","Z"],loc="upper right")
plt.grid(True)
plt.show()