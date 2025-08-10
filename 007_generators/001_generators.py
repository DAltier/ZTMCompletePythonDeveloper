range(100) # creates elements one by one -> this is a generator
list(range(100)) # creates an entire list in memory

def make_list(num):
	result = []
	for i in range(num): # it creates each individual item before adding it to the list
		result.append(i * 2)
	return result

my_list = make_list(100)
print(my_list)

