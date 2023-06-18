import cv2 as cv

img=cv.imread('lena.jpg')
img1=cv.imread('hazard10.jpg',0)
cv.imshow('GREY COLOR',img1)
cv.imshow('image',img)
cv.waitKey(0)
cv.destroyAllWindows()
