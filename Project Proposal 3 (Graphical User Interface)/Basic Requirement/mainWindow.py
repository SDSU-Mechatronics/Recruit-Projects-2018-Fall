# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(949, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.degrees = QtGui.QLabel(self.centralwidget)
        self.degrees.setGeometry(QtCore.QRect(650, 20, 57, 14))
        self.degrees.setText(_fromUtf8(""))
        self.degrees.setObjectName(_fromUtf8("degrees"))
        self.upperHue = QtGui.QSlider(self.centralwidget)
        self.upperHue.setGeometry(QtCore.QRect(650, 100, 280, 16))
        self.upperHue.setMaximum(180)
        self.upperHue.setProperty("value", 180)
        self.upperHue.setOrientation(QtCore.Qt.Horizontal)
        self.upperHue.setObjectName(_fromUtf8("upperHue"))
        self.lowerHue = QtGui.QSlider(self.centralwidget)
        self.lowerHue.setGeometry(QtCore.QRect(650, 120, 280, 16))
        self.lowerHue.setMaximum(180)
        self.lowerHue.setOrientation(QtCore.Qt.Horizontal)
        self.lowerHue.setObjectName(_fromUtf8("lowerHue"))
        self.upperSaturation = QtGui.QSlider(self.centralwidget)
        self.upperSaturation.setGeometry(QtCore.QRect(650, 160, 280, 16))
        self.upperSaturation.setMaximum(255)
        self.upperSaturation.setSliderPosition(255)
        self.upperSaturation.setOrientation(QtCore.Qt.Horizontal)
        self.upperSaturation.setObjectName(_fromUtf8("upperSaturation"))
        self.lowerSaturation = QtGui.QSlider(self.centralwidget)
        self.lowerSaturation.setGeometry(QtCore.QRect(650, 180, 280, 16))
        self.lowerSaturation.setMaximum(255)
        self.lowerSaturation.setOrientation(QtCore.Qt.Horizontal)
        self.lowerSaturation.setObjectName(_fromUtf8("lowerSaturation"))
        self.upperValue = QtGui.QSlider(self.centralwidget)
        self.upperValue.setGeometry(QtCore.QRect(650, 220, 280, 16))
        self.upperValue.setMaximum(255)
        self.upperValue.setSliderPosition(255)
        self.upperValue.setOrientation(QtCore.Qt.Horizontal)
        self.upperValue.setObjectName(_fromUtf8("upperValue"))
        self.lowerValue = QtGui.QSlider(self.centralwidget)
        self.lowerValue.setGeometry(QtCore.QRect(650, 240, 280, 16))
        self.lowerValue.setMaximum(255)
        self.lowerValue.setSliderPosition(0)
        self.lowerValue.setOrientation(QtCore.Qt.Horizontal)
        self.lowerValue.setObjectName(_fromUtf8("lowerValue"))
        self.videoFeed = QtGui.QLabel(self.centralwidget)
        self.videoFeed.setGeometry(QtCore.QRect(0, 20, 640, 480))
        self.videoFeed.setText(_fromUtf8(""))
        self.videoFeed.setObjectName(_fromUtf8("videoFeed"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(650, 80, 31, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(650, 140, 71, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(650, 200, 41, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 949, 19))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label.setText(_translate("MainWindow", "Hue", None))
        self.label_2.setText(_translate("MainWindow", "Saturation", None))
        self.label_3.setText(_translate("MainWindow", "Value", None))

