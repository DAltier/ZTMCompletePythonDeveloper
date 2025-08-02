# square
my_list = [5, 4, 3]

new_list = list(map(lambda item: item ** 2, my_list))
print(new_list)

# list sorting
a = [(4, 3), (0, 2), (10, -1), (9, 9)]
a.sort(key = lambda x: x[1])
print(a)