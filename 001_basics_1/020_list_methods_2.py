basket = ['a','b','c','d','e','d']

print(basket.index('d')) # if that value is not there in the list, then it will throw an error and program will stop running.

# lookup:start:stop
print(basket.index('d',0,4))

print('a' in basket) # we use this to avoid the error.
print('x' in basket)

name = 'dana'
print('d' in name) # we can use this with strings as well

print(basket.count('d'))