import cv2
import numpy as np
image = cv2.imread('test1.png')

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# cv2.imwrite('gray.jpg', gray)

_,thressed1 = cv2.threshold(gray,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
# cv2.imshow("thresh",thresh)
cv2.imwrite('thressed1.jpg', thressed1)
