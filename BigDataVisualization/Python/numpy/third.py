import numpy as np 

a = np.random.rand(4,5)
print(a)
b = np.cumsum(a,0)
c = np.cumsum(a,1)
print(b[3])
print(c[:,4])