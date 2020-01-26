from PIL import Image
# im = Image.open('images/cat.jpg')

# def decrease_red(picture):
#  new_list = []

#  for p in picture.getdata():
#  	temp = (int(p[0]*2), int(p[1]*1), int(p[2]*1))
#  	new_list.append(temp)

#  picture.putdata(new_list)
#  picture.save('images/new_pic.jpg')

# decrease_red(im)

#================================================================================

# mapping method is an alternate to looping through a pixel and creating a new temp value

# im = Image.open('images/roses.jpg')

# def map_red(pixel):
#  return (int(pixel[0]*.5), pixel[1], pixel[2])

# # map red is a function but is not being called here, map is telling map_red to run with im.getdata parameters
# new_list = map(map_red, im.getdata())

# im.putdata(list(new_list))

# im.save('images/new.jpg')

# =================================================================================

# implementation of a lambda funciton

im = Image.open('images/cat.jpg')

# lambda a: (insert function definition), creates lambda function a with its wn definitions/actions
new_list = map(lambda a: (a[0], int(a[1]/1.3), int(a[2]/1.3)), im.getdata())

im.putdata(list(new_list))

im.save('images/new_pic.jpg')


#====================================================================================

#negative images

# im = Image.open('images/cat.jpg')

# # fancy way of subtracting 255 from each pixel in the image
# def negative_image(pixel):
# 	#for each number in the pixel, subtract 255 and return to a tuple
# 	return tuple(map(lambda a: (255 - a)*2, pixel)) #multiply by two to make double negative

# negative_list = map(negative_image, im.getdata())

# '''
# or with list comprehension,
# neg_list = [(255 - p[0], 255-p[1], 255-p[2]) for p in im.getdata()]
# '''
# im.putdata(list(negative_list))
# im.save('images/new_negative.jpg')

#====================================================================================

# greyscale

# im = Image.open('images/hellothere.jpg')

# # lambda function =  int( (a[0] + a[1] + a[2] / 3) )
# #//---average
# # new_list = map(lambda a: ( int((a[0] + a[1] + a[2]) / 3), ) *3, im.getdata())

# #//---channels
# # new_list = map( lambda a : (a[1], ) * 3, im.getdata())

# #//---Better grayscale
# def lum_image(p):
# 	new_red = int(p[0] * 0.299)
# 	new_green = int(p[1] * 0.587)
# 	new_blue = int(p[2] * 0.114)
# 	luminance = new_red + new_green + new_blue
# 	return (luminance,) * 3

# new_list = map(lum_image, im.getdata())

# '''
# or,
# new_list = [ ((a[0] + a[1] + a[2]) // 3,) * 3 for a in im.getdata()]
# '''

# im.putdata(list(new_list))
# im.save('images/new_gray.jpg')

#====================================================================================

# color distance
