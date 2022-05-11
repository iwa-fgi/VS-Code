import cv2 as cv
import matplotlib as plt
img = cv.imread('Resources/Island.png')
color = ('b','g','r')
for i,col in enumerate(color):
    histr = cv.calcHist([img],[i],None,[256],[0,256])
    plt.pyplot.plot(histr,color = col)
    plt.pyplot.xlim([0,256])
plt.show()