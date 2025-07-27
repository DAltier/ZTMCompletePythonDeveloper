class A:
    num = 10

class B(A):
    pass

class C(A):
    num = 1

class D(B,C):     
    pass

print(D.num)

print(D.mro())
print(D.__mro__)
# both the above are same