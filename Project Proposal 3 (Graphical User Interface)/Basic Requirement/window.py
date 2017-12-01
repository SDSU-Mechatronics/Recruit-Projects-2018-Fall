import sys
from PyQt4 import QtGui
from PyQt4.QtGui import QApplication, QMainWindow, QImage
from PyQt4.QtCore import QThread, SIGNAL
from mainWindow import Ui_MainWindow
from time import sleep
import cv2
import math
import numpy as np
import serial


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
        self.deg = degreesThread(self)
        self.deg.start()
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
        self.deg.wait()
        self.video.wait()

    def isActive(self):
        return self.active


class videoThread(QThread):

    def __init__(self, window):
        QThread.__init__(self)
        self.width = 640
        self.height = 480
        self.window = window

    def run(self):
        cap = cv2.VideoCapture(0)
        while self.window.isActive():
            _, frame = cap.read()
            frame = cv2.resize(frame, (self.width, self.height))
            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            lower_hsv = np.array([window.lHue, window.lSat, window.lVal])
            upper_hsv = np.array([window.uHue, window.uSat, window.uVal])

            mask = cv2.inRange(hsv, lower_hsv, upper_hsv)
            window.mask = mask

            res = cv2.bitwise_and(frame, frame, mask=mask)
            image = QImage(res.tostring(), res.shape[1], res.shape[0], QImage.Format_RGB888).rgbSwapped()
            self.emit(SIGNAL('newImage'), image)


class degreesThread(QThread):

    def __init__(self, window):
        QThread.__init__(self)
        self.window = window
        self.mid = 319
        self.pixPerInch = 141.2
        self.distanceToServo = 5
        self.ser = serial.Serial('/dev/ttyACM0')

    def run(self):
        sleep(1)
        while self.window.isActive():
            data = cv2.findNonZero(window.mask)
            x = 0
            if data is None:
                continue
            for pt in data:
                x += pt[0][0]
            avgX = x / len(data)
            disX = (avgX - self.mid)
            if disX != 0:
                print(disX / self.pixPerInch)
                degrees = abs(math.degrees(math.atan((disX / self.pixPerInch) / self.distanceToServo)) - 90)
            else:
                degrees = 90
            window.updateDegrees(degrees)
            self.rotateServo(degrees)
            sleep(.3)
        self.ser.close()

    def rotateServo(self, degrees):
        self.ser.write(b''.join(str(int(degrees))))


app = QApplication(sys.argv)
window = mainWindow()

window.show()
app.exec_()
