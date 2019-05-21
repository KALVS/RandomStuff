##  USURF will not get the orientation of the blobs
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('Butterfly.jpg',0)

surf = cv2.xfeatures2d.SURF_create(400)
print ( surf.getHessianThreshold()) # == 400.0


surf.setHessianThreshold(23000)


surf.setUpright(True)
surf.setExtended(True)
kp, des = surf.detectAndCompute(img, None)
print (surf.descriptorSize())
print (des.shape)

print ( surf.getHessianThreshold()) # == 400.0


print (len(kp))

##if its less than 50, we draw on the image
img2 = cv2.drawKeypoints(img,kp,None,(255,0,0),4)

plt.imshow(img2),plt.show()


###Good to use with Matching. This is found in another file.

