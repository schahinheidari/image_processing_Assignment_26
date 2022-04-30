import numpy as np
import cv2 as cv

faceDetector = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv.VideoCapture(-1)

while True:

    ret, frame = cap.read()
    if ret == False:
        break

    frame = cv.resize(frame,(196,196), fx = 0, fy = 0, interpolation=cv.INTER_CUBIC)
    

    frameGray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    faces = faceDetector.detectMultiScale(frameGray, 1.3)

    # convert the image to grayscale and blur it slightly
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    blurred = cv.GaussianBlur(gray, (7, 7), 0)
    thresh = cv.adaptiveThreshold(blurred, 255,
	cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY_INV, 21, 4)
    for (x, y, w, h) in faces:
        shape  = cv.resize(frame[y:y+h,x:x+w], (25,25))
        

        censoreFace = cv.resize(thresh, (w, h), interpolation=cv.INTER_NEAREST)
        #cv.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 4)
        #Thresh = cv.adaptiveThreshold(frameGray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY_INV, 11, 2)
        frame[y:y+h, x:x+h] = censoreFace
        
        
        


    cv.imshow("thresh", frame)
    if cv.waitKey(25) & 0xFF == ord("q"):
        break

cap.release()
cv.destroyAllWindows()