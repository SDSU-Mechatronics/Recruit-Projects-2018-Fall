import cv2
import numpy


def HSV_Filter(source):
    frame = cv2.cvtColor(source, cv2.COLOR_BGR2HSV)
    
    hsvMin = numpy.array([64, 128, 0])
    hsvMax = numpy.array([128, 255, 255])
    
    mask = cv2.inRange(frame, hsvMin, hsvMax)
    
    frame = cv2.bitwise_and(frame, frame, mask = mask)

    frame = cv2.cvtColor(frame, cv2.COLOR_HSV2BGR)
    
    return frame

def Canny_Edge(source):
    frame = cv2.Canny(source, 100, 200)
    return frame


def Hough_Circles(source):
    output = source.copy()
    
    gray = cv2.cvtColor(source, cv2.COLOR_BGR2GRAY)
    
    circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1.4, 100)
    
    if circles is not None:
        for val in circles:
            cv2.circle(output, (val[0][0], val[0][1]), val[0][2], (0, 255, 0), 4)
    
    return output


def Hough_Circles_HSV(source):
    frame = HSV_Filter(source)
    
    output = source.copy()
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 2, 100)
    
    if circles is not None:
        for val in circles:
            cv2.circle(output, (val[0][0], val[0][1]), val[0][2], (0, 255, 0), 4)
    
    return output

def Contour_Analysis(source):
    output = source.copy()
    '''
    ret, thresh = cv2.threshold(Canny_Edge(output), 1, 1, 1)
    
    _, contours, heirarchy = cv2.findContours(thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    '''
    
    return output

cap = cv2.VideoCapture(0)

while True:
    b, source = cap.read()
    
    cv2.imshow("Filter", HSV_Filter(source))
    cv2.imshow("Source", source)
    cv2.imshow("Canny Edge", Canny_Edge(source))
    #cv2.imshow("Hough Circles", Hough_Circles(source))
    cv2.imshow("Hough Circles HSV", Hough_Circles_HSV(source))
    #cv2.imshow("Contour Analysis", Contour_Analysis(source))
    
    if (cv2.waitKey(100) &0xFF == ord('q')):
        break
    
cap.release()