import numpy as np
import  cv2
import math

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

cap = cv2.VideoCapture(0)

while True:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x,y,w,h) in faces:
    	r=int(math.sqrt(((x-w)*(x-w))+((y-h)*(y-h)))/2)
        cv2.circle(img,(x,y),r,(0,255,0),2)
     
    cv2.imshow('img',img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()
