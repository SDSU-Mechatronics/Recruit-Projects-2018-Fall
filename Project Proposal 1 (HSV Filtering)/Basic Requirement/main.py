import cv2
import numpy

def HSV_Filter(source, hsvMin, hsvMax):
    frame = cv2.cvtColor(source, cv2.COLOR_BGR2HSV)
    
    mask = cv2.inRange(frame, hsvMin, hsvMax)
    
    frame = cv2.bitwise_and(frame, frame, mask = mask)

    frame = cv2.cvtColor(frame, cv2.COLOR_HSV2BGR)
    
    return frame

def Canny_Edge(source, threshMin):
    frame = cv2.Canny(source, threshMin, 200)
    return frame


def Hough_Circles(source, dp):
    output = source.copy()
    
    gray = cv2.cvtColor(source, cv2.COLOR_BGR2GRAY)
    
    circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, dp, 100)
    
    if circles is not None:
        for val in circles:
            cv2.circle(output, (val[0][0], val[0][1]), val[0][2], (0, 255, 0), 4)
    
    return output


def Hough_Circles_HSV(source, hsvFilter, dp):    
    output = source.copy()
    
    gray = cv2.cvtColor(hsvFilter, cv2.COLOR_BGR2GRAY)
    
    circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, dp, 100)
    
    if circles is not None:
        for val in circles:
            cv2.circle(output, (val[0][0], val[0][1]), val[0][2], (0, 255, 0), 4)
    
    return output

class Foo:
    def __call__(self, _):
        pass

cap = cv2.VideoCapture(0)
Options_name = "Options"
cv2.namedWindow(Options_name, cv2.WINDOW_NORMAL)
cv2.resizeWindow(Options_name, 720, 1080)
cv2.createTrackbar("Source", Options_name, 0, 1, Foo())

cv2.createTrackbar("HSV Filter", Options_name, 0, 1, Foo())
cv2.createTrackbar("Hue Min", Options_name, 128, 255, Foo())
cv2.createTrackbar("Hue Max", Options_name, 255, 255, Foo())
cv2.createTrackbar("Sat Min", Options_name, 0, 255, Foo())
cv2.createTrackbar("Sat Max", Options_name, 255, 255, Foo())
cv2.createTrackbar("Value Min", Options_name, 0, 255, Foo())
cv2.createTrackbar("Value Max", Options_name, 255, 255, Foo())

cv2.createTrackbar("Canny Edge", Options_name, 0, 1, Foo())
cv2.createTrackbar("Min", Options_name, 100, 200, Foo())

cv2.createTrackbar("Hough Circles", Options_name, 0, 1, Foo())
cv2.createTrackbar("dp", Options_name, 14, 20, Foo())

cv2.createTrackbar("Hough Circles HSV", Options_name, 0, 1, Foo())

while True:
    b, source = cap.read()
    
    if cv2.getTrackbarPos("Source", Options_name):
        cv2.imshow("Source", source)
    else:
        cv2.destroyWindow("Source")
    
    hsvMin = numpy.array([cv2.getTrackbarPos("Hue Min", Options_name), cv2.getTrackbarPos("Sat Min", Options_name), cv2.getTrackbarPos("Value Min", Options_name)])
    hsvMax = numpy.array([cv2.getTrackbarPos("Hue Max", Options_name), cv2.getTrackbarPos("Sat Max", Options_name), cv2.getTrackbarPos("Value Max", Options_name)])
    if cv2.getTrackbarPos("HSV Filter", Options_name):
        cv2.imshow("HSV Filter", HSV_Filter(source, hsvMin, hsvMax))
    else:
        cv2.destroyWindow("HSV Filter")
    
    threshMin = cv2.getTrackbarPos("Min", Options_name)
    if cv2.getTrackbarPos("Canny Edge", Options_name):
        cv2.imshow("Canny Edge", Canny_Edge(source, threshMin))
    else:
        cv2.destroyWindow("Canny Edge")
        
    dp = cv2.getTrackbarPos("dp", Options_name)/ 10.0
    if cv2.getTrackbarPos("Hough Circles", Options_name):
        cv2.imshow("Hough Circles", Hough_Circles(source, dp))
    else:
        cv2.destroyWindow("Hough Circles")
    
    if cv2.getTrackbarPos("Hough Circles HSV", Options_name):
        cv2.imshow("Hough Circles HSV", Hough_Circles_HSV(source, HSV_Filter(source, hsvMin, hsvMax), dp))
    else:
        cv2.destroyWindow("Hough Circles HSV")
    
    if (cv2.waitKey(100) &0xFF == ord('q')):
        cv2.destroyAllWindows
        break
    
cap.release()