## Feature detection using FAST
## This incorporates machine learning for corner detection.
## FAST (Features from Accelerated Segment Test) algorithm
## was proposed by Edward Rosten and Tom Drummond in their
## paper “Machine learning for high-speed corner detection”
## in 2006 (Later revised it in 2010). ##


## Feature detection using FAST
## Select a pixel (p) in the image which is to be identified as an interest point
## Select an appropriate threshold value (t)
## a set of pixels in a circle around (p) are checked if the threshold is higher or lower

## A high speed test was proposed to use 1, 9, 5, 13
## which is top, bottom, right, left
## If (p) is a corner, then 3 of these must be brighter or darker than (p)

import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('simple.jpg',0)

# Initiate FAST object with default values
fast = cv2.FastFeatureDetector_create()

# find and draw the keypoints
kp = fast.detect(img,None)
img2 = cv2.drawKeypoints(img, kp, (255,0,0))

# Print all default params
print ("Threshold: ", fast.getThreshold())
print ("nonmaxSuppression: ", fast.getNonmaxSuppression())
print ("neighborhood: ", fast.getType())
print ("Total Keypoints with nonmaxSuppression: ", len(kp))

cv2.imwrite('fast_true.png',img2)

# Disable nonmaxSuppression
fast.setNonmaxSuppression(False)
kp = fast.detect(img,None)

print ("Total Keypoints without nonmaxSuppression: ", len(kp))

img3 = cv2.drawKeypoints(img, kp, (255,0,0))

cv2.imwrite('fast_false.png',img3)

