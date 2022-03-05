lst = ["Akash","Muskan","Sachin","Gauri","Yash","Kismat"]

# Without enumerate function
i = 0
for item in lst:
    if (i%2 == 0):
        print(f"Boys are {item}")
    i += 1




# using enumerate function
for index,items in enumerate(lst):
    if(index%2 != 0):
        print(f"Girls are {items}")
    
    







