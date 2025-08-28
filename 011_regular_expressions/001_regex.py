import re

string = "search inside of this text please!"

a = re.search('this',string)
print(a)

# the below 4 commands will give error if the string does not exist.
print(a.span()) # (17, 21)
print(a.start()) # 17
print(a.end()) # 21
print(a.group()) # this

pattern = re.compile('inside')

b = pattern.search(string) # <re.Match object; span=(7, 13), match='inside'>
c = pattern.findall(string) # ['inside']

pattern = re.compile('search inside of this text please!')
d = pattern.fullmatch('search inside of this text please!') # <re.Match object; span=(0, 34), match='search inside of this text please!'>
e = pattern.fullmatch('hello search inside of this text please!')    # this should be exact match, otherwise returns none

print(f"b: {b}")
print(f"c: {c}")
print(f"d: {d}")
print(f"e: {e}")