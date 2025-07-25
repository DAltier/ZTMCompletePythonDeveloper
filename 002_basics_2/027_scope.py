a = 1

def confusion():
    a = 5
    return a

print(a) # 1
print(confusion()) # 5

def parent_func():
    #a = 10
    # total = 0
    def local_func():
        return a # here it will check what is the value of a, locally, then parent, then globally and finally in the built in function
    return local_func()

print(parent_func())
print(a)