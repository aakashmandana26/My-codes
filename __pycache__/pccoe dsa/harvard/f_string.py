# -----------Fstring-----------
a = "Akash"
b = "Sachin"

# print("I am %s"%a)
# print("We are %s, %s"%(a,b))
c = "We are {1},{0}"
d = c.format(a,b)
print(d)

# ---------Fstring-------------
e = f"We are {a} and {b}. Our fav no. is {int(21/3)}"
print(e)
