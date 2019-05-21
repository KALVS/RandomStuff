import numpy as np
import cv2 as cv
img = cv.imread('/Users/macboiiii/Documents/LearnProjects/OpenCV/PicVid/orange_inpain.jpeg')
mask = cv.imread('/Users/macboiiii/Documents/LearnProjects/OpenCV/PicVid/mask.jpeg',0)
dst = cv.inpaint(img,mask,3,cv.INPAINT_NS)
cv.imshow('dst',dst)
cv.imshow('img',img)
cv.imshow('mask', mask)
cv.waitKey(0)
cv.destroyAllWindows()
