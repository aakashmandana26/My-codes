a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
# 
# sum=a+b
# mult=a*b
# rem=a%b
# division=a/b
add = lambda a,b:a+b
multiply = lambda a,b:a*b
remainder = lambda a,b:a%b
divide = lambda a,b:a/b

print("Which operation do you want?\n 1. add\n 2. multiply\n 3. remainder\n 4. divide")
n=int(input("Choose the operation you want to perform:"))
if n==1:
    
    print("Sum is",add(a,b))
elif n==2:
    
    print("multiplication is",multiply(a,b))
elif n==3:
    
    print("% is",remainder(a,b))
elif n==4:
    
    print("division is",divide(a,b))
# 
