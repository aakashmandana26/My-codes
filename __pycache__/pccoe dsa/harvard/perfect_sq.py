def check_sq(num):
    sqrt = num**(1/2)
    if(sqrt - int(sqrt) == 0):
        return True
    

a = check_sq(9)
print(a)
# print(type(a))
# print(a - int(a))