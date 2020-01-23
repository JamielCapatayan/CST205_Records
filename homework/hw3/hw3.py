import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton, QComboBox, QHBoxLayout, QLineEdit
from PyQt5.QtGui import QColor, QIcon, QPixmap
from PyQt5.QtCore import pyqtSlot
from PIL import Image

# Authors: Jamiel Capatayan & Eunji Choi
# Date: October 14, 2019
# Course: CST 205

filters = ["Pick a filter",
          "Sepia",
          "Negative",
          "Grayscale",
          "Thumbnail",
          "None"]

image_info = [
     {
           "id" : "images/34694102243_3370955cf9_z.jpg",
           "title" : "Eastern",
           "flickr_user" : "Sean Davis",
           "tags" : ["Los Angeles", "California", "building"],
      },
      {
           "id" : "images/37198655640_b64940bd52_z.jpg",
           "title" : "Spreetunnel",
           "flickr_user" : "Jens-Olaf Walter",
           "tags" : ["Berlin", "Germany", "tunnel", "ceiling"]
      },
      {
           "id" : "images/36909037971_884bd535b1_z.jpg",
           "title" : "East Side Gallery",
           "flickr_user" : "Pieter van der Velden",
           "tags" : ["Berlin", "wall", "mosaic", "sky", "clouds"]
      },
      {
           "id" : "images/36604481574_c9f5817172_z.jpg",
           "title" : "Lombardia, september 2017",
           "flickr_user" : "Mónica Pinheiro",
           "tags" : ["Italy", "Lombardia", "alley", "building", "wall"]
      },
      {
           "id" : "images/36885467710_124f3d1e5d_z.jpg",
           "title" : "Palazzo Madama",
           "flickr_user" : "Kevin Kimtis",
           "tags" : [ "Rome", "Italy", "window", "road", "building"]
      },
      {
           "id" : "images/37246779151_f26641d17f_z.jpg",
           "title" : "Rijksmuseum library",
           "flickr_user" : "John Keogh",
           "tags" : ["Amsterdam", "Netherlands", "book", "library", "museum"]
      },
      {
           "id" : "images/36523127054_763afc5ed0_z.jpg",
           "title" : "Canoeing in Amsterdam",
           "flickr_user" : "bdodane",
           "tags" : ["Amsterdam", "Netherlands", "canal", "boat"]
      },
      {
           "id" : "images/35889114281_85553fed76_z.jpg",
           "title" : "Quiet at dawn, Cabo San Lucas",
           "flickr_user" : "Erin Johnson",
           "tags" : ["Mexico", "Cabo", "beach", "cactus", "sunrise"]
      },
      {
           "id" : "images/34944112220_de5c2684e7_z.jpg",
           "title" : "View from our rental",
           "flickr_user" : "Doug Finney",
           "tags" : ["Mexico", "ocean", "beach", "palm"]
      },
      {
           "id" : "images/36140096743_df8ef41874_z.jpg",
           "title" : "Someday",
           "flickr_user" : "Thomas Hawk",
           "tags" : ["Los Angeles", "Hollywood", "California", "Volkswagen", "Beatle", "car"]
      }
]


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.label1 = QLabel("Image Search: ")
        self.line_edit = QLineEdit()
        hbox = QHBoxLayout()
        hbox.addWidget(self.label1)
        hbox.addWidget(self.line_edit)

        self.combo_box = QComboBox()
        self.combo_box.addItems(filters)
        self.submit = QPushButton('Submit')
        vbox = QVBoxLayout()
        vbox.addWidget(self.combo_box)
        vbox.addWidget(self.submit)

        mbox = QVBoxLayout()
        mbox.addLayout(hbox)
        mbox.addLayout(vbox)

        self.setLayout(mbox)
        self.submit.clicked.connect(self.set_image)
        self.setWindowTitle("Image Search")

    @pyqtSlot()
    def set_image(self):
        filter = self.combo_box.currentText()
        string = self.line_edit.text()

        string.lower()
        string_list = string.split(" ")

        ######################################## Image code block ########################################
        counters = [0,0,0,0,0,0,0,0,0,0]

        for word in string_list:
            for pos in range(len(image_info)):
                if (word in image_info[pos]['title'] or word in image_info[pos]['tags']):
                    counters[pos] += 1

        img_list = []

        for pos in range(len(counters)):
            if(counters[pos] == max(counters)):
                img_list.append( (image_info[pos]['title'], pos) )

        sorted(img_list)

        im = Image.open(image_info[img_list[0][1]]['id'])

        ########################################## filter code block #################################3
        if(filter == 'Sepia'):
            new_image = []
            for pixel in im.getdata():
                temp = (pixel[0], int(pixel[1] * 0.7), int(pixel[2] * 0.7))
                new_image.append(temp)
            im.putdata(new_image)
            im.show()
        elif(filter == 'Negative'):
            neg_list = [(255 - p[0], 255-p[1], 255-p[2]) for p in im.getdata()]
            im.putdata(neg_list)
            im.show()
        elif(filter == 'Grayscale'):
            new_image = [ ((a[0] + a[1] + a[2]) // 3,) * 3 for a in im.getdata()]
            im.putdata(new_image)
            im.show()
        elif(filter == 'Thumbnail'):
            size = (128, 128)
            im.thumbnail(size)
            im.show()
        elif(filter == 'None'):
            im.show()


app = QApplication(sys.argv)
win = MainWindow()
win.show()
sys.exit(app.exec_())
