# booleans

is_cool = True
is_cool = False

print(bool(-0)) # False
print(bool(0)) # False
print(bool(1)) # True
print(bool(0.5)) # True
print(bool('0')) # True
print(bool('True')) # True
print(bool('False')) # True 
print(bool(False)) # False
print(bool('any random thing')) # True

# All values are considered "truthy" except for the following, which are "falsy":
#     None
#     False
#     0
#     0.0
#     0j
#     Decimal(0)
#     Fraction(0, 1)
#     [] - an empty list
#     {} - an empty dict
#     () - an empty tuple
#     '' - an empty str
#     b'' - an empty bytes
#     set() - an empty set
#     an empty range, like range(0)
#     objects for which
#         obj.__bool__() returns False
#         obj.__len__() returns 0