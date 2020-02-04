# import sys
# from PyQt5.QtWidgets import QApplication, QWidget, QLabel

# my_qt_app = QApplication(sys.argv)

# my_window = QWidget()

# my_window.setGeometry(0,0,400,300)

# my_window.setWindowTitle('CST 205!')

# my_label = QLabel(my_window)

# my_label.setText('Hi!')

# my_window.show()
# sys.exit(my_qt_app.exec_())


#=================================make a main window application=====================================
# import sys
# from PyQt5.QtWidgets import QApplication, QMainWindow

# app = QApplication(sys.argv)

# class MainWindow(QMainWindow):
# 	def __init__(self):
# 		super().__init__()
# 		self.setWindowTitle('CST 205 Main Window')
# 		self.show()


# mainWin = MainWindow()
# mainWin.show()
# status = app.exec_()
# sys.exit(status)

#===============================make a label========================================================
# import sys
# from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
# class Example(QWidget):
# 	def __init__(self):
# 		super().__init__()
# 		self.label1 = QLabel('Label 1', self)
# 		self.label2 = QLabel('Label 2', self)

# 		vbox = QVBoxLayout()
# 		vbox.addWidget(self.label1)
# 		vbox.addWidget(self.label2)

# 		self.setLayout(vbox)
# 		self.setGeometry(100,100,600,400)
# 		self.show()

# app = QApplication(sys.argv)
# ex = Example()
# sys.exit(app.exec_())

#==============================make a button with qt=================================================

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel
from PyQt5.QtCore import pyqtSlot

class MainWindow(QWidget):
	def __init__(self):
		super().__init__()

		vbox = QVBoxLayout()

		self.my_btn = QPushButton("Button 1", self)
		self.my_lbl = QLabel('Button not clicked')
		self.my_btn.clicked.connect(self.on_click)

		vbox.addWidget(self.my_btn)
		vbox.addWidget(self.my_lbl)
		self.setLayout(vbox)

	@pyqtSlot()
	def on_click(self):
		self.my_lbl.setText('Button clicked')

app = QApplication(sys.argv)
main_win = MainWindow()
main_win.show()
sys.exit(app.exec_())
