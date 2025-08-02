import functools

my_list = [1,2,3,4,5]

# multiply by 2
print(list(map(lambda item: item*2, my_list)))

# keep only odd numbers
print(list(filter(lambda item: item % 2 != 0, my_list)))

# reduce 
print(functools.reduce(lambda acc,item: item+acc, my_list))

'''
syntax:
lambda param: action(param)
it automatically returns the action taken,
it does not have any name, doesn't get stored in the memory.
and so used only once.
and behaves exactly like a function.
'''