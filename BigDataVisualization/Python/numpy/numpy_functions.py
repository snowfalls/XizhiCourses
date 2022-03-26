import numpy as np 
a = [1,3,5,7,9]
b = [2,4,6,8,10]
c = np.dot(a, b) #计算点积
d = np.vdot(a, b)
print("点积", c)
print("向量点积", d)
e = np.inner(a, b)
print("向量内积", e)


matrix=np.array([[1,2], [3,4]])
f = np.linalg.inv(matrix)
print("矩阵的逆矩阵\n",f)
g = np.diff(matrix, 1)
print("沿指定轴的离散差分\n", g)
h = np.diff(matrix, 0)
print("沿指定轴的离散差分\n", h)
t = np.cross(matrix, matrix)
print("叉积\n", t)

matrix = np.array([[1,2,3], [4,5,6], [7,8,9]])
a1 = np.prod(matrix, 0)
print("第0轴的数组乘积", a1)
a2 = np.prod(matrix, 1)
print("第1轴的数组乘积", a2)

b1 = np.cumprod(matrix, 0)
print("第0轴的数组乘积", a1)
b2 = np.cumprod(matrix, 1)
print("第1轴的数组乘积", a2)

arr = np.array([1,3,5,7,9])
c = np.gradient(arr)
print("数组梯度\n", c)