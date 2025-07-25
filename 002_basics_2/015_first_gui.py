picture = [
	[0,0,0,1,0,0,0],
	[0,0,1,1,1,0,0],
	[0,1,1,1,1,1,0],
	[1,1,1,1,1,1,1],
	[0,0,0,1,0,0,0],
	[0,0,0,1,0,0,0]
]

fill = '*'
empty = ' '
for row in picture:
	for pixel in row:
		if pixel:
			print(fill, end = "") # end defaults to new line, overwriting that default
		else:
			print(empty, end = "")
	print("") # need a new line after each row