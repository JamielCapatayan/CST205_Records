def find_first(val):
  val /= 16
  val = int(val)

  if(val < 16 and val > 9):
  	val += 55
  	return(chr(val))

  return(str(val))


def find_second(val):
  val %= 16

  if(val < 16 and val > 9):
    val += 55
    return(chr(val))

  return(str(val))



color_code = input("")
color_list = color_code.split(',')

for i in range(0, len(color_list)):
	color_list[i] = int(color_list[i])

new_code = (color_list[0], color_list[1], color_list[2])

hex_code = "#"

for char in new_code:
  first = find_first(char)
  second = find_second(char)
  
  hex_code += first
  hex_code += second

print(hex_code)











































# def get_value(val1, val2):
# 	definitions = {'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15}

# 	if(val1.isalpha()):
# 		for key, value in definitions.items():
# 			if val1 == key:
# 				val1 = int(value)
# 	elif(val1.isdigit()):
# 		val1 = int(val1)
		

# 	if(val2.isalpha()):
# 		for key, value in definitions.items():
# 			if val2 == key:
# 				val2 = int(value)
# 	elif(val2.isdigit()):
# 		val2 = int(val2)

# 	val1 *= 16
# 	val2 *= 1

# 	return val1 + val2


# color_code = input()

# new_code = color_code.replace("#", "")

# count = 0
# red_vals = []
# green_vals = []
# blue_vals = []

# for char in new_code:
# 	count += 1
# 	if(count <= 2):
# 		red_vals.append(char)
# 	elif(count > 2 and count <= 4):
# 		green_vals.append(char)
# 	else:
# 		blue_vals.append(char)


# red_val = get_value(red_vals[0], red_vals[1])
# green_val = get_value(green_vals[0], green_vals[1])
# blue_val = get_value(blue_vals[0], blue_vals[1])


# code = (red_val, green_val, blue_val)
# print(code)







#color_list = color_code.split(',')

# for i in range(0, len(color_list)):
# 	color_list[i] = int(color_list[i])

# hue = (color_list[0], color_list[1], color_list[2])


# if hue[0] > 200 or hue[0] > 100:
# 	print('The color is reddish\n')
# 	if hue[1] > 100:
# 		print('The color is a shade of yellow')
# 	elif hue[2] > 100:
# 		print('The color is a shade of magenta')
# elif hue[1] > 200 or hue[1] > 100:
# 	print('The color is greenish\n')
# 	if hue[0] > 100:
# 		print('The color is a shade of yellow')
# 	elif hue[2] > 100:
# 		print('The color is a shade of cyan')
# elif hue[2] > 200 or hue[2] > 100:
# 	print('The color is bluish\n')
# 	if hue[0] > 100:
# 		print('The color is a shade of magenta')
# 	elif hue[1] > 100:
# 		print('The color is a shade of cyan')