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