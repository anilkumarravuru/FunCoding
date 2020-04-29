#anilkumarravuru   input: output of image_to_star
off = '.'
on = '*'
fp = open("input.txt")
Array = []
for line in fp:
	l = map(str, line.split())
	Array += [l]
width, height = len(Array[0]), len(Array)
ShapeArray = [['' for i in range(width-1)] for j in range(height-1)]
for i in range(height-2):
	for j in range(width-2):
		if Array[i][j]==off and Array[i][j+1]==off and Array[i+1][j]==off and Array[i+1][j+1]==off:
			ShapeArray[i][j] = " "
		elif Array[i][j]==off and Array[i][j+1]==off and Array[i+1][j]==off and Array[i+1][j+1]==on:
			ShapeArray[i][j] = " "
		elif Array[i][j]==off and Array[i][j+1]==off and Array[i+1][j]==on and Array[i+1][j+1]==on:
			ShapeArray[i][j] = "_"
		elif Array[i][j]==off and Array[i][j+1]==off and Array[i+1][j]==on and Array[i+1][j+1]==off:
			ShapeArray[i][j] = " "
		elif Array[i][j]==off and Array[i][j+1]==on and Array[i+1][j]==off and Array[i+1][j+1]==off:
			ShapeArray[i][j] = " "
		elif Array[i][j]==off and Array[i][j+1]==on and Array[i+1][j]==off and Array[i+1][j+1]==on:
			ShapeArray[i][j] = "|"
		elif Array[i][j]==off and Array[i][j+1]==on and Array[i+1][j]==on and Array[i+1][j+1]==on:
			ShapeArray[i][j] = "/"
		elif Array[i][j]==off and Array[i][j+1]==on and Array[i+1][j]==on and Array[i+1][j+1]==off:
			ShapeArray[i][j] = "/"
		elif Array[i][j]==on and Array[i][j+1]==off and Array[i+1][j]==off and Array[i+1][j+1]==off:
			ShapeArray[i][j] = off
		elif Array[i][j]==on and Array[i][j+1]==off and Array[i+1][j]==off and Array[i+1][j+1]==on:
			ShapeArray[i][j] = "\\"
		elif Array[i][j]==on and Array[i][j+1]==off and Array[i+1][j]==on and Array[i+1][j+1]==on:
			ShapeArray[i][j] = "|"
		elif Array[i][j]==on and Array[i][j+1]==off and Array[i+1][j]==on and Array[i+1][j+1]==off:
			ShapeArray[i][j] = "|"
		elif Array[i][j]==on and Array[i][j+1]==on and Array[i+1][j]==off and Array[i+1][j+1]==off:
			ShapeArray[i][j] = "_"
		elif Array[i][j]==on and Array[i][j+1]==on and Array[i+1][j]==off and Array[i+1][j+1]==on:
			ShapeArray[i][j] = "\\"
		elif Array[i][j]==on and Array[i][j+1]==on and Array[i+1][j]==on and Array[i+1][j+1]==on:
			ShapeArray[i][j] = on
		elif Array[i][j]==on and Array[i][j+1]==on and Array[i+1][j]==on and Array[i+1][j+1]==off:
			ShapeArray[i][j] = "/"
for i in range(width-2):
	for j in range(height-2):
		print ShapeArray[i][j],
	print ""
