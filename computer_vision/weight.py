import numpy as np
import cv2


def all_zero(img,n):
	for i in range(n+1,640):
		if img[250,i] == 100:
			return False
	return True



def upper(img):
	i=0
	while bottle_present(img):
		print 'finding Upper'
		while i<500:
			pxi=img[250,i]
			if pxi==100:
				print 'pxi = ',i
				return i
			i+=1


def lower(img):
	x=upper(img)+1
	c=0
	while bottle_present(img):
		
		while x<500:
			c+=1
			print 'finding lower',c
			pxf=img[250,x]
			if pxf==100 and all_zero(img,x):
				print 'pxf = ',x
				return x
			x+=1
		



def bottle_present(img):
	
	for i in range(400):
		if img[250,i]==100:
			return True
	return False




def process(cap):
	l=[]
	c=0
	while True:
		_,frame=cap.read()
		#img=frame[0:500,0:500]
		hsv=cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
		low=np.array([150,150,0])
		up=np.array([255,255,180])
		low1=np.array([100,50,100])
		up1=np.array([130,255,130])
		mask1=cv2.inRange(hsv,low1,up1)
		mask=cv2.inRange(hsv,low,up)
		fin=cv2.bitwise_and(frame,frame,mask=mask1)
		final=cv2.bitwise_and(frame,frame,mask=mask)
		f_gray=cv2.cvtColor(final,cv2.COLOR_BGR2GRAY)
		fin_gray=cv2.cvtColor(fin,cv2.COLOR_BGR2GRAY)
		_,th1=cv2.threshold(fin_gray,0,100,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
		#cv2.imshow('hsv',th1)
		#if cv2.waitKey(1)&0xFF==ord('a'):
		#	return
		ret,th=cv2.threshold(f_gray,0,100,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
		if bottle_present(th):
			print 'got it'
			c+=1
			print c
			i1=lower(th)
			i2=upper(th)
			h=i1-i2
			return h
			#i=400
			#while i>0:
			#	if th[i,250]==100:
			#		pxi = i;
			#		break
			#	i-=1
			#for j in range(pxi,400):
			#	if all_zero(th,j):
			#		pxf=j
			#		break
			#else:
			#	continue
			#h=pxf-pxi
			#return h
	
	
c = cv2.VideoCapture(0)
h = process(c)
print h


# the hight and weight must essentially have a linear relation and hence find the equation and put value in the equatio...

#eg.

#wt=const_1*h+const_2



#re-execute the code to find the hight of the bottle 
#by the rules of similar triangles, let h1=hight of original bottle(known); h2=hight of bottle in image(calculated); x1=hight of water in actual; x2=hight of water in image
#then;  by similar triangles;
#h2=(x2/x1)*h1




#Time complexity doubles, space needed increased hence this method is worth discarding.
