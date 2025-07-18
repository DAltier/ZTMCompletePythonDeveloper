my_tuple = (1,2,3,4,5,2)
# my_tuple[0] = 4     # it will be an error, because tuple are immutable

print(my_tuple)
print(my_tuple[0])
print(5 in my_tuple)

my_dict = {"age": 45, (1,2): "hello"}
print(my_dict)
print(my_dict.items())   # returns key:value pair as a tuple
print(my_dict[(1,2)])
