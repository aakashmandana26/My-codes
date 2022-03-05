import datetime

def getdate():
    return datetime.datetime.now()
a = getdate()
b = "Datetime cannot be printed as it is not a string"
f = open("file_h1.txt",'r+')
content = f.read()
print(content)
# a = "\na is a string"
# f.write(b)
# f.write(a)
content = f.read()

print(content)
# f.write("\nNow I am serious")
# content = f.read()
# print(content)
# print(f.readline())
# for line in f:
    # print(line)
# f.close()
