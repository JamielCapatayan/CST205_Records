from PIL import Image

def getMedian(nums):
    mid = len(nums)//2
    return nums[mid]

files = {1:"images/1.png",
         2:"images/2.png",
         3:"images/3.png",
         4:"images/4.png",
         5:"images/5.png",
         6:"images/6.png",
         7:"images/7.png",
         8:"images/8.png",
         9:"images/9.png",
         10:"images/10.png",
         11:"images/11.png"}

im1 = Image.open(files[1])
im2 = Image.open(files[2])
im3 = Image.open(files[3])
im4 = Image.open(files[4])
im5 = Image.open(files[5])
im6 = Image.open(files[6])
im7 = Image.open(files[7])
im8 = Image.open(files[8])
im9 = Image.open(files[9])
im10 = Image.open(files[10])
im11 = Image.open(files[11])

list1 = list(im1.getdata())
list2 = list(im2.getdata())
list3 = list(im3.getdata())
list4 = list(im4.getdata())
list5 = list(im5.getdata())
list6 = list(im6.getdata())
list7 = list(im7.getdata())
list8 = list(im8.getdata())
list9 = list(im9.getdata())
list10 = list(im10.getdata())
list11 = list(im11.getdata())

index = 0
imageList = []

while(index < len(list1)):
    temp = [list1[index], list2[index], list3[index], list4[index], list5[index], list6[index], list7[index], list8[index], list9[index], list10[index], list11[index]]
    temp = sorted(temp)
    pixel = getMedian(temp)
    imageList.append(pixel)
    index += 1

im1.putdata(imageList)
im1.save('images/new.png')
