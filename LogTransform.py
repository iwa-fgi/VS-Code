import cv2
import numpy as np
img=cv2.imread("Resources/DarkRoad.jfif")
c=255/np.log(1+np.max(img))
l_img=c*np.log(img+1)
l_img=np.array(l_img,dtype=np.uint8)
cv2.imshow("Image",img)
cv2.imshow("LogImage",l_img)
cv2.waitKey(0)