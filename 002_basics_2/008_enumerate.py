for i in enumerate('Hello World'):
    print(i)
    
for i,j in enumerate([1,2,3,4]):
    print(i,j)

for i in enumerate((1,2,3,4,5)):
    print(i)

print(list(item for item in enumerate('123456789')))
print((i * i for i in range(8)))

print(list(enumerate('123456789')))

print(dict(list(enumerate((i * i for i in range(1,11)),1))))