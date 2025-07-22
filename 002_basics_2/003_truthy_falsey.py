# truthy
print(bool('hello'))
print(bool(5))

# falsey
print(bool(''))
print(bool(0))
print(bool(None))

password = '123'
username = 'johnny'

if username and password:
	print('welcome')