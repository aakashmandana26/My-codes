def searcher():
    import time
    print("Start searching")
    book = "Hi I am Akash, I am a human being."
    time.sleep(4)
    
    while True:
        text = (yield)
        if(text in book):
            print("Text Present")
        else:
            print("Text not present")

search = searcher()
next(search)
search.send("Akash")
search.send("no")
