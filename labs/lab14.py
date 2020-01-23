from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
from pprint import pprint
import numpy as np
import cv2

my_site = "https://knowyourmeme.com/photos/1466326-oh-youre-approaching-me-jojo-approach"


req = Request(
    my_site,
    headers={'User-Agent':'Moszilla/5.0'}
)

resp = urlopen(req)
bs_obj = BeautifulSoup(resp.read(), 'lxml')

link = bs_obj.find("a", {'class' : 'magnify'})

imgLink = link['href']

r = urlopen(imgLink)

image = np.asarray(bytearray(r.read()), dtype="uint8")
image = cv2.imdecode(image, cv2.IMREAD_COLOR)

im_remap = cv2.applyColorMap(image, cv2.COLORMAP_BONE)
status = cv2.imwrite('/Developer/jojo.jpg', im_remap)
print("Image written to file-system : ",status)
# cv2.imshow('JoJo', im_remap)
# cv2.waitKey()
