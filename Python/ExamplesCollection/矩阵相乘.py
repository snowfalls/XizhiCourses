def matrix():
    m = int(input("请输入矩阵的行数:"))
    n = int(input("请输入矩阵的列数:"))
    arr = []
    for i in range(m):
        arr.append([])
        for j in range(n):
            x = int(input("请输入"))
            arr[i].appen(x)
    return arr

a = matrix()
b = matrix()
c = []

if(len(a[0] == len(b) and len(a) == len(b[0]))):
    for i in range(len(a)):
        c.append([])
        for j in range(len(b[0])):
            s = sum(a[i][k] * b[k][j] for k in range(len(b)))
            c[i].append(s)
    print(c)
else:
    print("输入的矩阵维度不匹配")
