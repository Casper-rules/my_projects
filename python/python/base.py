import cv2
import numpy as np
from time import *
import RPi.GPIO as gpio

#setting up pi output
gpio.setmode(gpio.BOARD)

#setting up pins for leds to indicate the weight
gpio.setup(40,gpio.OUT)#led to glow when weight is more than 500 but less than 1000
gpio.setup(38,gpio.OUT)#this glows while weight is less than 500
gpio.setup(36,gpio.OUT)#glows when weight is more than 1000


#setting up pins for motordriver

#Extra pins defined if we switch back to 4 wheel drive
#direction pins for motor drivers
gpio.setup(3,gpio.OUT)#m1
gpio.setup(5,gpio.OUT)#m2
#gpio.setup(11,gpio.OUT)
#gpio.setup(13,gpio.OUT)

#pins to control speed of motor
gpio.setup(8,gpio.OUT)#m1
gpio.setup(10,gpio.OUT)#m2
#gpio.setup(12,gpio.OUT)
#gpio.setup(16,gpio.OUT)


#m1=left motor
#m2=right motor


#motor speed pin setting up to give pwm output
m1=gpio.PWM(8,100)#pin number, duty cycle
m2=gpio.PWM(10,100)
#m3=gpio.PWM(12,100)
#m4=gpio.PWM(16,100)


#calculate weight first then follow line

#calculation of wieght
def weight(cap1):
	
		_,img=cap1.read()#read the camera feed	                         #
		blur = cv2.GaussianBlur(img, (15, 15), 0)#remove the noise
		hsv=cv2.cvtColor(blur,cv2.COLOR_BGR2HSV)#apply hue saturation value
		lower_blue=np.array([110,50,50])#lower value of hue for cap
		upper_blue=np.array([130,255,255])#upper value of hue for cap

	
		lower_red=np.array([0,100,100])#lower value of hue for water
		upper_red=np.array([10,255,255])#upper value of hue for water


	#applying masks on the images for proper detection of water and bottle
		mask1=cv2.inRange(hsv,lower_red,upper_red)
		mask2=cv2.inRange(hsv,lower_blue,upper_blue)


	#detecting water
		res1=cv2.bitwise_and(img,img,mask=mask1)

	#detecting bottle									
		res2=cv2.bitwise_and(img,img,mask=mask2)


	#convert images to grascale fro simplified processing		
		gray_water=cv2.cvtColor(res1,cv2.COLOR_BGR2GRAY)
		gray_cap=cv2.cvtColor(res2,cv2.COLOR_BGR2GRAY)
		
		
	#Apply threshold for easier calculation and processing of the images
		ret,otsu_water=cv2.threshold(gray_water,60,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
		ret,otsu_cap=cv2.threshold(gray_cap,60,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)


	#find contours with maximum areas in theb image
		___,contours1 = cv2.findContours(gray_water,cv2.RETR_LIST,cv2.CHAIN_APPROX_NONE)
		___,contours2 = cv2.findContours(gray_cap,cv2.RETR_LIST,cv2.CHAIN_APPROX_NONE)	
		c1 = max(contours1, key = cv2.contourArea)
		c2 = max(contours2, key = cv2.contourArea)
	
		
	#Find the bounding region in the image for water and bottle
		x1,y1,w1,h1 = cv2.boundingRect(c1)
		x2,y2,w2,h2 = cv2.boundingRect(c2)
	
	
	
	#marking the countours
		waterr = cv2.rectangle(otsu_water,(x1,y1),(x1+w1,y1+h1),(0,255,0),2)
		capr = cv2.rectangle(otsu_cap,(x2,y2),(x2+w2,y2+h2),(0,255,0),2)
	
	
	
	#taking only the region of image having the water and the bottle(Cap)
		water=waterr[y1:y1+h1,x1:x1+w1]
		cap=capr[ y2:y2+h2,x2:x2+w2]
	
	
		bottle_height=(y1+h1)-y2   #height of bottle in pixels
	
		water_height=h1            #height of water in pixels
		
	
	
	
		actual_water_height=(25.5*water_height)/(bottle_height)
		weight=actual_water_height*32
		return weight


cap1=cv2.VideoCapture(0)
wt=0

try :
	while wt<500:
		wt+=weight(cap1)
		#glow an led
		gpio.output(40,0)
		gpio.output(38,1)
		gpio.output(36,0)
		sleep(t1) #a t1 sec time gap to pick the next bottle

	if 500<wt<1000:
		gpio.output(40,1)
		gpio.output(38,0)
		gpio.output(36,0)
	
	elif wt>1000:
		gpio.output(40,0)
		gpio.output(38,0)
		gpio.output(36,1)
	
	else:
		gpio.output(40,0)
		gpio.output(38,0)
		gpio.output(36,0)
	
except KeyboardInterrupt :	
	cap1.release()
	gpio.cleanup()
#sleep for t seconds


sleep(t)


#turn the camera for line following
# after 't' seconds start to follow the line


#follow the line
cap=cv2.VideoCapture(1)
while True:
	ret,frame=cap.read()
	roi=frame
	#cv2.imshow('frames',frame)
	gray=cv2.cvtColor(roi,cv2.COLOR_BGR2GRAY)
	#lines meet at centre of the screen
	#Thresholding the feed
	ret,otsu=cv2.threshold(gray,0,100,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
	contours,_=cv2.findContours(otsu.copy(),1,cv2.CHAIN_APPROX_NONE)
	if len(contours)>0:#if find the line
		#taking maximum region contour
		c=max(contours,key=cv2.contourArea)
		M=cv2.moments(c)
		#center coordinates
		cx=int(M['m10']/M['m00'])
		#draw contours
		cv2.drawContours(frame,contours,-1,(0,255,0),3)#just for effect in color frame
		# cx must lie between a,b; where a<b and b-a>20. Value of a and b depends completely on first practice we do with camera properly mounted, rest the cam will align on itself
		
		if cx>b:
			
			#To right
			
			#left motor rotates clockwise at higher speed
			m1.changeDutyCycle(100)
			gpio.output(3,1)
			
			#right motor rotates clockwise at a very low speed
			m2.changeDutyCycle(10)
			gpio.output(5,1)
		
		elif cx<a:
			#To left
			
			#right motor rotates clockwise at a low speed
						#left motor rotates clockwise at higher speed
			m1.changeDutyCycle(10)
			gpio.output(3,1)
			
			#right motor rotates clockwise at a very low speed
			m2.changeDutyCycle(100)
			gpio.output(5,1)
			
		elif a<cx<b:
			#Keep Moving Straight
			#both wheels move at same speed in same direction
			m1.changeDutyCycle(100)
			gpio.output(3,1)
			
			m2.changeDutyCycle(100)
			gpio.output(5,1)

cap.release()
gpio.cleanup()
