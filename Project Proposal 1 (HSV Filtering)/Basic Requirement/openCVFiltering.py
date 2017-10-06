import cv2
import numpy as np

#GLOBALS
LOWER_POS = 0
UPPER_HUE = 180
UPPER_OTH = 255

#Default for Trackbar
def nothing(x):
	pass

cap = cv2.VideoCapture(0)

cv2.namedWindow("image")

#Creating Trackbar
cv2.createTrackbar('UpperHue',        'image', LOWER_POS, UPPER_HUE, nothing)
cv2.createTrackbar('LowerHue',        'image', LOWER_POS, UPPER_HUE, nothing)
cv2.createTrackbar('UpperSaturation', 'image', LOWER_POS, UPPER_OTH, nothing)
cv2.createTrackbar('LowerSaturation', 'image', LOWER_POS, UPPER_OTH, nothing)
cv2.createTrackbar('UpperValue',      'image', LOWER_POS, UPPER_OTH, nothing)
cv2.createTrackbar('LowerValue',      'image', LOWER_POS, UPPER_OTH, nothing)

#Setting Upperbound defaults
cv2.setTrackbarPos('UpperHue',        'image', UPPER_HUE)
cv2.setTrackbarPos('UpperSaturation', 'image', UPPER_OTH)
cv2.setTrackbarPos('UpperValue',      'image', UPPER_OTH)


while True:
	#Getting frame data from video camera
	ret, frame = cap.read()
	#Convert color data to HSV
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
	
	#Getting the upper and lower bounds for the filter from the trackbar
	lower_hsv = np.array([cv2.getTrackbarPos('LowerHue', 'image'), cv2.getTrackbarPos('LowerSaturation', 'image'), cv2.getTrackbarPos('LowerValue', 'image')])
	upper_hsv = np.array([cv2.getTrackbarPos('UpperHue', 'image'), cv2.getTrackbarPos('UpperSaturation', 'image'), cv2.getTrackbarPos('UpperValue', 'image')])

	mask = cv2.inRange(hsv, lower_hsv, upper_hsv)
	res  = cv2.bitwise_and(frame, frame, mask=mask)
	
	#Hough Circles
#	gres = cv2.cvtColor(cv2.cvtColor(res, cv2.COLOR_HSV2BGR), cv2.COLOR_BGR2GRAY)
#	print("Converted to gray")
#	circles = cv2.HoughCircles(gres, cv2.HOUGH_GRADIENT, 1, 20, param1=50, param2=30, minRadius=0,maxRadius=0)
#	print("Found Circles")
#	circles = np.uint16(np.around(circles))
#	print(len(circles) + " circles")
#	for i in circles[0,:]:
#		cv2.circle(res, (i[0], i[1]), i[2], (0, 255, 0), 2)

	#Canny Edge Detection
	edges = cv2.Canny(frame, 100, 200) #Figure out what thresholds do

	cv2.imshow('result', res)
	cv2.imshow('edges', edges)

	#Waits for a q or esc to exit
	k = cv2.waitKey(1)
	if k == ord('q') or k == 27:
		break

#Cleanup
cv2.destroyAllWindows()
cap.release()
