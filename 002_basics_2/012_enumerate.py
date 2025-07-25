for char in enumerate('Hello World'):
    print(char)
    
for index, item in enumerate([1,2,3,4]):
    print(index, item)

for index, item in enumerate(range(0, 100)):
    if item == 50:
        print(f"index of 50 is {index}")

for i in enumerate((1,2,3,4,5)):
    print(i)

print(list(item for item in enumerate('123456789')))

print(list(enumerate('123456789')))

print(dict(list(enumerate((i * i for i in range(1,11)),1))))