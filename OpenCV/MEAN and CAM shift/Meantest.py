import numpy as np
import cv2
cap = cv2.VideoCapture('slow.flv')

## Cap.Read reads the next image in the video
ret, frame = cap.read()
rows, cols = frame.shape[:2]

windowWidth = int(cap.get(3))  # float
windowHeight = int(cap.get(4)) # float
windowCol = int((cols - windowWidth) / 2)
windowRow = int((rows - windowHeight) / 2)
track_window = (windowCol,windowRow,windowWidth,windowHeight)
print('height',windowHeight,'Width', windowWidth)

# Setting up the Region on Interest
roi = frame[windowRow:windowRow + windowHeight, windowCol:windowCol + windowWidth]
roiHSV = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)


# Masking the dark areas
# Black
lowLimit = np.array((0., 0., 0.))
highLimit = np.array((255., 255., 255))
mask = cv2.inRange(roiHSV, lowLimit, highLimit)

# Calculate the hue histoghram of the unmasked region
roiHist = cv2. calcHist([roiHSV], [0], mask, [180], [0, 180])
cv2.normalize(roiHist, roiHist, 0, 255, cv2.NORM_MINMAX)


# Sets the termination criteria: with ten iterations or moved less than 1 pixel
terminationCriteria = (cv2.TERM_CRITERIA_COUNT | cv2.TERM_CRITERIA_EPS, 10, 1)

# main loop
