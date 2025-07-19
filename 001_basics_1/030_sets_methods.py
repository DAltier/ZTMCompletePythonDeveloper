# this is very similar to Venn diagrams.

my_set = {1,2,3,4,5}
your_set = {4,5,6,7,8,9,10}

# .difference()
print(my_set.difference(your_set))
print(my_set)

# .discard()
print(my_set.discard(5))
print(my_set)

# .difference_update()
print(my_set.difference_update(your_set))
print(my_set)

my_set = {1,2,3,4,5}

# .intersection()
print(my_set.intersection(your_set))
print(my_set & your_set)

# .isdisjoint()
print(my_set.isdisjoint(your_set))
my_set = {1,2,3}
print(my_set.isdisjoint(your_set))

# .issubset()
print(my_set.issubset(your_set))
my_set = {4,6,8}
print(my_set.issubset(your_set))

# .issuperset()
print(my_set.issuperset(your_set))
print(your_set.issuperset(my_set))

# .union()
my_set = {1,2,3,4,5}
print(my_set.union(your_set))
# or
print(my_set | your_set)