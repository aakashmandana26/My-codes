# a = ["Akash","Sachin","Ritik"]
def func_print(normal,*args,**kwargs):
    print(normal,args)
    print(type(args))
    print(normal)
    for item in args:
        print(item)
    for key,value in kwargs.items():
        print(f"{key} was born on {value}")

a = ["Akash","4",3,"Sachin","Ritik","Yash"]
kw = {"Muskan": 31,"Gauri" : 25,"Kismat" : 24}
print(type(a))
normal = 34
func_print(normal,*a,**kw)
# print(type(a))