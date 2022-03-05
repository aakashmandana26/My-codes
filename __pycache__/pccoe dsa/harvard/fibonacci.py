# 0,1,1,2,3,5,8,13...

def fibonacci(n):
    if(n==1): 
        return 0
    elif(n==2):
        return 1
    else:
        fib = fibonacci(n-1) + fibonacci(n-2)
        return fib
print(fibonacci(6))

    
    
    
    
    




     
  
  
  

