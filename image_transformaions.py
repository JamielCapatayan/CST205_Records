# copy an image
import math
import numpy as np
from PIL import Image


pic1 = Image.open("images/husky.png")
pic2 = Image.open("images/sunset.jpg")


# def copy_husky():
# 	#source image
# 	husky = Image.open("images/husky.png")

# 	#destination image
# 	canvas = Image.new("RGB", (640,480), "white")

# 	target_x = 0

# 	for source_x in range(husky.width):
# 		target_y = 0

# 		for source_y in range(husky.height):
# 			color = husky.getpixel((source_x, source_y)) # get pixels from the source
# 			canvas.putpixel((target_x, target_y), color) # puts pixels onto target
# 			target_y += 1
# 		target_x += 1

# 	canvas.save("images/copy_husky.png")

# copy_husky()

# ==========================Scaling up a pic=====================================

# target = Image.new('RGB', (source.width*2, source.height*2))#scales up  by 2

# target_x = 0

# for source_x in np.repeat(range(source.width), 2):
# 	target_y = 0
# 	for source_y in np.repeat(range(source.height), 2):
# 		 color = source.getpixel((int(source_x), int(source_y)))
# 		 target.putpixel((target_x, target_y), color)
# 		 target_y += 1
# 	target_x += 1

# target.show()

#================================Chroma Key++++++++++++++++++++++++++++++++++++++++

def distance(color_1, color_2):
	red_diff = math.pow((color_1[0] - color_2[0]), 2)
	green_diff = math.pow((color_1[1] - color_2[1]), 2)
	blue_diff = math.pow((color_1[2] - color_2[2]), 2)
	return math.sqrt(red_diff + green_diff + blue_diff) 


def chromakey(source, bg):
	for x in range(source.width):
		for y in range(source.height):

			cur_pixel = source.getpixel((x,y))
			green = (0, 190, 60)

			if distance(cur_pixel, green) < 250:
				# grab the color at the same spot from the new background
				source.putpixel((x,y), bg.getpixel((x,y))) 

	source.save("images/chromakeyed.png")

chromakey(pic1, pic2) 