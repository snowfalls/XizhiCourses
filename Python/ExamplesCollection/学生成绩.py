# 1.某学校的期末考试结束，并统计出了现在的所有同学的成绩现在需要对学生成绩进行分级，通过python编程实现, 
# 将学生的成绩分类为A、B、C，分别对应高于80,60~80之间的成绩，以及60分以下的成绩。并打印出60分以下成绩同学对应的索引。

import numpy as np 

student_mark = np.random.randint(50,100,size=100) #generate the random number from 50~100 size=100
print("student_marks:\n", student_mark)
b = []
c = []
index = 1
for i in student_mark:
    if (i >= 90):
        b.append('A')
    elif (i < 60):
        b.append('C')
        c.append(index)
    else:
        b.append('B')
    index += 1

print("mark level:\n", b)
print("low marks:\n", c)