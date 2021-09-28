import cv2
import numpy as np
from skimage import morphology
import matplotlib.pyplot as plt
import skimage

def noise_removal(image):
    import numpy as np
    kernel = np.ones((1, 1), np.uint8)
    image = cv2.dilate(image, kernel, iterations=100)
    kernel = np.ones((1, 1), np.uint8)
    image = cv2.erode(image, kernel, iterations=100)
    image = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)

    # image = cv2.medianBlur(image, 1)
    return (image)

fname = "data/image0.jpg"
bgray = cv2.imread(fname)[...,0]

blured1 = cv2.medianBlur(bgray,3)
blured2 = cv2.medianBlur(bgray,51)
divided = np.ma.divide(blured1, blured2).data
normed = np.uint8(255*divided/divided.max())
th, threshed = cv2.threshold(normed, 1, 255, cv2.THRESH_OTSU)

threshed = noise_removal(threshed)
threshed = noise_removal(threshed)

threshed = noise_removal(threshed)

threshed = noise_removal(threshed)
threshed = noise_removal(threshed)
threshed = noise_removal(threshed)
threshed = noise_removal(threshed)
threshed = noise_removal(threshed)
threshed = noise_removal(threshed)

image = threshed
thresh = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
opening = 255 - cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=1)


# dst = np.vstack((normed, threshed))
cv2.imwrite("data/dst.png", opening)


# """Another One"""
#
# import cv2
# import numpy as np
#
# img = cv2.imread("test1.png")[:,:,0]  # the last readable image
#
# new_img = []
# for line in img:
#     new_img.append(np.array(list(map(lambda x: 0 if x < 198 else 255, line))))
#
# new_img = np.array(list(map(lambda x: np.array(x), new_img)))
#
# cv2.imwrite("threshold2.png", new_img)