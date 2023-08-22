import cv2
import numpy as np

img = np.zeros((512, 256, 3))
print(img.shape)
#img[:] = 255, 0 ,0 # BRG

cv2.line(img, (0,0), (img.shape[1], img.shape[0]), (0, 255, 0))  # starting point, ending point, color
cv2.rectangle(img, (0,0), (100, 300), (0, 0, 255), cv2.FILLED)
cv2.circle(img, (100, 256), 40, (255, 255, 0), 4)
cv2.putText(img,'learn openCV',(50, 400), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0,  100, 100), 1)

cv2.imshow('img',img)

cv2.waitKey(0)