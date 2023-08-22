import cv2
import numpy as np

img = cv2.imread('resources/img1.jpg')
print(img.shape)

resizedImg = cv2.resize(img, (1000, 500)) # width, height
print(resizedImg.shape)

croppedImg = img[:300, 200:]

cv2.imshow('image', img)
cv2.imshow('resized Img', resizedImg)
cv2.imshow('cropped Img', croppedImg)

cv2.waitKey(0)
