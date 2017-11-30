import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import QApplication, QMainWindow, QImage
from PyQt4.QtCore import QThread, SIGNAL
from mainWindow import Ui_MainWindow
from threading import Thread
import cv2
import numpy as np

class mainWindow(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.upperHue.valueChanged.connect(self.updateUpperHue)
        self.ui.lowerHue.valueChanged.connect(self.updateLowerHue)
        self.ui.upperSaturation.valueChanged.connect(self.updateUpperSaturation)
        self.ui.lowerSaturation.valueChanged.connect(self.updateLowerSaturation)
        self.ui.upperValue.valueChanged.connect(self.updateUpperValue)
        self.ui.lowerValue.valueChanged.connect(self.updateLowerValue)
        self.video = videoThread(self)
        self.video.start()
        self.ui.videoFeed.connect(self.video, SIGNAL('newImage'), self.feedVideo)
        self.uHue = 180
        self.lHue = 0
        self.uSat = 255
        self.lSat = 0
        self.uVal = 255
        self.lVal = 0
        self.active = True

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
        pix = QtGui.QPixmap.fromImage(img)
        self.ui.videoFeed.setPixmap(pix)

    def updateDegrees(self, degrees):
        self.ui.degrees.setText("{}".format(degrees))

    def closeEvent(self, event):
        self.active = False

    def isActive(self):
        return self.active

class videoThread(QThread):

    def __init__(self, window):
        QThread.__init__(self)
        self.window = window
        
    def run(self):
        cap = cv2.VideoCapture(0)
        while self.window.isActive():
            _, frame = cap.read()
            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            lower_hsv = np.array([window.lHue, window.lSat, window.lVal])
            upper_hsv = np.array([window.uHue, window.uSat, window.uVal])

            mask = cv2.inRange(hsv, lower_hsv, upper_hsv)

            #Compute Degrees
            counter = 0
            xVals = 0
            for (y, x), val in np.ndenumerate(mask):
                if mask[y][x] == 255:
                    counter += 1
                    xVals += x
            if counter == 0:
                degrees = 0
            else:
                degrees = xVals/counter
            
            self.window.updateDegrees(degrees)


            res = cv2.bitwise_and(frame, frame, mask=mask)
            image = QImage(res.tostring(), res.shape[1], res.shape[0], QImage.Format_RGB888).rgbSwapped()
            self.emit(SIGNAL('newImage'), image)

app = QApplication(sys.argv)
window = mainWindow()

window.show()
sys.exit(app.exec_())
