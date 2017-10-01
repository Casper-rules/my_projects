import numpy as np
import cv2
cap=cv2.VideoCapture(0)
while True:
	ret,frame=cap.read()
	gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
#edge detection
	_,thresh=cv2.threshold(gray,0,50,cv2.THRESH_BINARY + cv2.THRESH_OTSU)
	edge=cv2.Canny(thresh,100,200)
	edge2=cv2.Canny(frame,100,200)
	#cv2.imshow('frame',frame)
	cv2.imshow('thresh',thresh)
	cv2.imshow('edge',edge)
	cv2.imshow('edge2',edge2)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
cap.release()
cv2.destroyAllWindows()

