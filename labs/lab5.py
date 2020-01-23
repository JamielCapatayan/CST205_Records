from PIL import Image

with open('mona.txt', 'r') as f:
	line_list = f.readlines()

pic_list = []

for line in line_list:
	pic_list.append(line)

i = []

for line in pic_list:
	i.append(line.split(','))

temp1 = []

for element in i:
	#print(element)
	for nums in element:
		temp1.append(nums.split())

mona_data = []

for vals in temp1:
	#print(vals)
	temp2 = []
	for val in vals:
		if(';' in val):
			val = val.replace(';', '')
		if(val.isdigit()):
			temp2.append(int(val))
	mona_data.append(temp2)

nums = []
for data in mona_data:
	# print(data)
	for num in data:
		nums.append(num)


mona = Image.frombytes('L', (18,29), bytes(nums))

mona.show()


#print(temp)


#print(pic_list)

#print(line_list)