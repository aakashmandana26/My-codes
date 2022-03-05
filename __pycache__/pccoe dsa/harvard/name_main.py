from unittest import main


def fun1(string):
    return(f"You typed {string}")
    
def fun2(n1,n2):
    sum = n1 + n2
    return(f"sum is {sum}")

a = fun2(2,3)
print(a)
print(type(a))
print(fun1("aku"))

print(f"name is {__name__}")
if (__name__ == '__main__'):
    print("This is main function")
    print("this will not be printed if you import anywhere else because its in __main__ function")
