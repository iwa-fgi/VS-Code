import cv2
import matplotlib.pyplot as plt
src = cv2.imread("Resources/DarkRoad.jfif")
src1 = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
histr = cv2.calcHist([src],[0],None,[256],[0,256])
dst = cv2.equalizeHist(src1)
cv2.imshow('Source image', cv2.cvtColor(src,cv2.COLOR_BGR2GRAY))
cv2.imshow('Equalized Image', dst)
plt.plot(histr)
plt.show()
cv2.waitKey(0)