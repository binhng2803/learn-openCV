import cv2
import numpy as np

img = cv2.imread('resources/img1.jpg')
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# imgBlur = cv2.GaussianBlur(imgGray, (7,7), 0)
# imgBlur2 = cv2.GaussianBlur(imgGray, (15,15), 0)
imgCanny = cv2.Canny(img, 150, 200)
imgDialation = cv2.dilate(imgCanny, np.ones((5,5), np.uint8), iterations=1)
# imgDialation2 = cv2.dilate(imgCanny, np.ones((3,3), np.uint8), iterations=1)
# imgDialation3 = cv2.dilate(imgCanny, np.ones((5,5), np.uint8), iterations=5)
imgEroded = cv2.erode(imgDialation, np.ones((5,5), np.uint8), iterations=1)


cv2.imshow('image',img)
cv2.imshow('gray image', imgGray)
# cv2.imshow('gray blur image', imgBlur)
# cv2.imshow('gray blur image 2', imgBlur2)
cv2.imshow('canny image', imgCanny)
cv2.imshow('dilation image', imgDialation)
# cv2.imshow('dilation image 2', imgDialation2)
# cv2.imshow('dilation image 3', imgDialation3)
cv2.imshow('eroded image', imgEroded)

cv2.waitKey(0)

