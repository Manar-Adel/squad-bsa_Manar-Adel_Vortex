# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calculator.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(361, 588)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.output_label = QtWidgets.QLabel(self.centralwidget)
        self.output_label.setGeometry(QtCore.QRect(10, 10, 341, 91))
        font = QtGui.QFont()
        font.setFamily("American Typewriter")
        font.setPointSize(36)
        self.output_label.setFont(font)
        self.output_label.setFrameShape(QtWidgets.QFrame.Box)
        self.output_label.setFrameShadow(QtWidgets.QFrame.Raised)
        self.output_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.output_label.setObjectName("output_label")
        self.percentButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_it("%"))
        self.percentButton.setGeometry(QtCore.QRect(10, 110, 75, 75))
        font = QtGui.QFont()
        font.setFamily("American Typewriter")
        font.setPointSize(26)
        self.percentButton.setFont(font)
        self.percentButton.setObjectName("percentButton")
        self.cButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_it("c"))
        self.cButton.setGeometry(QtCore.QRect(100, 110, 75, 75))
        font = QtGui.QFont()
        font.setFamily("American Typewriter")
        font.setPointSize(26)
        self.cButton.setFont(font)
        self.cButton.setObjectName("cButton")
        self.divideButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_it("/"))
        self.divideButton.setGeometry(QtCore.QRect(275, 110, 75, 75))
        font = QtGui.QFont()
        font.setFamily("American Typewriter")
        font.setPointSize(26)
        self.divideButton.setFont(font)
        self.divideButton.setObjectName("divideButton")
        self.arrowButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.remove_it())
        self.arrowButton.setGeometry(QtCore.QRect(190, 110, 75, 75))
        font = QtGui.QFont()
        font.setFamily("American Typewriter")
        font.setPointSize(26)
        self.arrowButton.setFont(font)
        self.arrowButton.setObjectName("arrowButton")
        self.sevenButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_it("7"))
        self.sevenButton.setGeometry(QtCore.QRect(10, 190, 75, 75))
        font = QtGui.QFont()
        font.setFamily("American Typewriter")
        font.setPointSize(26)
        self.sevenButton.setFont(font)
        self.sevenButton.setObjectName("sevenButton")
        self.nineButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_it("9"))
        self.nineButton.setGeometry(QtCore.QRect(190, 190, 75, 75))
        font = QtGui.QFont()
        font.setFamily("American Typewriter")
        font.setPointSize(26)
        self.nineButton.setFont(font)
        self.nineButton.setObjectName("nineButton")
        self.multiplyButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_it("*"))
        self.multiplyButton.setGeometry(QtCore.QRect(275, 190, 75, 75))
        font = QtGui.QFont()
        font.setFamily("American Typewriter")
        font.setPointSize(26)
        self.multiplyButton.setFont(font)
        self.multiplyButton.setObjectName("multiplyButton")
        self.eightButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_it("8"))
        self.eightButton.setGeometry(QtCore.QRect(100, 190, 75, 75))
        font = QtGui.QFont()
        font.setFamily("American Typewriter")
        font.setPointSize(26)
        self.eightButton.setFont(font)
        self.eightButton.setObjectName("eightButton")
        self.fourButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_it("4"))
        self.fourButton.setGeometry(QtCore.QRect(10, 270, 75, 75))
        font = QtGui.QFont()
        font.setFamily("American Typewriter")
        font.setPointSize(26)
        self.fourButton.setFont(font)
        self.fourButton.setObjectName("fourButton")
        self.sixButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_it("6"))
        self.sixButton.setGeometry(QtCore.QRect(190, 270, 75, 75))
        font = QtGui.QFont()
        font.setFamily("American Typewriter")
        font.setPointSize(26)
        self.sixButton.setFont(font)
        self.sixButton.setObjectName("sixButton")
        self.minusButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_it("-"))
        self.minusButton.setGeometry(QtCore.QRect(275, 270, 75, 75))
        font = QtGui.QFont()
        font.setFamily("American Typewriter")
        font.setPointSize(26)
        self.minusButton.setFont(font)
        self.minusButton.setObjectName("minusButton")
        self.fiveButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_it("5"))
        self.fiveButton.setGeometry(QtCore.QRect(100, 270, 75, 75))
        font = QtGui.QFont()
        font.setFamily("American Typewriter")
        font.setPointSize(26)
        self.fiveButton.setFont(font)
        self.fiveButton.setObjectName("fiveButton")
        self.oneButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_it("1"))
        self.oneButton.setGeometry(QtCore.QRect(10, 350, 75, 75))
        font = QtGui.QFont()
        font.setFamily("American Typewriter")
        font.setPointSize(26)
        self.oneButton.setFont(font)
        self.oneButton.setObjectName("oneButton")
        self.threeButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_it("3"))
        self.threeButton.setGeometry(QtCore.QRect(190, 350, 75, 75))
        font = QtGui.QFont()
        font.setFamily("American Typewriter")
        font.setPointSize(26)
        self.threeButton.setFont(font)
        self.threeButton.setObjectName("threeButton")
        self.plusButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_it("+"))
        self.plusButton.setGeometry(QtCore.QRect(275, 350, 75, 75))
        font = QtGui.QFont()
        font.setFamily("American Typewriter")
        font.setPointSize(26)
        self.plusButton.setFont(font)
        self.plusButton.setObjectName("plusButton")
        self.twoButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_it("2"))
        self.twoButton.setGeometry(QtCore.QRect(100, 350, 75, 75))
        font = QtGui.QFont()
        font.setFamily("American Typewriter")
        font.setPointSize(26)
        self.twoButton.setFont(font)
        self.twoButton.setObjectName("twoButton")
        self.plusMinusButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.plus_minus_it())
        self.plusMinusButton.setGeometry(QtCore.QRect(10, 430, 75, 75))
        font = QtGui.QFont()
        font.setFamily("American Typewriter")
        font.setPointSize(26)
        self.plusMinusButton.setFont(font)
        self.plusMinusButton.setObjectName("plusMinusButton")
        self.dotButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.dot_it())
        self.dotButton.setGeometry(QtCore.QRect(190, 430, 75, 75))
        font = QtGui.QFont()
        font.setFamily("American Typewriter")
        font.setPointSize(26)
        self.dotButton.setFont(font)
        self.dotButton.setObjectName("dotButton")
        self.equalButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.math_it())
        self.equalButton.setGeometry(QtCore.QRect(275, 430, 75, 75))
        font = QtGui.QFont()
        font.setFamily("American Typewriter")
        font.setPointSize(26)
        self.equalButton.setFont(font)
        self.equalButton.setObjectName("equalButton")
        self.zeroButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_it("0"))
        self.zeroButton.setGeometry(QtCore.QRect(100, 430, 75, 75))
        font = QtGui.QFont()
        font.setFamily("American Typewriter")
        font.setPointSize(26)
        self.zeroButton.setFont(font)
        self.zeroButton.setObjectName("zeroButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 361, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)



    #lets do some math
    def math_it(self):
        #grab wahst on the screen already
        screen= self.output_label.text()
        try:
            #do the math
            answer=eval(screen)
            #output answer
            self.output_label.setText(str(answer))
        except: 
            #output error on screen
            self.output_label.setText("Error")   

    #remove a character
    def remove_it(self):
        #grab wahst on the screen already
        screen= self.output_label.text()
        #remove last item
        screen=screen[:-1]
        #output back to screen
        self.output_label.setText(screen)
        

    #add a decimal
    def dot_it(self):
        screen= self.output_label.text()
        if screen[-1]=="." in screen:
            pass
        else:
            self.output_label.setText(f'{screen}.')
            
    #change to positive/negative
    def plus_minus_it(self):
        #grab wahst on the screen already
        screen= self.output_label.text()
        
        if "-" in screen:
            self.output_label.setText(screen.replace("-",""))
        else:
            self.output_label.setText(f'-{screen}')
                
        
        
                 


    #for pressing the button
    def press_it(self, pressed):
        if pressed=="c":
            self.output_label.setText("0")
        else:
            #ceck to see if starts with zero and deletes it
            if self.output_label.text()=="0":
               self.output_label.setText("") 
            #otherwise add the numbers next to each other   
            self.output_label.setText(f'{self.output_label.text()}{pressed}')


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Calculator"))
        self.output_label.setText(_translate("MainWindow", "0"))
        self.percentButton.setText(_translate("MainWindow", "%"))
        self.cButton.setText(_translate("MainWindow", "C"))
        self.divideButton.setText(_translate("MainWindow", "/"))
        self.arrowButton.setText(_translate("MainWindow", "<<"))
        self.sevenButton.setText(_translate("MainWindow", "7"))
        self.nineButton.setText(_translate("MainWindow", "9"))
        self.multiplyButton.setText(_translate("MainWindow", "x"))
        self.eightButton.setText(_translate("MainWindow", "8"))
        self.fourButton.setText(_translate("MainWindow", "4"))
        self.sixButton.setText(_translate("MainWindow", "6"))
        self.minusButton.setText(_translate("MainWindow", "-"))
        self.fiveButton.setText(_translate("MainWindow", "5"))
        self.oneButton.setText(_translate("MainWindow", "1"))
        self.threeButton.setText(_translate("MainWindow", "3"))
        self.plusButton.setText(_translate("MainWindow", "+"))
        self.twoButton.setText(_translate("MainWindow", "2"))
        self.plusMinusButton.setText(_translate("MainWindow", "+/-"))
        self.dotButton.setText(_translate("MainWindow", "."))
        self.equalButton.setText(_translate("MainWindow", "="))
        self.zeroButton.setText(_translate("MainWindow", "0"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())