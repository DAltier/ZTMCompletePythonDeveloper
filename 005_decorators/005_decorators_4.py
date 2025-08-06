from time import time
def performance(func):
	def wrapper(*args, **kwargs):
		t1 = time()
		result = func(*args, **kwargs)
		t2 = time()
		print(f"it took {t2 - t1}ms")
		return result
	return wrapper

@performance
def long_time():
	for i in range(100000000):
		i * 5

long_time()