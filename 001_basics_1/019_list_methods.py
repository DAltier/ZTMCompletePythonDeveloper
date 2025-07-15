print("\nappend")
li = [1,2,3,4,5]
new_li = li.append(100)
print(li)
print(new_li) # None, because append modifies the list in place.

print("\ninsert")
new_li = li.insert(2,2000)
print(li)
print(new_li) # None, because insert modifies the list in place.

print("\nextend")
new_li = li.extend([45,"hello"])
print(li)
print(new_li) # None, because extend modifies the list in place.

print("\npop")
new_li = li.pop()
print(li)
print(new_li) # pop removes the last element by default, but you can specify an index.

print("\npop")
new_li = li.pop(0)
print(li)
print(new_li)

print("\nremove")
new_li = li.remove(2000)
print(li)
print(new_li)

print("\nclear")
new_li = li.clear()
print(li) # clear removes all elements from the list, making it empty.
print(new_li)