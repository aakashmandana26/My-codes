def translation():
    from PyDictionary import PyDictionary
    dict = PyDictionary()
    x = input("Enter a word to translate:\n")
    trans = dict.translate(x,'de')
    return trans

print(translation())
