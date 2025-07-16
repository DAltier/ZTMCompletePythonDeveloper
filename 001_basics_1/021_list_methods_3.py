basket = ['a', 'x', 'b', 'c', 'd', 'e', 'd']

print(basket.sort())
print(basket)

print(basket.reverse())
print(basket)

print("Sorted function")
print(sorted(basket))   # it creates a new list that is sorted
print(basket)

new_li = basket.copy()   # same as doing new_li = li[:]
print(new_li)
