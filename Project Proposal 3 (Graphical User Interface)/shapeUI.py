from PyQt4 import QtGui, QtCore
import cv2
import numpy

class shape_UI(object):  
    def setupUI(self, shapeui):
        self.img = "test2.jpg"
        
        self.hbox = QtGui.QHBoxLayout(shapeui)
        
        self.pic = QtGui.QLabel("Display", shapeui)
        qpix = QtGui.QPixmap(self.img)
        self.pic.setPixmap(qpix)
        
        self.hbox.addWidget(self.pic)
        
        self.hbox.addSpacing(100)
        
        self.vbox = QtGui.QVBoxLayout()
        self.hbox.addLayout(self.vbox)
        
        self.vbox.addSpacing(100)
        
        self.button = QtGui.QPushButton("Detect Shapes", shapeui)
        self.vbox.addWidget(self.button)
        
        QtCore.QObject.connect(self.button, QtCore.SIGNAL("clicked()"), self.DetectShapes)
        
    def DetectShapes(self):
        im = cv2.imread(self.img)
        imgray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        ret, thresh = cv2.threshold(imgray, 127, 255, 0)
        contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        
        height, width = im.shape[:2]
        area = (height-10) * (width-10)
    
        for cnt in contours:
            approx = cv2.approxPolyDP(cnt,0.01*cv2.arcLength(cnt,True),True)
            #print len(approx)
            if len(approx)==5:
                print "pentagon"
                cv2.drawContours(im,[cnt],0,255,-1)
                ser.write('2')
            elif len(approx)==3:
                print "triangle"
                cv2.drawContours(im,[cnt],0,(0,255,0),-1)
                ser.write('1')
            elif len(approx)==4 and cv2.contourArea(cnt) < area:
                print "square"
                cv2.drawContours(im,[cnt],0,(0,0,255),-1)
                ser.write('4')
            elif len(approx) > 15:
                print "circle"
                cv2.drawContours(im,[cnt],0,(0,255,255),-1)
                ser.write('3')
                
        im  = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)
        qimg = QtGui.QImage(im, im.shape[1], im.shape[0], QtGui.QImage.Format_RGB888)
        self.pic.setPixmap(QtGui.QPixmap(qimg))
        
        
if __name__ == "__main__":
    import serial
    import time
    ser = serial.Serial("COM3", 9600)
    time.sleep(2)
    
    import sys
    a = QtGui.QApplication(sys.argv)
    UI = QtGui.QWidget()
    ui = shape_UI()
    ui.setupUI(UI)
    UI.show()
    sys.exit(a.exec_())