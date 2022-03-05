

def func1(func2):
    def exec():
        print("Executing now...")
        func2()
        print("Execution Successful")
    return exec()


@func1
def akash():
    print("I am Akash")


# akash = func1(akash)



