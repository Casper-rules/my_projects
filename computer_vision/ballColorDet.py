import cv2
import numpy as np
import RPi.GPIO as gpio

gpio.setmode(gpio.BOARD)
#set pins 40 and 38 for GPIO outputs
gpio.setup(38,gpio.OUT) #lsb(because 38<40)
gpio.setup(40,gpio.OUT) #msb(beacause need only two pins and only one option)

#initialize the pins and put them at LOW
gpio.output(38,0)
gpio.output(40,0)

#scanning function
def scan(img):
	#untill the end scan for the desired color on a thresholded image
	


#for green ball
def green(img):
	#convert the input hsv image to pass through a green mask and threshold the result
	low=np.array([50,100,100])
	up=np.array([70,255,255])
	#not sure of the hsv values.. still working on it
	if scan(img):
		return True
	else:
		return False
	


#for the other ball
def magenta(img):
	#convert the input hsv image to pass through a green mask and threshold the result
	hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
	low=np.array([140,100,100])
	up=np.array([160,255,255])
	#not sure of the hsv values.. still working on it
	mask=cv2.inRange(hsv,l,u)
	res=cv2.bitwise_and(img,img,mask=mask)
	if scan(res):
		return True
	else:
		return False

	
#rasPi sends color
def sendColor(img):#color==1 for green and color==2 for magenta
	#pin one alone high => green ball
	#pin two alone high => magenta ball
	#no pins high => no balls
	if green(img):
		print("Green")
		gpio.output(38,1)
		gpio.output(40,0)
	elif magenta(img):
		print("Magenta")
		gpio.output(38,0)
		gpio.output(40,1)

#where everything happens
def main():
	cap=cv2.VideoCapture(0)
	while(1):
		ret,frame=cap.read()
		sendColor(frame)


main()		
