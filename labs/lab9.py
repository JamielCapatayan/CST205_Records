import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QColor

class Window(QWidget):
	def __init__(self):
		super().__init__()
		self.label1 = QLabel('Jamiel Capatayan', self)

		self.setAutoFillBackground(True)
		p = self.palette()
		p.setColor(self.backgroundRole(), QColor(220, 100, 220))
		self.setPalette(p)

		vbox = QVBoxLayout()

		self.my_btn = QPushButton("Button 1", self)
		self.my_lbl = QLabel('Button not clicked')
		self.my_btn.clicked.connect(self.on_click)

		vbox.addWidget(self.label1)
		vbox.addWidget(self.my_btn)
		vbox.addWidget(self.my_lbl)
		self.setGeometry(100,100,600,400)
		self.setLayout(vbox)

	@pyqtSlot()
	def on_click(self):
		self.my_lbl.setText('Button clicked')




app = QApplication(sys.argv)
main_win = Window()
main_win.show()
sys.exit(app.exec_())
