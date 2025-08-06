def hello(func):
	func()

def greet():
	print("hello!")
       
a = hello(greet)
print(a)