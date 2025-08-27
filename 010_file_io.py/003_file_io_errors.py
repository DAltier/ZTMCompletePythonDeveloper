try:
	with open(r"c:\Users\cnx36\Documents\7.Projects\1.ZeroToMastery\CompletePythonDeveloper\010_file_io.py\test.txt", mode = 'r') as my_file:
		print(my_file.read())
except FileNotFoundError as err:
	print('File does not exist')
	raise err
except IOError as err:
	print('IO error')
	raise err
