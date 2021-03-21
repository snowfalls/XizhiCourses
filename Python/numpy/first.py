import numpy as np 

a = np.random.rand(3,4)
print(a)
b = np.random.rand(4,3)
print(b)
c = np.matmul(a,b)
print(c)
print(c.shape)