#-----Iterative method-------
def factorial(n):
    fact = 1
    for i in range(n):
        fact = fact * (i+1)
    print("The factorial of",n,"is",fact)
factorial(5)

#------Recursive method-------
def factorial2(n):
    if(n==0 or n==1):
        return 1
    else:
        fact = n * factorial2(n-1)
        return fact
factorial2(6)
print("The factorial is",factorial2(6))
    



    



