import cv2
import numpy as np

frameWidth = 640
frameHeight = 480

cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10, 100)

myColors = [[156, 188, 0, 179, 255, 255], 
            [70, 110, 0, 99, 255, 255],
            [10, 32, 141, 29, 183, 255]]

myColorValues = [[0, 0, 255], 
                 [0, 255, 0],
                 [8, 220, 220]]  # BGR

myPoints = []  # [x, y, colorId]

def getContours(img):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE) # cv2.RETR_EXTERNAL: retrieves only the extreme outer contours
    x, y, w, h = 0, 0, 0, 0
    for cnt in contours:
        area = cv2.contourArea(cnt)
        # print(area)
        if area > 500:
            # cv2.drawContours(imgResult, cnt, -1, (255, 0, 0), 3)
            peri = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.02*peri, True) 
            x, y, w, h = cv2.boundingRect(approx)
    return x+w//2, y

def findColor(img, myColors, myColorValues):
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    count = 0
    newPoints = []
    for color in myColors:
        lower = np.array(color[:3])
        upper = np.array(color[3:])
        mask = cv2.inRange(imgHSV, lower, upper)
        x, y = getContours(mask)
        cv2.circle(imgResult, (x, y), 10, myColorValues[count], cv2.FILLED)
        if x != 0 and y != 0:
            newPoints.append([x, y, count])
        count += 1
    return newPoints

def drawOnCanvas(myPoints, myColorValues):
    for point in myPoints:
        cv2.circle(imgResult, (point[0], point[1]), 10, myColorValues[point[2]], cv2.FILLED)
        
while True:
    success, img = cap.read()
    imgResult = img.copy()
    newPoints = findColor(img, myColors, myColorValues)
    if len(newPoints) != 0:
            myPoints += newPoints
    if len(myPoints) != 0:
        drawOnCanvas(myPoints, myColorValues)
    cv2.imshow('Result', imgResult)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break