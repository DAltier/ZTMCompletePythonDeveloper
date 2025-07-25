i = 0
while i < 50:
    print(i)
    break

i = 0
while i < 5:
    print(i)
    i += 1
else:
    print("done")
    
while True:
    response = input("say something: ")
    if (response == 'bye'):
        break