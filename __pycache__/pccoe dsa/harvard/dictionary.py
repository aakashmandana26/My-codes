#---------Program to create a dictionay and take input from user and retun its meaning------------

dictionary = {"Dawg" : "Mordern word used to denote a boy", "Simp" : "An innocent person who often gets ditched", "Orchestrated" : "Set up a plan for a desired effect"}
for word in dictionary:
    print(word)
key = input("\nEnter the word to know its meaning: ")
print(dictionary[key])
print("\nThanks for using the dictionary")

#-----Convert dictionary to list, set, tuple------
l = list(dictionary)
s = set(dictionary)
t = tuple(dictionary)
print(l)
print(type(l))
print(s)
print(t)

