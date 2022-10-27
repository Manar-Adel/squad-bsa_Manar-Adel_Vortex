#task 3 GUI


#IMPORTS
from PyQt5 import QtCore, QtGui, QtWidgets
import tkinter
from turtle import reset
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import *
from PyQt5.QtCore import *
import cv2
import numpy as np
import os
import sys
import time
from tkinter import *
import threading
import sys
import time
from multiprocessing.connection import Listener as l
import cv2 as cv
import numpy as np
import base64
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys

#TIMER VARIABLES
global count
count =0

#MAIN CLASS
class Ui_MainWindow(object):
    
    #Habiba Ahmed and Manar Adel --------------------------
    def __init__(self):
        self.Worker1 = Worker1()
        self.Worker1.start(0)
        self.Worker1.ImageUpdate.connect(self.ImageUpdateSlot)
    
    
    #Zeina Mohamed ----------------------------
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 609)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.bgImgLabel = QtWidgets.QLabel(self.centralwidget)
        self.bgImgLabel.setGeometry(QtCore.QRect(0, -10, 810, 570))
        self.bgImgLabel.setText("")
        self.bgImgLabel.setPixmap(QtGui.QPixmap("icons/a.jpg"))
        self.bgImgLabel.setScaledContents(True)
        self.bgImgLabel.setObjectName("bgImgLabel")
        self.guiLabel = QtWidgets.QLabel(self.centralwidget)
        self.guiLabel.setGeometry(QtCore.QRect(330, 0, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.guiLabel.setFont(font)
        self.guiLabel.setText("Vortex GUI")
        self.guiLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.guiLabel.setObjectName("guiLabel")
        self.camera2Label = QtWidgets.QLabel(self.centralwidget)
        self.camera2Label.setGeometry(QtCore.QRect(440, 40, 301, 251))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.camera2Label.setFont(font)
        self.camera2Label.setText("Camera 2")
        self.camera2Label.setAlignment(QtCore.Qt.AlignCenter)
        self.camera2Label.setObjectName("camera2Label")
        self.camera1Label = QtWidgets.QLabel(self.centralwidget)
        self.camera1Label.setGeometry(QtCore.QRect(50, 30, 321, 251))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.camera1Label.setFont(font)
        self.camera1Label.setText("Camera 1")
        self.camera1Label.setAlignment(QtCore.Qt.AlignCenter)
        self.camera1Label.setObjectName("camera1Label")
        self.grapperUpLabel = QtWidgets.QLabel(self.centralwidget)
        self.grapperUpLabel.setGeometry(QtCore.QRect(70, 319, 60, 91))
        self.grapperUpLabel.setAccessibleDescription("")
        self.grapperUpLabel.setAutoFillBackground(False)
        self.grapperUpLabel.setText("")
        self.grapperUpLabel.setPixmap(QtGui.QPixmap("icons/grapper-close.png"))
        self.grapperUpLabel.setScaledContents(True)
        self.grapperUpLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.grapperUpLabel.setWordWrap(False)
        self.grapperUpLabel.setIndent(-1)
        self.grapperUpLabel.setOpenExternalLinks(False)
        self.grapperUpLabel.setObjectName("grapperUpLabel")
        self.upLabel = QtWidgets.QLabel(self.centralwidget)
        self.upLabel.setGeometry(QtCore.QRect(80, 410, 40, 40))
        self.upLabel.setText("")
        self.upLabel.setPixmap(QtGui.QPixmap("icons/frwrd-arrowred.png"))
        self.upLabel.setScaledContents(True)
        self.upLabel.setObjectName("upLabel")
        self.ccwUpLabel = QtWidgets.QLabel(self.centralwidget)
        self.ccwUpLabel.setGeometry(QtCore.QRect(160, 430, 80, 40))
        self.ccwUpLabel.setText("")
        self.ccwUpLabel.setPixmap(QtGui.QPixmap("icons/cwred.png"))
        self.ccwUpLabel.setScaledContents(True)
        self.ccwUpLabel.setObjectName("ccwUpLabel")
        self.ccwDownLabel = QtWidgets.QLabel(self.centralwidget)
        self.ccwDownLabel.setGeometry(QtCore.QRect(160, 470, 80, 40))
        self.ccwDownLabel.setText("")
        self.ccwDownLabel.setPixmap(QtGui.QPixmap("icons/ccwred.png"))
        self.ccwDownLabel.setScaledContents(True)
        self.ccwDownLabel.setObjectName("ccwDownLabel")
        self.grapperRightLabel = QtWidgets.QLabel(self.centralwidget)
        self.grapperRightLabel.setGeometry(QtCore.QRect(160, 329, 80, 61))
        self.grapperRightLabel.setText("")
        self.grapperRightLabel.setPixmap(QtGui.QPixmap("icons/grapper-close-horizontalpng.png"))
        self.grapperRightLabel.setScaledContents(True)
        self.grapperRightLabel.setObjectName("grapperRightLabel")
        self.downArrowLabel = QtWidgets.QLabel(self.centralwidget)
        self.downArrowLabel.setGeometry(QtCore.QRect(280, 460, 41, 50))
        self.downArrowLabel.setText("")
        self.downArrowLabel.setPixmap(QtGui.QPixmap("icons/downward-arrowred.png"))
        self.downArrowLabel.setScaledContents(True)
        self.downArrowLabel.setObjectName("downArrowLabel")
        self.upArrowLabel = QtWidgets.QLabel(self.centralwidget)
        self.upArrowLabel.setGeometry(QtCore.QRect(280, 410, 41, 50))
        self.upArrowLabel.setText("")
        self.upArrowLabel.setPixmap(QtGui.QPixmap("icons/upward-arrowred.png"))
        self.upArrowLabel.setScaledContents(True)
        self.upArrowLabel.setObjectName("upArrowLabel")
        self.downownLabel = QtWidgets.QLabel(self.centralwidget)
        self.downownLabel.setGeometry(QtCore.QRect(80, 470, 40, 40))
        self.downownLabel.setText("")
        self.downownLabel.setPixmap(QtGui.QPixmap("icons/bckwrd-arrowred.png"))
        self.downownLabel.setScaledContents(True)
        self.downownLabel.setObjectName("downownLabel")
        self.rightLabel = QtWidgets.QLabel(self.centralwidget)
        self.rightLabel.setGeometry(QtCore.QRect(110, 440, 40, 40))
        self.rightLabel.setText("")
        self.rightLabel.setPixmap(QtGui.QPixmap("icons/right-arrowred.png"))
        self.rightLabel.setScaledContents(True)
        self.rightLabel.setObjectName("rightLabel")
        self.leftLabel = QtWidgets.QLabel(self.centralwidget)
        self.leftLabel.setGeometry(QtCore.QRect(50, 440, 40, 40))
        self.leftLabel.setText("")
        self.leftLabel.setPixmap(QtGui.QPixmap("icons/left-arrowred.png"))
        self.leftLabel.setScaledContents(True)
        self.leftLabel.setObjectName("leftLabel")
        
        #timer label
        self.resetBtn = QtWidgets.QPushButton(self.centralwidget,clicked= lambda: self.reset())
        self.resetBtn.setGeometry(QtCore.QRect(530, 320, 75, 23))
        self.resetBtn.setObjectName("resetBtn")
        
        self.currentSpeedTxt = QtWidgets.QLabel(self.centralwidget)
        self.currentSpeedTxt.setGeometry(QtCore.QRect(250, 330, 101, 20))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.currentSpeedTxt.setFont(font)
        self.currentSpeedTxt.setFrameShape(QtWidgets.QFrame.Box)
        self.currentSpeedTxt.setText("Current speed:")
        self.currentSpeedTxt.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.currentSpeedTxt.setObjectName("currentSpeedTxt")
        self.currentHeadingTxt = QtWidgets.QLabel(self.centralwidget)
        self.currentHeadingTxt.setGeometry(QtCore.QRect(250, 360, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.currentHeadingTxt.setFont(font)
        self.currentHeadingTxt.setFrameShape(QtWidgets.QFrame.Box)
        self.currentHeadingTxt.setText("Current heading:")
        self.currentHeadingTxt.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.currentHeadingTxt.setObjectName("currentHeadingTxt")
        self.depthTxt = QtWidgets.QLabel(self.centralwidget)
        self.depthTxt.setGeometry(QtCore.QRect(430, 390, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.depthTxt.setFont(font)
        self.depthTxt.setFrameShape(QtWidgets.QFrame.Box)
        self.depthTxt.setText("Depth:")
        self.depthTxt.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.depthTxt.setObjectName("depthTxt")
        self.zTxt = QtWidgets.QLabel(self.centralwidget)
        self.zTxt.setGeometry(QtCore.QRect(430, 480, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.zTxt.setFont(font)
        self.zTxt.setFrameShape(QtWidgets.QFrame.Box)
        self.zTxt.setText("Z acc:")
        self.zTxt.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.zTxt.setObjectName("zTxt")
        self.yTxt = QtWidgets.QLabel(self.centralwidget)
        self.yTxt.setGeometry(QtCore.QRect(430, 450, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.yTxt.setFont(font)
        self.yTxt.setFrameShape(QtWidgets.QFrame.Box)
        self.yTxt.setText("Y acc:")
        self.yTxt.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.yTxt.setObjectName("yTxt")
        self.xTxt = QtWidgets.QLabel(self.centralwidget)
        self.xTxt.setGeometry(QtCore.QRect(430, 420, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.xTxt.setFont(font)
        self.xTxt.setFrameShape(QtWidgets.QFrame.Box)
        self.xTxt.setText("X acc:")
        self.xTxt.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.xTxt.setObjectName("xTxt")
        
        #timer labels
        self.startBtn = QtWidgets.QPushButton(self.centralwidget,clicked=lambda: self.start())
        self.startBtn.setGeometry(QtCore.QRect(370, 320, 75, 23))
        self.startBtn.setObjectName("startBtn")
        self.stopBtn = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.stop())
        self.stopBtn.setGeometry(QtCore.QRect(450, 320, 75, 23))
        self.stopBtn.setObjectName("stopBtn")
        
        #mode buttons
        self.manualBtn = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.clickModeButton("Manual"))
        self.manualBtn.setGeometry(QtCore.QRect(610, 490, 81, 23))
        self.manualBtn.setObjectName("manualBtn")
        
        self.stabilizeBtn = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.clickModeButton("Stabilize"))
        self.stabilizeBtn.setGeometry(QtCore.QRect(610, 460, 81, 23))
        self.stabilizeBtn.setObjectName("stabilizeBtn")
        
        self.depthHoldBtn = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.clickModeButton("Depth hold"))
        self.depthHoldBtn.setGeometry(QtCore.QRect(610, 430, 81, 23))
        self.depthHoldBtn.setObjectName("depthHoldBtn")
        
        self.autonmousBtn = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.clickModeButton("Autonmous"))
        self.autonmousBtn.setGeometry(QtCore.QRect(610, 400, 81, 23))
        self.autonmousBtn.setObjectName("autonmousBtn")
        
        self.runBtn = QtWidgets.QPushButton(self.centralwidget)
        self.runBtn.setGeometry(QtCore.QRect(700, 320, 75, 23))
        self.runBtn.setObjectName("runBtn")
        self.codeComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.codeComboBox.setGeometry(QtCore.QRect(610, 320, 81, 22))
        self.codeComboBox.setObjectName("codeComboBox")
        self.codeComboBox.addItem("")
        self.codeComboBox.addItem("")
        
        
        self.timer = QtWidgets.QLabel(self.centralwidget)
        self.timer.setGeometry(QtCore.QRect(440, 350, 91, 20))
        
        
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.timer.setFont(font)
        self.timer.setText("00:00:00")
        self.timer.setAlignment(QtCore.Qt.AlignCenter)
        self.timer.setObjectName("timer")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(50, 410, 101, 101))
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.grapperRightBtn = QtWidgets.QPushButton(self.centralwidget)
        self.grapperRightBtn.setEnabled(True)
        self.grapperRightBtn.setGeometry(QtCore.QRect(160, 330, 80, 61))
        self.grapperRightBtn.setToolTip("")
        self.grapperRightBtn.setWhatsThis("")
        self.grapperRightBtn.setAutoFillBackground(False)
        self.grapperRightBtn.setText("")
        self.grapperRightBtn.setShortcut("")
        self.grapperRightBtn.setCheckable(False)
        self.grapperRightBtn.setAutoDefault(False)
        self.grapperRightBtn.setDefault(False)
        self.grapperRightBtn.setFlat(True)
        self.grapperRightBtn.setObjectName("grapperRightBtn")
        self.upBtn = QtWidgets.QPushButton(self.centralwidget)
        self.upBtn.setEnabled(True)
        self.upBtn.setGeometry(QtCore.QRect(80, 410, 41, 41))
        self.upBtn.setToolTip("")
        self.upBtn.setWhatsThis("")
        self.upBtn.setAutoFillBackground(False)
        self.upBtn.setText("")
        self.upBtn.setShortcut("")
        self.upBtn.setCheckable(False)#
        self.upBtn.setAutoDefault(False)
        self.upBtn.setDefault(False)
        self.upBtn.setFlat(True)
        self.upBtn.setObjectName("upBtn")
        self.upArrowBtn = QtWidgets.QPushButton(self.centralwidget)
        self.upArrowBtn.setEnabled(True)
        self.upArrowBtn.setGeometry(QtCore.QRect(280, 410, 41, 51))
        self.upArrowBtn.setToolTip("")
        self.upArrowBtn.setWhatsThis("")
        self.upArrowBtn.setAutoFillBackground(False)
        self.upArrowBtn.setText("")
        self.upArrowBtn.setShortcut("")
        self.upArrowBtn.setCheckable(False)#
        self.upArrowBtn.setAutoDefault(False)
        self.upArrowBtn.setDefault(False)
        self.upArrowBtn.setFlat(True)
        self.upArrowBtn.setObjectName("upArrowBtn")
        self.ccwUpBtn = QtWidgets.QPushButton(self.centralwidget)
        self.ccwUpBtn.setEnabled(True)
        self.ccwUpBtn.setGeometry(QtCore.QRect(160, 430, 80, 41))
        self.ccwUpBtn.setToolTip("")
        self.ccwUpBtn.setWhatsThis("")
        self.ccwUpBtn.setAutoFillBackground(False)
        self.ccwUpBtn.setText("")
        self.ccwUpBtn.setShortcut("")
        self.ccwUpBtn.setCheckable(False)#
        self.ccwUpBtn.setAutoDefault(False)
        self.ccwUpBtn.setDefault(False)
        self.ccwUpBtn.setFlat(True)
        self.ccwUpBtn.setObjectName("ccwUpBtn")
        self.ccwDownBtn = QtWidgets.QPushButton(self.centralwidget)
        self.ccwDownBtn.setEnabled(True)
        self.ccwDownBtn.setGeometry(QtCore.QRect(160, 470, 80, 41))
        self.ccwDownBtn.setToolTip("")
        self.ccwDownBtn.setWhatsThis("")
        self.ccwDownBtn.setAutoFillBackground(False)
        self.ccwDownBtn.setText("")
        self.ccwDownBtn.setShortcut("")
        self.ccwDownBtn.setCheckable(False)#
        self.ccwDownBtn.setAutoDefault(False)
        self.ccwDownBtn.setDefault(False)
        self.ccwDownBtn.setFlat(True)
        self.ccwDownBtn.setObjectName("ccwDownBtn")
        self.downArrowBtn = QtWidgets.QPushButton(self.centralwidget)
        self.downArrowBtn.setEnabled(True)
        self.downArrowBtn.setGeometry(QtCore.QRect(280, 460, 41, 51))
        self.downArrowBtn.setToolTip("")
        self.downArrowBtn.setWhatsThis("")
        self.downArrowBtn.setAutoFillBackground(False)
        self.downArrowBtn.setText("")
        self.downArrowBtn.setShortcut("")
        self.downArrowBtn.setCheckable(False)#
        self.downArrowBtn.setAutoDefault(False)
        self.downArrowBtn.setDefault(False)
        self.downArrowBtn.setFlat(True)
        self.downArrowBtn.setObjectName("downArrowBtn")
        self.downBtn = QtWidgets.QPushButton(self.centralwidget)
        self.downBtn.setEnabled(True)
        self.downBtn.setGeometry(QtCore.QRect(80, 470, 41, 41))
        self.downBtn.setToolTip("")
        self.downBtn.setWhatsThis("")
        self.downBtn.setAutoFillBackground(False)
        self.downBtn.setText("")
        self.downBtn.setShortcut("")
        self.downBtn.setCheckable(False)#
        self.downBtn.setAutoDefault(False)
        self.downBtn.setDefault(False)
        self.downBtn.setFlat(True)
        self.downBtn.setObjectName("downBtn")
        self.rightBtn = QtWidgets.QPushButton(self.centralwidget)
        self.rightBtn.setEnabled(True)
        self.rightBtn.setGeometry(QtCore.QRect(110, 440, 41, 41))
        self.rightBtn.setToolTip("")
        self.rightBtn.setWhatsThis("")
        self.rightBtn.setAutoFillBackground(False)
        self.rightBtn.setText("")
        self.rightBtn.setShortcut("")
        self.rightBtn.setCheckable(False)#
        self.rightBtn.setAutoDefault(False)
        self.rightBtn.setDefault(False)
        self.rightBtn.setFlat(True)
        self.rightBtn.setObjectName("rightBtn")
        self.leftBtn = QtWidgets.QPushButton(self.centralwidget)
        self.leftBtn.setEnabled(True)
        self.leftBtn.setGeometry(QtCore.QRect(50, 440, 41, 41))
        self.leftBtn.setToolTip("")
        self.leftBtn.setWhatsThis("")
        self.leftBtn.setAutoFillBackground(False)
        self.leftBtn.setText("")
        self.leftBtn.setShortcut("")
        self.leftBtn.setCheckable(False)#
        self.leftBtn.setAutoDefault(False)
        self.leftBtn.setDefault(False)
        self.leftBtn.setFlat(True)
        self.leftBtn.setObjectName("leftBtn")
        self.frame_4 = QtWidgets.QFrame(self.centralwidget)
        self.frame_4.setGeometry(QtCore.QRect(50, 310, 101, 101))
        self.frame_4.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.grapperUpBtn = QtWidgets.QPushButton(self.frame_4)
        self.grapperUpBtn.setEnabled(True)
        self.grapperUpBtn.setGeometry(QtCore.QRect(10, 20, 80, 61))
        self.grapperUpBtn.setToolTip("")
        self.grapperUpBtn.setWhatsThis("")
        self.grapperUpBtn.setAutoFillBackground(False)
        self.grapperUpBtn.setText("")
        self.grapperUpBtn.setShortcut("")
        self.grapperUpBtn.setCheckable(False)#
        self.grapperUpBtn.setAutoDefault(False)
        self.grapperUpBtn.setDefault(False)
        self.grapperUpBtn.setFlat(True)
        self.grapperUpBtn.setObjectName("grapperUpBtn")
        self.frame_6 = QtWidgets.QFrame(self.centralwidget)
        self.frame_6.setGeometry(QtCore.QRect(250, 410, 101, 101))
        self.frame_6.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.frame_8 = QtWidgets.QFrame(self.centralwidget)
        self.frame_8.setGeometry(QtCore.QRect(150, 310, 101, 101))
        self.frame_8.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.frame_7 = QtWidgets.QFrame(self.centralwidget)
        self.frame_7.setGeometry(QtCore.QRect(150, 410, 101, 101))
        self.frame_7.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.frame_9 = QtWidgets.QFrame(self.centralwidget)
        self.frame_9.setGeometry(QtCore.QRect(250, 310, 101, 101))
        self.frame_9.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.scriptsLabel = QtWidgets.QLabel(self.centralwidget)
        self.scriptsLabel.setGeometry(QtCore.QRect(670, 300, 41, 16))
        self.scriptsLabel.setObjectName("scriptsLabel")
        self.sensorReadingsLabel = QtWidgets.QLabel(self.centralwidget)
        self.sensorReadingsLabel.setGeometry(QtCore.QRect(430, 370, 101, 20))
        self.sensorReadingsLabel.setObjectName("sensorReadingsLabel")
        self.vehicleIndicatorsLabel = QtWidgets.QLabel(self.centralwidget)
        self.vehicleIndicatorsLabel.setGeometry(QtCore.QRect(50, 290, 111, 20))
        self.vehicleIndicatorsLabel.setObjectName("vehicleIndicatorsLabel")
        self.timerLabel = QtWidgets.QLabel(self.centralwidget)
        self.timerLabel.setGeometry(QtCore.QRect(470, 300, 41, 16))
        self.timerLabel.setObjectName("timerLabel")
        self.currentModeLabel = QtWidgets.QLabel(self.centralwidget)
        self.currentModeLabel.setGeometry(QtCore.QRect(610, 360, 91, 16))
        self.currentModeLabel.setObjectName("currentModeLabel")
        
        #mode label
        self.modeLB = QtWidgets.QLabel(self.centralwidget)
        self.modeLB.setGeometry(QtCore.QRect(720, 360, 58, 16))
        self.modeLB.setObjectName("modeLB")
        
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #Habiba Ahmed --------------------------------------
        def grapperRightBtn_clicked(self):
            self.grapperRightBtn.setCheckable(True)
            if (self.grapperRightBtn.getChecked):
                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap("icons/grapper-open.png"), QtGui.QIcon.Active)
                icon.addPixmap(QtGui.QPixmap("icons/grapper-close.png"), QtGui.QIcon.Disabled)
                self.upwardred.setIcon(icon)

            else:
                icon = QtGui.QIcon()
    
                icon.addPixmap(QtGui.QPixmap("icons/grapper-open.png"), QtGui.QIcon.Disabled)
                icon.addPixmap(QtGui.QPixmap("icons/grapper-close.png"), QtGui.QIcon.Active)
                self.upwardred.setIcon(icon)

        def grapperUpBtn_clicked(self):
            self.grapperUpBtn.setCheckable(True)
            if (self.grapperUpBtn.getChecked):
                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap("icons/grapper-open-horizontal.png"), QtGui.QIcon.Active)
                icon.addPixmap(QtGui.QPixmap("icons/grapper-close-horizontalpng.png"), QtGui.QIcon.Disabled)
                self.upwardred.setIcon(icon)

            else:
                icon = QtGui.QIcon()
    
                icon.addPixmap(QtGui.QPixmap("icons/grapper-open-horizontal.png"), QtGui.QIcon.Disabled)
                icon.addPixmap(QtGui.QPixmap("icons/grapper-close-horizontalpng.png"), QtGui.QIcon.Active)
                self.upwardred.setIcon(icon)

        def leftBtn(self):
            self.leftBtn.setCheckable(True)
            if (self.leftBtn.getChecked):
                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap("icons/left-arrowred.png"), QtGui.QIcon.Active)
                icon.addPixmap(QtGui.QPixmap("icons/left-arrow.png"), QtGui.QIcon.Disabled)
                self.upwardred.setIcon(icon)

            else:
                icon = QtGui.QIcon()
    
                icon.addPixmap(QtGui.QPixmap("icons/left-arrowred.png"), QtGui.QIcon.Disabled)
                icon.addPixmap(QtGui.QPixmap("icons/left-arrow.png"), QtGui.QIcon.Active)
                self.upwardred.setIcon(icon)
        
        #Zeina Mohamed ----------------------------
        def rightBtn(self):
            self.rightBtn.setCheckable(True)
            if (self.rightBtn.getChecked):
                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap("icons/right-arrowred.png"), QtGui.QIcon.Active)
                icon.addPixmap(QtGui.QPixmap("icons/right-arrow.png"), QtGui.QIcon.Disabled)
                self.upwardred.setIcon(icon)

            else:
                icon = QtGui.QIcon()
    
                icon.addPixmap(QtGui.QPixmap("icons/right-arrowred.png"), QtGui.QIcon.Disabled)
                icon.addPixmap(QtGui.QPixmap("icons/right-arrow.png"), QtGui.QIcon.Active)
                self.upwardred.setIcon(icon)


        def downBtn_clicked(self): 
            self.downBtn.setCheckable(True)
            if (self.downBtn.getChecked):
                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap("icons/downward-arrowed.png"), QtGui.QIcon.Active)
                icon.addPixmap(QtGui.QPixmap("icons/downward-arrow.png"), QtGui.QIcon.Disabled)
                self.upwardred.setIcon(icon)

            else:
                icon = QtGui.QIcon()
    
                icon.addPixmap(QtGui.QPixmap("icons/downward-arrowed.png"), QtGui.QIcon.Disabled)
                icon.addPixmap(QtGui.QPixmap("icons/downward-arrow.png"), QtGui.QIcon.Active)
                self.upwardred.setIcon(icon)

        
        def downArrowBtn_clicked(self):
            self.downArrowBtn.setCheckable(True)
            if (self.downArrowBtn.getChecked):
                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap("icons/downward-arrowed.png"), QtGui.QIcon.Active)
                icon.addPixmap(QtGui.QPixmap("icons/downward-arrow.png"), QtGui.QIcon.Disabled)
                self.upwardred.setIcon(icon)

            else:
                icon = QtGui.QIcon()
    
                icon.addPixmap(QtGui.QPixmap("icons/downward-arrowed.png"), QtGui.QIcon.Disabled)
                icon.addPixmap(QtGui.QPixmap("icons/downward-arrow.png"), QtGui.QIcon.Active)
                self.upwardred.setIcon(icon)


        #Manar Adel -----------------------------------
        def ccwDownBtn_clicked(self):
            self.ccwUpBtn.setCheckable(True)
            if (self.ccwUpBtn.getChecked):
                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap("icons/cwred.png"), QtGui.QIcon.Active)
                icon.addPixmap(QtGui.QPixmap("icons/cw.png"), QtGui.QIcon.Disabled)
                self.upwardred.setIcon(icon)

            else:
                icon = QtGui.QIcon()
    
                icon.addPixmap(QtGui.QPixmap("icons/cwred.png"), QtGui.QIcon.Disabled)
                icon.addPixmap(QtGui.QPixmap("icons/cw.png"), QtGui.QIcon.Active)
                self.upwardred.setIcon(icon)


        def ccwUpBtn_clicked(self):
            self.grapperRightBtn.setCheckable(True)
            if (self.grapperRightBtn.getChecked):
                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap("icons/ccwred.png"), QtGui.QIcon.Active)
                icon.addPixmap(QtGui.QPixmap("icons/ccw.png"), QtGui.QIcon.Disabled)
                self.upwardred.setIcon(icon)

            else:
                icon = QtGui.QIcon()
    
                icon.addPixmap(QtGui.QPixmap("icons/ccwred.png"), QtGui.QIcon.Disabled)
                icon.addPixmap(QtGui.QPixmap("icons/ccw.png"), QtGui.QIcon.Active)
                self.upwardred.setIcon(icon)
       
        def upArrowBtn_clicked(self):
            self.upArrowBtn.setCheckable(True)
            if (self.upArrowBtn.getChecked):
                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap("icons/frward-arrowed.png"), QtGui.QIcon.Active)
                icon.addPixmap(QtGui.QPixmap("icons/frward-arrow.png"), QtGui.QIcon.Disabled)
                self.upwardred.setIcon(icon)

            else:
                icon = QtGui.QIcon()
    
                icon.addPixmap(QtGui.QPixmap("icons/frward-arrowed.png"), QtGui.QIcon.Disabled)
                icon.addPixmap(QtGui.QPixmap("icons/frward-arrow.png"), QtGui.QIcon.Active)
                self.upwardred.setIcon(icon)

            def upBtn_clicked(self):
                self.upBtn.setCheckable(True)
                if (self.upBtn.getChecked):
                    icon = QtGui.QIcon()
                    icon.addPixmap(QtGui.QPixmap("icons/upward-arrow.png"), QtGui.QIcon.Active)
                    icon.addPixmap(QtGui.QPixmap("icons/upward-arrowred.png"), QtGui.QIcon.Disabled)
                    self.upwardred.setIcon(icon)

                else:
                    icon = QtGui.QIcon()
        
                    icon.addPixmap(QtGui.QPixmap("icons/upward-arrowed.png"), QtGui.QIcon.Disabled)
                    icon.addPixmap(QtGui.QPixmap("icons/upward-arrow.png"), QtGui.QIcon.Active)
                    self.upwardred.setIcon(icon)
        
        
        
 #Habiba Ahmed, Zeina Mohamed, Manar Adel  ---------------------------------     
        
    #for the camera    
    def ImageUpdateSlot(self, Image):
        self.camera1Label.setPixmap(QPixmap.fromImage(Image)) 
        
        
        
    #codes
    def reset(self):#sha8al
        global count
        count=1
        self.timer.setText('00:00:00')  
        
    def start(self): #sha8al
        global count
        count=0
        if count==0:
            self.root=Tk()#el moshkla fel bt3ha de el bethaneg el laptop
            self.timerT()
        
    def stop(self):
        global count
        count=1
        
            
    def timerT(self): #sha8al bs m7tag tazbeet
        global count
        

        self.t = StringVar()
        self.t.set(self.timer.text())
        if(count==0):
            self.d = str(self.t.get())
            h,m,s = map(int,self.d.split(":")) 
            h = int(h)
            m=int(m)
            s= int(s)
            if(s<59):
                s+=1
            elif(s==59):
                s=0
                if(m<59):
                    m+=1
                elif(m==59):
                    m=0
                    h+=1
            if(h<10):
                h = str(0)+str(h)
            else:
                h= str(h)
            if(m<10):
                m = str(0)+str(m)
            else:
                m = str(m)
            if(s<10):
                s=str(0)+str(s)
            else:
                s=str(s)
            self.d=h+":"+m+":"+s           
            self.t.set(self.d)
            self.timer.setText(self.t.get())
            if(count==0):
                self.root.after(1000,self.timerT)
                
            self.root.mainloop() 
            
    #change model label when clicking a button
    def clickModeButton(self,pressed):
        if pressed=="Autonmous":
            self.modeLB.setText("Autonmous")  
        elif pressed =="Depth hold":
            self.modeLB.setText("Depth hold")
        elif pressed =="Stabilize":
            self.modeLB.setText("Stabilize")   
        elif pressed =="Manual":
            self.modeLB.setText("Manual")  
    

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.resetBtn.setText(_translate("MainWindow", "Reset"))
        self.startBtn.setText(_translate("MainWindow", "Start"))
        self.stopBtn.setText(_translate("MainWindow", "Stop"))
        self.manualBtn.setText(_translate("MainWindow", "Manual"))
        self.stabilizeBtn.setText(_translate("MainWindow", "Stabilize"))
        self.depthHoldBtn.setText(_translate("MainWindow", "Depth hold"))
        self.autonmousBtn.setText(_translate("MainWindow", "Autonmous"))
        self.runBtn.setText(_translate("MainWindow", "Run"))
        self.codeComboBox.setItemText(0, _translate("MainWindow", "Code 1"))
        self.codeComboBox.setItemText(1, _translate("MainWindow", "Code 2"))
        self.scriptsLabel.setText(_translate("MainWindow", "Scripts"))
        self.sensorReadingsLabel.setText(_translate("MainWindow", "Sensor Readings"))
        self.vehicleIndicatorsLabel.setText(_translate("MainWindow", "Vehicle Indicators"))
        self.timerLabel.setText(_translate("MainWindow", "Timer"))
        self.currentModeLabel.setText(_translate("MainWindow", "Current Mode"))
        self.modeLB.setText(_translate("MainWindow", "mode"))


 #Habiba Ahmed, Zeina Mohamed, Manar Adel -----------------------------------

#camera code
class Worker1(QThread):
    ImageUpdate = pyqtSignal(QImage)
    def run(self):
        self.ThreadActive = True
        self.adrr = ('0.0.0.0',12345)
        self.lis = l(self.adrr, authkey=b'bsa')
        self.conn = self.lis.accept()
        while self.ThreadActive:
            packet = self.conn.recv()
            data = base64.b64decode(packet,' /')
            npdata = np.fromstring(data,dtype=np.uint8)
            frame = cv.imdecode(npdata,1)
            frame = cv.flip(frame, 1)
            converted = QImage(frame, frame.shape[1],
                            frame.shape[0], frame.shape[1] * 3,QImage.Format_RGB888).rgbSwapped()
            Pic = converted.scaled(640, 480, Qt.KeepAspectRatio)
            self.ImageUpdate.emit(Pic)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
