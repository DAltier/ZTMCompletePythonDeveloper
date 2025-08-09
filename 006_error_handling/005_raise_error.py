while True:
	try:
		age = int(input('what is your age? '))
		10/age
		raise ValueError('hey cut it out!') # or raise Exception
	except ZeroDivisionError:
		print('please enter age higher than 0')
	else:
		print('thank you!')
		break
	finally:
		print('ok, I am finally done')