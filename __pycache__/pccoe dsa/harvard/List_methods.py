
# -----LIST METHODS-----
# append()	Adds an element at the end of the list
# clear()	Removes all the elements from the list
# copy()	Returns a copy of the list
# count()	Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()	Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()	Removes the element at the specified position
# remove()	Removes the first item with the specified value
# reverse()	Reverses the order of the list
# sort()	Sorts the list
lst = ['21','2','23',24]
lst2 = ['lst2_starts','aksh','sachin',28,26]
print("Append")
lst.append(3)
print(lst)

print("Count")
print(lst.count(3))

print("Extend")
lst.extend(lst2)
print(lst)

print("Index")
print(lst.index(24))

print("Insert")
lst.insert(3,"inserted")
print(lst)

print("Pop")
lst.pop(3)
print(lst)

print("Reversed")
lst.reverse()
print(lst)

lst3 = [2,34,56,23,4,5,565]


lst.clear()
print("Clear")
print(lst)

print("Sort lst3")
lst3.sort()
print(lst3)

print("reverse")
lst3.reverse()
print(lst3)

