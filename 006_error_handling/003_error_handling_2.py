def sum(num1, num2):
	try:
		return num1/num2
	except (TypeError, ZeroDivisionError) as err:
		return err

print(sum(1, 0))