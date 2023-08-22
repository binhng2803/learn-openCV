import cv2
print('Hello, OpenCV')


img = cv2.imread('resources/img1.jpg')
cv2.imshow('Output', img)
cv2.waitKey(0)