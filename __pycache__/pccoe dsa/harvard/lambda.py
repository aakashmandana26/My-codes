#------lambda is used to make a 1 liner function----- 

# minus = lambda x,y:x%y  
# a = minus(9,5)
# print(a)
def a_first(a):
    return a[1]


a = [[1,664],[3,88],[6,32]]
b = a.sort(key=a_first)
print(a)

sum = lambda x,y,z : x+y+z
print(sum(3,4,6))