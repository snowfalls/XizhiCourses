#利用数组打印出杨辉三角形的前n行
#涉及的知识 数组 循环 python的输入 lambda表达式3

def generate(numRows):
    r = [[1]]
    for i in range(1,numRows):
        r.append(list(map(lambda x,y:x+y, [0]+r[-1],r[-1]+[0]))) #need to be checked
    return r[:numRows]
    
n=input("请输入一个整数以生成杨辉三角形:")
a=generate(int(n))
for i in a:
    print(i)