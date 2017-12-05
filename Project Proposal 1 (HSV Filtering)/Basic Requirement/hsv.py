
import cv2
import numpy as np

def nothing(x):
    pass

HSV_MIN = 0
HUE_MAX = 180
HSV_MAX = 255

cap = cv2.VideoCapture(0)

cv2.namedWindow("image")

hh = 'Hue High'
hl = 'Hue Low'
sh = 'Saturation High'
sl = 'Saturation Low'
vh = 'Value High'
vl = 'Value Low'

#Trackbar
cv2.createTrackbar(hh, 'image', HSV_MIN, HUE_MAX, nothing)
cv2.createTrackbar(hl, 'image', HSV_MIN, HUE_MAX, nothing)
cv2.createTrackbar(sh, 'image', HSV_MIN, HSV_MAX, nothing)
cv2.createTrackbar(sl, 'image', HSV_MIN, HSV_MAX, nothing)
cv2.createTrackbar(vh, 'image', HSV_MIN, HSV_MAX, nothing)
cv2.createTrackbar(vl, 'image', HSV_MIN, HSV_MAX, nothing)

cv2.setTrackbarPos(hh, 'image', HUE_MAX)
cv2.setTrackbarPos(sh, 'image', HSV_MAX)
cv2.setTrackbarPos(vh, 'image', HSV_MAX)

while True:
    _, frame = cap.read()
    
    #HSV Filtering
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    huh = cv2.getTrackbarPos(hh, 'image')
    hul = cv2.getTrackbarPos(hl, 'image')
    sah = cv2.getTrackbarPos(sh, 'image')
    sal = cv2.getTrackbarPos(sl, 'image')
    vah = cv2.getTrackbarPos(vh, 'image')
    val = cv2.getTrackbarPos(vl, 'image')
    
    '''
    lower_red = np.array([30,150,50])
    upper_red = np.array([255,255,180])
    lower_blue = np.array([110,50,50])
    upper_blue = np.array([130,255,255])
    lower_green = np.array([50, 100, 100])
    upper_green = np.array([70, 255, 255])
    '''
    
    lowHSV = np.array([hul, sal, val])
    highHSV = np.array([huh, sah, vah])
    
    mask = cv2.inRange(hsv, lowHSV, highHSV)
    res  = cv2.bitwise_and(frame, frame, mask=mask)

    #Canny Edge
    edges = cv2.Canny(frame, 100, 200)
    
    #Hough Circles
    output = res.copy()
    
    gray = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)
    
    circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT,50, 100)
    
    if circles is not None:
        for val in circles:
            cv2.circle(output, (val[0][0], val[0][1]), val[0][2], (0, 255, 0), 4)

    
              
    #Display Images
    cv2.imshow('Original Image', frame)
    cv2.imshow('image', res)
    cv2.imshow('Edges', edges)
    cv2.imshow('output', output)

    k = cv2.waitKey(1) & 0xFF
    if k == ord('q') or k == 27:
        break

cv2.destroyAllWindows()
cap.release()