def dict():
    from PyDictionary import PyDictionary
    dictionary=PyDictionary()
    x=input("Enter the word you want to search\n")
    ans = dictionary.meaning(x)
    return ans
print(dict())
