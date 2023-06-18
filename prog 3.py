import cv2 as cv
import numpy as np

img=np.zeros((500,500,3),np.uint8)

cv.line(img,(20,20),(500,500),(255,0,255),12)

cv.rectangle(img,(20,20),(480,400),(255,255,0),7)

cv.circle(img,(250,250),50,(255,0,255),12)

font=cv.FONT_HERSHEY_SIMPLEX
cv.putText(img,'Nishanth',(220,250),font,2,(255,0,0),7)

cv.imshow('Image',img)
cv.waitKey(0)
cv.destroyAllWindows()

