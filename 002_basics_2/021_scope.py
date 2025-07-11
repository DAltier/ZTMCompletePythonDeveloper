a = 1

def parent_func():
    #a = 10
    # total = 0
    def local_func():
        return a
        return sum  # here it will check what is the value of sum, locally, then parent, then globally and finally in the built in function
    return local_func()

print(parent_func())
print(a)