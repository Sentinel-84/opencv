import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img=cv.imread('hazard10.jpg')
cv.imshow('IMAGE',img)

#img_RGB=cv.cvtColor(img,cv.COLOR_BGR2RGB)
#plt.axis('off')
#plt.imshow(img_RGB)
#plt.show()

#ball=img[235:295,465:530]
#ball=([255,255,255])
#img[235:295,465:530]=ball

ball=img[235:295,465:530]
img[235:295,555:620]=ball

cv.imshow('IMAGE WITH TWO BALLS',img)

cv.waitKey(0)
cv.destroyAllWindows()
