from PIL import Image
im = Image.open("test.png")
width, height = im.size
empty = 0
white = 0
notwhite = 0
pix = im.load()
for i in range(0,height):
	for j in range(0,width):
		if pix[j, i] == (255, 255, 255, 255):
			white += 1
		else:
			notwhite += 1

	if white == width:
		empty += 1
	white = 0
read = float(input("Enter height of the vehicle in metres"))
print("Area in sq.m", notwhite * pow((read / 
	(height - empty)), 2))



