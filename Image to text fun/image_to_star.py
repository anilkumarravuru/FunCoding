#anilkumarravuru
import math
from PIL import Image
image = Image.open("cap2.png")
px = image.load()
dim = image.size
# print dim
# dim[0] X dim[1]
# Scale the image to 240 X 80
# print px[1,1]
sideScale = int(math.ceil(dim[0]/240))
downScale = int(math.ceil(dim[1]/80))
scale = max(sideScale, downScale)
# print sideScale, downScale, scale
if scale<=1:
	scale = 2
for x in range(0,dim[1],scale-1):
	string = ''
	for y in range(0,dim[0],int(math.ceil(scale*2.0/3))-2):
		if px[y,x][:3] > (200,200,200):
			string += ' '
		else:
			string += '*'
	print string