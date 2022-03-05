# Generators in Python

from email import iterators

# 
# iterables -- __iter__() and __getitem__()
# iterators--  __next__()
# iteration


def gen(n):
    for i in range(n):
        yield i
        

a = gen(5)
print(a.__next__())
print(a.__next__())
print(a.__next__())
print(a.__next__())
print(a.__next__())
# print(a.__next__())

for i in a:
    print(i)

b = "akash"
ier = iter(b)
print(ier.__next__())
print(ier.__next__())
print(ier.__next__())




