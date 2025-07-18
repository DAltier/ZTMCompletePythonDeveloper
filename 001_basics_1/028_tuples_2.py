my_tuple = (1,2,3,4,5,2)

print(my_tuple[1:2])    # be careful here, we also get a 'comma' when we just store a single tuple value
print(my_tuple[0:2])
print(my_tuple[::-2])


a,b,c,*other = (1,2,3,4,5,6,7,8,9)  # it stores as list if the variable has more than 1 item, otherwise as int.
print(a)
print(type(a))
print(other)
print(type(other))


print(my_tuple.count(2))
print(my_tuple.index(5))