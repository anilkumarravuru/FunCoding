from PIL import Image
def isDistinct(p1,p2):
	if (p1[0]-p2[0])**2 + (p1[1]-p2[1])**2 + (p1[2]-p2[2])**2 >= 7500:
		return True
	return False

im = Image.open('kia.jpg') # Can be many different formats.
pix = im.load()
(x,y) = im.size
for j in range(y):
	for i in range(x-1):
		if isDistinct(pix[i,j],pix[i+1,j]):
			
# print pix[x,y]  # Get the RGBA Value of the a pixel of an image
# pix[x,y] = value  # Set the RGBA Value of the image (tuple)
# im.save('alive_parrot.png')  # Save the modified pixels as .png