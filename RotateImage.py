import cv2

img = cv2.imread("Resources/Island.png")
height, width = img.shape[0:2]
print(height,width)
rotationMatrix = cv2.getRotationMatrix2D((width/2, height/2), 90, .5)
rotatedImage = cv2.warpAffine(img, rotationMatrix, (width, height))
cv2.imshow('Rotated Image', rotatedImage)
cv2.waitKey(0)
width=img.shape[0]


#Cropping the image
startRow = int(height*.10)
print(startRow)
startCol = int(width*.70)
print(startCol)
endRow = int(height*.55)
endCol = int(width*.95)
print(endRow)
print(endCol)

croppedImage = img[startRow:endRow, startCol:endCol]
cv2.imshow('Original Image', img)
cv2.imshow('Cropped Image', croppedImage)
cv2.waitKey(0)