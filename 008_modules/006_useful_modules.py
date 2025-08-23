from collections import Counter, defaultdict, OrderedDict

li = [1,2,3,4,5,6,7,7]
print(Counter(li)) # Counter({7: 2, 1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1})
# sentence = 'blah blah blah thinking about python'
# print(Counter(sentence)) # Counter({'h': 5, ' ': 5, 'b': 4, 'a': 4, 'l': 3, 't': 3, 'n': 3, 'i': 2, 'o': 2, 'k': 1, 'g': 1, 'u': 1, 'p': 1, 'y': 1})

dictionary = {'a': 1, 'b': 2}
print(dictionary['a'])
dict2 = defaultdict(lambda: 'does not exist', {'a': 1, 'b': 2})
print(dict2['c']) # does not exist

d = OrderedDict()
d['a'] = 1
d['b'] = 2

d2 = OrderedDict()
d2['a'] = 1
d2['b'] = 2

print(d == d2) # True