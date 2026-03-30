def outer():
    def inner():
        print("Inside")
    inner()
    print("Outside")
outer()