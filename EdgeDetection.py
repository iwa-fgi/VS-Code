import cv2
image = cv2.imread('Resources/Panda.jpg',0)
image=cv2.resize(image,(640,480))
cv2.imshow("Original", image)
canny = cv2.Canny(image, 35, 170)
cv2.imshow("Canny", canny)
cv2.waitKey(0)