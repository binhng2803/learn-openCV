import cv2

plateCascade = cv2.CascadeClassifier('resources/haarcascades/haarcascade_russian_plate_number.xml')

width, height = 640, 480
minArea = 200
color = (0, 255, 0)

cap = cv2.VideoCapture(0)
cap.set(3, width)
cap.set(4, height)
cap.set(10, 150)
count = 0

while True:
    success, img = cap.read()
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    numberPlates = plateCascade.detectMultiScale(imgGray, 1.1, 10)
    for (x, y, w, h) in numberPlates:
        area = w*h
        if area > minArea:
            cv2.rectangle(img, (x, y), (x+w, y+h), color, 2)
            cv2.putText(img, 'number plate', (x, y-5),
                        cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, color, 2)
            
            imgRoi = img[y:y+h, x:x+w]
            cv2.imshow('ROI', imgRoi)
    cv2.imshow('output', img)
    
    if cv2.waitKey(1) & 0xFF == ord('s'):
        cv2.imwrite('resources/number-plates/number-plate'+str(count)+'.jpg', imgRoi)
        cv2.rectangle(img, (0, 200), (640, 300), (0, 255, 0), cv2.FILLED)
        cv2.putText(img, 'Scan saved', (150, 265),
                    cv2.FONT_HERSHEY_DUPLEX, 2, (0, 0, 255), 2)
        cv2.imshow('output', img)
        cv2.waitKey(500)
        count += 1
            
