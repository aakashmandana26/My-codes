n = int(input("number of items: "))
# lst = [input(i) for i in range(n)]
lst = []
for i in range(n):
    items=input(f"item:{i+1} = ")
    lst.append(items)
print(lst)
while True:
    
    user = input("how do you want? list or dict or set: ")
    if user == "list":
        c_list = [item for item in lst]
        print(c_list)

    elif user == "set":
        c_set = {item for item in lst}
        print(c_set)

    if user == "dict":
        c_dict = {item:item for item in lst}
        print(c_dict)
    else:
        quit()
    