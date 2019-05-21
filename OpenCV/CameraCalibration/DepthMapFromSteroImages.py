import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

imgL = cv.imread('/Users/macboiiii/Documents/LearnProjects/OpenCV/PicVid/l.jpeg',0)
imgR = cv.imread('/Users/macboiiii/Documents/LearnProjects/OpenCV/PicVid/r.jpeg',0)
stereo = cv.StereoBM_create(numDisparities=16, blockSize=15)
disparity = stereo.compute(imgL,imgR)
plt.imshow(disparity,'gray')
plt.show()
