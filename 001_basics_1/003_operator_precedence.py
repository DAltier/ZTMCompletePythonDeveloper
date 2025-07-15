# operator precedence

print(20 - 3 * 4) # 8

# ()
# **
# * /
# + -

print((5 + 4) * 10 / 2) # 45.0

print(((5 + 4) * 10) / 2) # 45.0

print((5 + 4) * (10 / 2)) # 45.0

print(5 + (4 * 10) / 2) # 25.0

print(5 + 4 * 10 // 2) # 25