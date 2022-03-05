while True:
    n = int(input("Enter a number: "))
    x = n
    fact = 1
    while n > 0:
        fact = fact * n
        n -= 1
    print("Factorial of ", x," is ",fact)







