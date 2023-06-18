import cv2 as cv
import numpy as np

img=np.zeros((500,500,3),np.uint8)

cv.circle(img,(250,250),150,(255,0,255),8)

cv.circle(img,(290,210),20,(255,0,255),8)
cv.circle(img,(290,290),20,(255,0,255),8)
cv.imshow('Image',img)
cv.waitKey(0)
cv.destroyAllWindows()



