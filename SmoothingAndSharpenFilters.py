import cv2
import numpy as np
image = cv2.imread('Resources/Panda.jpg')
# Print error message if image is null
if image is None:
    print('Could not read image')
image=cv2.resize(image,(640,480))
# Apply identity kernel
kernel1 = np.array( [ [0, -1, 0],
                      [-1, 5, -1],
                      [0, -1, 0] ]  )
sharpen = cv2.filter2D(src=image, ddepth=-1, kernel=kernel1)
cv2.imshow('Original', image)
cv2.imshow('Sharpen', sharpen)
cv2.waitKey()
cv2.imwrite('identity.jpg', sharpen)
cv2.destroyAllWindows()
# Apply blurring kernel
kernel2 = np.ones((5, 5), np.float32) / 25
img = cv2.filter2D(src=image, ddepth=-1, kernel=kernel2)
cv2.imshow('Original', image)
cv2.imshow('Kernel Blur', img)
cv2.waitKey()
cv2.imwrite('blur_kernel.jpg', img)
cv2.destroyAllWindows()
