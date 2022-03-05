# x = 55 #global
# def abcd(n):
    # print(x+n)
    # global x
    # x=5
    # print(x+n)
# abcd(2)
# print("global ",x)
x = 10
def gef():
    global x
    x = 55
    def xyz():
        global x
        x = 30
        print("Inside xyz()",x)

    print("Before calling xyz()",x)
    xyz()
    print("After calling xyz()",x)
print("global before calling gef()",x)
gef()
print("global",x)
    