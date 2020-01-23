import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton, QComboBox, QHBoxLayout
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QColor

colors = {"Pick a color":"",
        "Squirtle Blue": [(162, 215, 213), "#A2D7D5"],
        "Charmander Red": [(244, 177, 133), "#F4B185"],
        "Bulbasaur Green": [(137, 200, 147), "#89C893"]}

class ColorWindow(QWidget):
    def __init__(self):
        super().__init__()

        master = MainWindow()

        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), QColor(colors["Squirtle Blue"][0][0], colors["Squirtle Blue"][0][1], colors["Squirtle Blue"][0][2]))
        self.setPalette(p)


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.label1 = QLabel("CST 205 Color Exchange!", self)
        self.my_combo_box = QComboBox()
        self.my_combo_box.addItems(colors)

        vbox = QVBoxLayout()
        vbox.addWidget(self.label1)
        vbox.addWidget(self.my_combo_box)

        self.rgb_label = QLabel("RGB: ", self)
        self.rgb_text = QLabel("", self)
        self.hex_label = QLabel("Hex: ", self)
        self.hex_text = QLabel("", self)
        hbox = QHBoxLayout()
        hbox.addWidget(self.rgb_label)
        hbox.addWidget(self.rgb_text)
        hbox.addWidget(self.hex_label)
        hbox.addWidget(self.hex_text)

        self.show_color = QPushButton('Show Color!')
        vbox.addWidget(self.show_color)

        mbox = QVBoxLayout()
        mbox.addLayout(vbox)
        mbox.addLayout(hbox)

        self.setLayout(mbox)
        self.my_combo_box.currentIndexChanged.connect(self.update_ui)
        self.show_color.clicked.connect(self.open_win)
        self.setWindowTitle("Colors!")

    @pyqtSlot()
    def update_ui(self):
        my_text = self.my_combo_box.currentText()
        my_index = self.my_combo_box.currentIndex()
        if(my_index == 1):
            rgb = colors["Squirtle Blue"][0]
            hex = colors["Squirtle Blue"][1]
        elif(my_index == 2):
            rgb = colors["Charmander Red"][0]
            hex = colors["Charmander Red"][1]
        elif(my_index == 3):
            rgb = colors["Bulbasaur Green"][0]
            hex = colors["Bulbasaur Green"][1]
        self.rgb_text.setText(str(rgb))
        self.hex_text.setText(hex)

    def open_win(self):
        self.new_win = ColorWindow()
        self.new_win.show()

app = QApplication(sys.argv)
main = MainWindow()
main.show()
sys.exit(app.exec_())
