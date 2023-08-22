import cv2
import numpy as np

img = cv2.imread('resources/img2.jpg')

w, h = 250, 350
pts1 = np.float32([[229, 399], [182, 271], [462, 312], [414, 184]])
pts2 = np.float32([[0, 0], [w, 0], [0, h], [w, h]])
matrix = cv2.getPerspectiveTransform(pts1, pts2) 
outputImg = cv2.warpPerspective(img, matrix, (w, h))

cv2.imshow('image', img)
cv2.imshow('output image', outputImg)

cv2.waitKey(0)

