import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import QApplication, QMainWindow
from mainWindow import Ui_MainWindow
from threading import Thread
import cv2
import numpy as np

class mainWindow(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.upperHue.valueChanged.connect(self.updateUpperHue)
        self.ui.lowerHue.valueChanged.connect(self.updateLowerHue)
        self.ui.upperSaturation.valueChanged.connect(self.updateUpperSaturation)
        self.ui.lowerSaturation.valueChanged.connect(self.updateLowerSaturation)
        self.ui.upperValue.valueChanged.connect(self.updateUpperValue)
        self.ui.lowerValue.valueChanged.connect(self.updateLowerValue)
        self.active = True
        self.uHue = 180
        self.lHue = 0
        self.uSat = 255
        self.lSat = 0
        self.uVal = 255
        self.lVal = 0

    def updateUpperHue(self, val):
        self.uHue = val

    def updateLowerHue(self, val):
        self.lHue = val

    def updateUpperSaturation(self, val):
        self.uSat = val

    def updateLowerSaturation(self, val):
        self.lSat = val

    def updateUpperValue(self, val):
        self.uVal = val

    def updateLowerValue(self, val):
        self.lVal = val

    def feedVideo(self, img):
        #img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        frame = QtGui.QImage(img, img.shape[1], img.shape[0], QtGui.QImage.Format_RGB888)
        pix = QtGui.QPixmap.fromImage(frame)
        self.ui.videoFeed.setPixmap(pix)

    def updateDegrees(self, degrees):
        self.ui.degrees.setText("{}".format(degrees))

    def closeEvent(self, event):
        self.active = False

    def isActive(self):
        return self.active

app = QApplication(sys.argv)
window = mainWindow()

cap = cv2.VideoCapture(0)

window.show()
app.exec_()
while window.isActive():
    ret, frame = cap.read()
    window.feedVideo(frame)

    #HSV Filtering
#    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
#    lower_hsv = np.array([window.lHue, window.lSat, window.lVal])
#    upper_hsv = np.array([window.uHue, window.uSat, window.uVal])

#    mask = cv2.inRange(hsv, lower_hsv, upper_hsv)
#    res = cv2.bitwise_and(frame, frame, mask=mask)

    #Load to GUI
    res = cv2.cvtColor(res, cv2.COLOR_BGR2RGB)
#    res = frame
    window.feedVideo(res)
    window.updateDegrees(0)

cv2.destroyAllWindows()
cap.release()
