from functools import reduce
num = []
for i in range(10):
    num.append(i)

sum = reduce((lambda x,y : x+y),num)
print(sum)

