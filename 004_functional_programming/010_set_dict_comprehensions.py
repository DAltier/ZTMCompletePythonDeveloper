# sets
my_set = {num**2 for num in range(1,11) if num**2 % 2 == 0}
print(my_set)

# dicts
my_dict = {num:num**2 for num in range(1,11)}
print(my_dict)

my_dict_2 = {num:num**2 for num in [1,2,3]}
print(my_dict_2)

random_dict = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4
    }

my_new_dict = {k:v**2 for k,v in random_dict.items()}
print(my_new_dict)

my_new_dict2 = {k:v**2 for k,v in random_dict.items() if v % 2 == 0}
print(my_new_dict2)