import cv2
img=cv2.imread('Resources/XRay.jfif')
img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
n_img=255-img
cv2.imshow("Original img",img)
cv2.imshow("Inverted img",n_img)
cv2.waitKey(0)
