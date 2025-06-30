picture = [
	[0,0,0,1,0,0,0],
	[0,0,1,1,1,0,0],
	[0,1,1,1,1,1,0],
	[1,1,1,1,1,1,1],
	[0,0,0,1,0,0,0],
	[0,0,0,1,0,0,0]
]

for line in picture:
	for pixel in line:
		if (pixel):
			print("*", end = "")
		else:
			print(" ", end = "")
	print("")