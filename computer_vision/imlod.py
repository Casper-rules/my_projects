import numpy as np
import cv2
import matplotlib.pyplot as plt
img=cv2.imread('image.jpg')
cv2.line(img,(0,0),(100,100),[255,0,255],5)
pts=np.array([[102,120],[210,120],[43,34],[1,190],[200,200],[450,240]],int)
cv2.polylines(img,[pts],True,[0,255,0],5)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
#plt.imshow(img)
#plt.show()

