lst = [21,32,45,76,43,56]

def greater_30(num):
    return num>30
# Filter function will filter the list or iterables and remove all false value and return all true values
# since 21>30 is false it got removed.
gr = list(filter(greater_30,lst))
print(gr)

# using lambda
gr2 = list(filter(lambda a:a>30,lst))
print(gr2)



# filter() to filter all sqaures value from 1 to 1000
def check_sq(num):
    sqrt = num**(1/2)
    if(sqrt - int(sqrt) == 0):
        return True
lst = []
for i in range(1,1000):
     lst.append(i)

sq_list = list(filter(check_sq,lst))
print(sq_list)


# map function
sqrt_list = list(map(lambda x:int(x**(1/2)),sq_list))
print(sqrt_list)
print(sqrt_list[-1])