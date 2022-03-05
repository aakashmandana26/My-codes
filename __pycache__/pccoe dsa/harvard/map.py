# lst = ['aks','sachin',21,22,54]
# for i in range(5):
    # n = input(f"{i+1}th element: ")
    # lst.append(n)
# print(f"Final list : {lst}")

lst = ['21','22','23']


# without map() function
# for i in range(len(lst)):
    # lst[i]=int(lst[i])
# print(lst)



# with map() function

numbers = map(int,lst)
# print(numbers)
nums = list(numbers)
print(nums)


# map function for square of numbers
def sq(a):
    return(a*a)

square = map(sq,nums)
square_num = list(square)
print(square_num)

def sqrt(b):
    return(b**(1/2))

sqroot = map(sqrt,square_num)
sqrt_num = list(sqroot)
print(sqrt_num)

# squares using lambda and map
l_sq = map(lambda a:a*a,nums)
print(list(l_sq))




