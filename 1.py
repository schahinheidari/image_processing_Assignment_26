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

    
    for (x, y, w, h) in faces:
        cv.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
        frame[y:y+h, x:x+w] = cv.medianBlur(frame[y:y+h, x:x+w],35)

    cv.imshow("thresh", frame)
    if cv.waitKey(25) & 0xFF == ord("q"):
        break

cap.release()
cv.destroyAllWindows()
