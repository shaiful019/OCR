import cv2
import numpy as np
from skimage import morphology
import matplotlib.pyplot as plt
import skimage

def noise_removal(image):
    kernel = np.ones((1, 1), np.uint8)
    image = cv2.dilate(image, kernel, iterations=100)
    kernel = np.ones((1, 1), np.uint8)
    image = cv2.erode(image, kernel, iterations=100)
    image = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)

    image = cv2.medianBlur(image, 1)
    return (image)

fname = "data/image0.jpg"
bgray = cv2.imread(fname)[...,0]

blured1 = cv2.medianBlur(bgray,3)
blured2 = cv2.medianBlur(bgray,51)
divided = np.ma.divide(blured1, blured2).data
normed = np.uint8(255*divided/divided.max())
th, threshed = cv2.threshold(normed, 0, 255, cv2.THRESH_OTSU)

threshed = noise_removal(threshed)

image = threshed
thresh = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (6,6))
opening = 255 - cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=1)

opening = noise_removal(threshed)

_, blackAndWhite = cv2.threshold(opening, 127, 255, cv2.THRESH_BINARY_INV)

nlabels, labels, stats, centroids = cv2.connectedComponentsWithStats(blackAndWhite, None, None, None, 8, cv2.CV_32S)
sizes = stats[1:, -1] #get CC_STAT_AREA component
img2 = np.zeros((labels.shape), np.uint8)

for i in range(0, nlabels - 1):
    if sizes[i] >= 100:   #filter small dotted regions
        img2[labels == i + 1] = 255

res = cv2.bitwise_not(img2)
mask= cv2.morphologyEx(res,cv2.MORPH_CLOSE,np.ones((20,40))) #this will connect letters together
out = cv2.connectedComponentsWithStats(mask, 4, cv2.CV_32S) #count pixel in each blob
bad = out[2][:,cv2.CC_STAT_AREA]<2000 #remove small blobs
mask = np.zeros_like(res,dtype=np.uint8)
for i in range(1,out[0]):
    if not bad[i]:
        mask[out[1] == i] = 1
img_clean = res & mask
plt.imsave("data/dst.png",1-img_clean,cmap='gray')
# cv2.imwrite("data/dst.png", res)


