import cv2 as cv

img=cv.imread('hazard10.jpg',0)#putting 0 will grayscale the image
cv.imshow('hazard',img)
cv.waitKey(0)#0 represents infinite time of waitage till a key is pressed
cv.destroyAllWindows()

