import numpy as np
import cv2
import matplotlib.pyplot as plt


img = (cv2.imread(r"res.png",-1)==0).astype(np.uint8)

mask=cv2.morphologyEx(img,cv2.MORPH_CLOSE,np.ones((20,40))) #this will connect letters together
out = cv2.connectedComponentsWithStats(mask, 4, cv2.CV_32S) #count pixel in each blob
bad = out[2][:,cv2.CC_STAT_AREA]<2000 #remove small blobs
mask = np.zeros_like(img,dtype=np.uint8)
for i in range(1,out[0]):
    if not bad[i]:
        mask[out[1] == i] = 1
img_clean = img & mask
# plt.imshow(1-img_clean,interpolation="none",cmap='gray')
plt.imsave('spot_remover.png',1-img_clean,cmap='gray')
# cv2.imwrite('spot_remover.png', res)