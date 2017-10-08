import cv2
import numpy

cap = cv2.VideoCapture(0)

while True:
    b, source = cap.read()
    
    frame = cv2.cvtColor(source, cv2.COLOR_BGR2HSV)
    
    width, height, channels = frame.shape
    
    hsvMin = numpy.array([80, 0, 0])
    hsvMax = numpy.array([125, 255, 255])
    
    mask = cv2.inRange(frame, hsvMin, hsvMax)
    
    frame = cv2.bitwise_and(frame, frame, mask = mask)

    
    '''
    for x in range(width):
        for y in range(height):
            if frame[x][y][0] > 80 and frame[x][y][0] < 125:
                pass
            else:
                frame[x][y][0] = 0
                frame[x][y][1] = 0
                frame[x][y][2] = 0
    '''
    
    frame = cv2.cvtColor(frame, cv2.COLOR_HSV2BGR)
    
    cv2.imshow("Source", source)
    cv2.imshow("Filtered", frame)
    if(cv2.waitKey(10) &0xFF == ord('q')):
        break
        
cap.release()