f = open("file_h3.txt")
print(f.readline())
print(f.tell())
print(f.readline())
print(f.tell())
f.seek(36)
print(f.readline())
print(f.tell())