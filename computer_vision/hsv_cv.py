import cv2
import numpy as np
cap=cv2.VideoCapture(0)
while True:
	ret,frame=cap.read()
	hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
	l=np.array([0,150,150])
	u=np.array([255,255,255])
	mask=cv2.inRange(hsv,l,u)
	res=cv2.bitwise_and(frame,frame,mask=mask)
	cv2.imshow('res',res)
	if cv2.waitKey(1) & 0xFF == ord('q'): #python takes only one & for and operation not &&
		break
cap.release()
cv2.destroyAllWindows()
