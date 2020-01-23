'''
Title: hw1_task1.py
Author: Jamiel Capatayan
Abstract: Take in data from a file and allocate the amount of numbers that fall within 4 ranges into appropriate bins
Date: 9/15/19
Course: CST205-01
'''
import pickle

def bin_allocation(image):
	# add logic gates and check items at 0, 1, 2 to see if they fit within these 4 ranges
	for items in image:
		for item in items:
			# red bin allocation
			if item[0] < 64:
				color_bin['red'][0] += 1
			elif item[0] >= 64 and item[0] < 128:
				color_bin['red'][1] += 1
			elif item[0] >= 128 and item[0] < 192:
				color_bin['red'][2] += 1
			elif item[0] >= 192 and item[0] < 255:
				color_bin['red'][3] += 1
			# green bin allocation
			if item[1] < 64:
				color_bin['green'][0] += 1
			elif item[1] >= 64 and item[1] < 128:
				color_bin['green'][1] += 1
			elif item[1] >= 128 and item[1] < 192:
				color_bin['green'][2] += 1
			elif item[1] >= 192 and item[1] < 255:
				color_bin['green'][3] += 1
			# blue bin allocation
			if item[2] < 64:
				color_bin['blue'][0] += 1
			elif item[2] >= 64 and item[2] < 128:
				color_bin['blue'][1] += 1
			elif item[2] >= 128 and item[2] < 192:
				color_bin['blue'][2] += 1
			elif item[2] >= 192 and item[2] < 255:
				color_bin['blue'][3] += 1

# use pickle module to open and read in data from a file
file = open('image_matrix', 'rb')

pixel = pickle.load(file)

file.close()

# --------------smaller case for testing-----------------
# print(pixel)

# pixel = [ 
#      [ (54, 54, 54), (232, 23, 93), (71, 71, 71), (168, 167, 167) ], 
#      [ (204, 82, 122), (54, 54, 54), (168, 167, 167), (232, 23, 93) ], 
#      [ (71, 71, 71), (168, 167, 167), (54, 54, 54), (204, 82, 122) ], 
#      [ (168, 167, 167), (204, 82, 122), (232, 23, 93), (54, 54, 54) ]
# ]
#--------------------------------------------------------

color_bin = {
	'red':[0, 0, 0, 0],
	'blue':[0, 0, 0, 0],
	'green':[0, 0, 0, 0]
}

bin_allocation(pixel)

print(pixel[0])