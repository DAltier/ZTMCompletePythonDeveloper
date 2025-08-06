# decorator
def my_decorator(func):
	def wrap_func():
		print("***********")
		func()
		print("***********")
	return wrap_func

@my_decorator
def hello():
	print('hello')

@my_decorator
def bye():
	print('see ya later!')

hello()
bye()

# my_decorator(hello)()