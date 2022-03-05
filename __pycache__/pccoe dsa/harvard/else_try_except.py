global f1 
def exec():
    print("Executing...")
    f1 = open('akash.txt') 
                   #This file exists
    # f = open ('sbdvhgcdh.txt')            #This file doesnot exists

    print("Executed")
    f1.close()


try:
    exec()
except Exception as e:
    print(e)

else:                                      #else and except doesnot run together
    print("This will run only if except does not run")
finally:
    print("done")
    
    
    

print("done2")