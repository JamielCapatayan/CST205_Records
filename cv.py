import numpy as mp
import cv2

################################### imread() example ###################################
# img = cv2.imread('images/cat.jpg')
# #uint8
# print('image data type')
# print(img.dtype)
#
# #shape
# print('image shape')
# print(img.shape)
#
# print('image print')
# print(img)
#########################################################################################

################################### change img filter ###################################
#convert image to grayscale
# im_gray = cv2.imread('images/cat.jpg', cv2.IMREAD_GRAYSCALE)
#
# im_remap = cv2.applyColorMap(im_gray, cv2.COLORMAP_HOT)
#
# #use highgui
# cv2.imshow('cat in gray', im_remap)
#
# #keeps image displayed
# cv2.waitKey()
#########################################################################################


################################### video capture #######################################
#
# my_video = cv2.VideoCapture('images/jojo.mp4')
#
# frame_rate = my_video.get(cv2.CAP_PROP_FPS)
#
# wait_value = int(1000/frame_rate)
#
# while True:
#     ret, frame = my_video.read()
#
#     if ret:
#         # CIE XYZ color space Recommendation BT.709 with D65 white point
#         cie_xyz = cv2.cvtColor(frame, cv2.COLOR_BGR2XYZ)
#         # remap makes vido into a filtered color
#         remap = cv2.applyColorMap(cie_xyz, cv2.COLORMAP_HOT)
#         #showing cie_xyz shows the original video remap shows the filtered version
#         cv2.imshow('Jojo v Dio', remap)
#         cv2.waitKey(wait_value)
#     else:
#         break
#########################################################################################


################################### cv rectangles #######################################

img = cv2.imread('labs/jojo.jpg')

cv2.rectangle(
        img,
        (185, 254),
        (265, 334),
        (0, 255, 0),
        2
)

cv2.imshow("Rectangled", img)
cv2.waitKey()
