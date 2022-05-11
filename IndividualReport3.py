import cv2
import numpy as np
path="Resources/Book.jpg"
img=cv2.imread(path)
width,height=350,450
img=cv2.resize(img,(640,480))
pts1=np.float32([(53,325),(158,95),(553,415),(596,170)])
pts2=np.float32([[0,0],[width,0],[0,height],[width,height]])
matrix=cv2.getPerspectiveTransform(pts1,pts2)
img_output=cv2.warpPerspective(img,matrix,(width,height))
cv2.imshow('Output',img_output)
cv2.imshow('OG image',img)
x=cv2.waitKey(0)
if x==ord('q'):
    cv2.destroyAllWindows()
    