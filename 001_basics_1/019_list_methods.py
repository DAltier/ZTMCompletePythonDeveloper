basket = [1,2,3,4,5]

# append
new_list = basket.append(100)
print(basket)
print(new_list) # None, because append modifies the list in place.

# insert
new_list = basket.insert(2,2000)
print(basket)
print(new_list) # None, because insert modifies the list in place.

# extend - takes in a list and adds it to the original one
new_list = basket.extend([45,"hello"])
print(basket)
print(new_list) # None, because extend modifies the list in place.

# pop last item
new_list = basket.pop()
print(basket)
print(new_list) # pop removes the last element by default, but you can specify an index.

# pop item at index
new_list = basket.pop(0)
print(basket)
print(new_list)

# remove
new_list = basket.remove(2000)
print(basket)
print(new_list)

# clear
new_list = basket.clear()
print(basket) # clear removes all elements from the list, making it empty.
print(new_list)