import numpy as np
import cv2 as cv
import glob
# termination criteria
criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 30, 0.001)
# prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
objp = np.zeros((6*7,3), np.float32)
objp[:,:2] = np.mgrid[0:7,0:6].T.reshape(-1,2)
# Arrays to store object points and image points from all the images.
objpoints = [] # 3d point in real world space
imgpoints = [] # 2d points in image plane.

img = cv.imread('/Users/macboiiii/Documents/LearnProjects/OpenCV/CameraCalibration/left12.jpg')
h,  w = img.shape[:2]

#for fname in images:
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# Find the chess board corners
print("A")
cv.waitKey(1000)
ret, corners = cv.findChessboardCorners(gray, (7,6), None)
# If found, add object points, image points (after refining them)
print("C")
objpoints.append(objp)
corners2 = cv.cornerSubPix(gray,corners, (11,11), (-1,-1), criteria)
imgpoints.append(corners)
print('D')
# Draw and display the corners
cv.drawChessboardCorners(img, (7,6), corners2, ret)
print('E')
ret, mtx, dist, rvecs, tvecs = cv.calibrateCamera(objpoints, imgpoints, gray.shape[::-1], None, None)
img = cv.imread('/Users/macboiiii/Documents/LearnProjects/OpenCV/CameraCalibration/left12.jpg')
h,  w = img.shape[:2]
newcameramtx, roi = cv.getOptimalNewCameraMatrix(mtx, dist, (w,h), 1, (w,h))
# undistort
print('F')
dst = cv.undistort(img, mtx, dist, None, newcameramtx)
# crop the image
x, y, w, h = roi
dst = dst[y:y+h, x:x+w]

print('G')
cv.imshow('img',dst)
cv.imwrite('calibresult.png', dst)
