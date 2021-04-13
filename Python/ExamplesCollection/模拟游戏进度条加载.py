# 这个例子通过模拟一个程序加载进度来实例for循环和print函数的使用方法
import time
import os

scale=100
print("----游戏加载----")
for i in range(scale+1):
    os.system("cls") #清空屏幕
    star='*'*i
    dot='.'*(scale-i)
    percentage=scale+1
    print("{:^3.0f}%[{}->{}]".format(i,star,dot))    
    time.sleep(0.1)
print("----执行结束----")