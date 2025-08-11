class MyGen():
    current = 0
    def __init__(self, first, last):
        self.first = first
        self.last = last
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current < self.last:
            num = MyGen.current
            MyGen.current += 1
            return num
        raise StopIteration
    
gen = MyGen(0,10)
print(gen)

for i in gen:
    print(i)

'''
loops by default deal with StopIteration error. they have build in functionality to handle them.
'''