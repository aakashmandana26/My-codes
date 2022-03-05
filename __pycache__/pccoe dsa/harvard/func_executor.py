# def func():
    # print("hello")

# a=func
# a()

lst=[]
def trav(string):
    for i in string:
        lst.append(i)
    print(lst)
        
# --executor function
def executor(func):
    func("pneumonoultramicroscopicsilicovolcanoconiosis")

def rev(string):
    print(string[::-1])

def print_len(string):
    print(len(string))

def capital(string):
    print(string.upper())

def count_o(string):
    count=0
    for i in string:
        if(i=='o'):
            count+=1
    print(count)

def sorting(string):
    trav(string)
    print("sorting")
    lst.sort()
    a=''.join(lst)
    print(a)
    
    


executor(print_len)
executor(trav)
executor(rev)
executor(capital)
executor(count_o)
executor(sorting)




