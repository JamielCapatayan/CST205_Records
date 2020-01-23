'''
Title: hw1_task1.py
Author: Jamiel Capatayan
Abstract: Take in data from file and use data to create a histogram to see the amount of certain values in the data.
Date: 9/15/19
Course: CST205-01
'''
import hist_machine as hp
import pickle

def task2(image):
	# append numbers into their respective colors
	for items in image:
		for num in items:
			color_bins['red'].append(num[0])

			color_bins['green'].append(num[1])

			color_bins['blue'].append(num[2])
			
	# sort the numbers
	color_bins['red'] = sorted(color_bins['red'])
	color_bins['green'] = sorted(color_bins['green'])
	color_bins['blue'] = sorted(color_bins['blue'])
	
	# store in a list
	color_vals = [color_bins['red'], color_bins['green'], color_bins['blue']]

	return color_vals

# -------------------small case for testing------------------
# pixel = [ 
#      [ (54, 54, 54), (232, 23, 93), (71, 71, 71), (168, 167, 167) ], 
#      [ (204, 82, 122), (54, 54, 54), (168, 167, 167), (232, 23, 93) ], 
#      [ (71, 71, 71), (168, 167, 167), (54, 54, 54), (204, 82, 122) ], 
#      [ (168, 167, 167), (204, 82, 122), (232, 23, 93), (54, 54, 54) ]
# ]
#-------------------------------------------------------------

# use pickle to read in and store file data
file = open('image_matrix', 'rb')

pixel = pickle.load(file)

file.close()

color_bins = {
	'red' : [],
	'blue' : [],
	'green' : []
}

# call hist_machine module to create SVG files in same directory
hp.hist_plotter(task2(pixel))
