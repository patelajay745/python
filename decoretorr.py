def dec1(func1):
    def nowexec():
        print("Executing now")
        func1()
        print("Executed")  
    return nowexec

@dec1
def who_is_ajay():

    print("Ajay is devsops Engineer")


who_is_ajay()

    