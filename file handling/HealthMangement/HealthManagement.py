def getdate():
    import datetime
    x = datetime.datetime.now()
    str_dt = x.strftime("%d %B %H:%M:%S")
    return(str_dt)

def options():
    option = int(input("1. Food    2. Exercise\nPress 1 or 2: "))
    if(option==1):
        f = input("What did you eat?\n")
        return f
    elif(option==2):
        e = input("Which exercise did you do today?\n")
        return e
    else:
        print("Invalid option entered. Go back")
        


while True:
    s = int(input("\n1. Retrieve Data    2.Add Data\nPress 1 or 2: "))
    if(s==1):
        getname = input("Type the name to retrieve his data: ")
        if(getname=='Akash'):
            with open ("akash.txt") as af:
                print(af.read())
            print("------Data retrieved successfully-----")    
        elif(getname=='Sachin'):
            with open ("sachin.txt") as sf:
                print(sf.read())
            print("------Data retrieved successfully-----")    
        elif(getname=='Ritik'):
            with open ("ritik.txt") as rf:
                print(rf.read())
            print("------Data retrieved successfully-----")    
        else:
            print("Invalid. Go back")
    
    elif(s==2):
        name = input("\n1. Akash\n2. Sachin\n3. Ritik\nType the name: ")
        if(name=="Akash"):
            with open ("akash.txt",'a') as af:
                af.write("["+getdate()+"] ")
                # af.write("\n")
                af.write(options())
                af.write("\n")
            print("------Data added successfully-----")    
        elif(name=="Sachin"):
            with open ("sachin.txt",'a') as sf:
                sf.write("["+getdate()+"] ")
                # sf.write("\n")
                sf.write(options())
                sf.write("\n")
            print("------Data added successfully-----")    
        elif(name=="Ritik"):
            with open ("ritik.txt",'a') as rf:
                rf.write("["+getdate()+"] ")
                # rf.write("\n")
                rf.write(options())
                rf.write("\n")
            print("------Data added successfully-----")    
        else:
            print("Invalid option")
        

    

    # def options():

        # option = input("1. Food\n2. Exercise\n")
        # if(option=="Food"):
            # f = input("What did you eat?\n")
            # return f
        # elif(option=="Exercise"):
            # e = input("Which exercise did you do today?\n")
            # return e
        # else:
            # print("Invalid option entered. Go back")
            # 


# if(name=='Akash'):
    # a = open("akash.txt",'r+')
    # a.write("Akash ate "+f)
    # a.write("\Akash did ",+e)
    # 
    # print(a.read())
    # a.close()
    # a.open()
    # print(a.read())
# 
# 
# 
# if(name=="Akash"):
    # options()
    # a = open("akash.txt",'w')
    #  
    # 
    # a.write("I ate "+f)
    # a.write("I did this"+e)
    

    


