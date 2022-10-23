
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel, QFileDialog
from PyQt5 import uic
from PyQt5.QtGui import QPixmap
import sys

class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init()
        
        #load the ui file
        uic.loadUi("imageViewer.ui",self)
        
        #define our widgets
        self.button=self.findChild(QPushButton,"pushButton")
        self.label=self.findChild(QLabel,"label")
        #click the dropdown box
        self.button.clicked.connect(self.clicker)
        #show the app
        self.show()
        
    def clicker(self):
        fname=QFileDialog.getOpenFileName(self,"Open File","Photos","All Files (*);;PNG Files(*.png);;Jpg Files (*.jpg)") 
        
        #open the image
        self.pixmap=QPixmap(fname[0])
        #add pic to label
        self.label.setPixmap(self.pixmap)
           
        
#initialize the app
app=QApplication(sys.argv)
UIWindow=UI()
app.exec_()
        