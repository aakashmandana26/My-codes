# using with block , it opens and closes the file by itself
with open("file_h3.txt") as f:
    print(f.readline())
    print(f.readline())
    # print(f.readline())
try:
    print(f.readline())
except Exception as e:
    print(e)
    print("Error : 'With' block has closed the file, so you cant read the line again unless you open the file again\n")
f = open("file_h3.txt")
print(f.readline())
