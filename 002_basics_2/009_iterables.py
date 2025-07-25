# iterable - list, dictionary, tuple, set, string

user = {'name': "john", 'age': 45, 'can_swim': False}

for i in user:
    print(i)

for i in user.keys():
    print(i)

for i in user.values():
    print(i)

for i in user.items():  #it stores each pair as tuple, in a list (in a dict_items class).
    print(i)

# dict_items([('name', 'john'), ('age', 45), ('can_swim', False)])
print(user.items())
print(type(user.items()))
print(list(user.items()))

for k,v in user.items():
    print(k,v)

for i in user.items():
    k,v=i
    print(k,v)