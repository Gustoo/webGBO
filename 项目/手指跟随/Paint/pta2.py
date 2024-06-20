import cv2
import numpy as np
import os
import HandTrackingModule as htm
import ocvex1
brushThickness = 25
eraserThickness = 100


folderPath = "pic"
mylist = os.listdir(folderPath)
overlaylist = []
for imPath in mylist:
    image = cv2.imread(f"{folderPath}/{imPath}")
    overlaylist.append(image)
    #print(len(overlayList))
header = overlaylist[0]
drawColor = (0, 0, 0)
cap = cv2.VideoCapture(1)
cap.set(3, 1280)
cap.set(4, 720)
detector = htm.handDetector(detectionCon=0.65,maxHands=1)
xp, yp = 0, 0
imgCanvas = np.zeros((720, 1280, 3), np.uint8)

while True:
    s, img = cap.read()
    img = cv2.flip(img, 1)
    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw=False)

    if len(lmList) != 0:
        x1, y1 = lmList[8][1:]
        x2, y2 = lmList[12][1:]
        fingers = detector.fingersUp()

        if fingers[1] and fingers[2]:
            if y1 < 150:
                if 400 < x1 < 600:
                    header = overlaylist[1]
                    drawColor = (0, 0, 255)
                elif 630 < x1 < 800:
                    header = overlaylist[2]
                    drawColor = (0, 255, 0)
                elif 830 < x1 < 1000:
                    header = overlaylist[3]
                    drawColor = (255, 0, 0)
                elif 1100 < x1 < 1200:
                    header = overlaylist[0]
                    drawColor = (0, 0, 0)
            cv2.rectangle(img, (x1, y1-25), (x2, y2 + 25), drawColor, cv2.FILLED)

        if fingers[1] and fingers[2] == False:
            cv2.circle(img, (x1, y1), 15, drawColor, cv2.FILLED)
            print("draw mode")
            if xp == 0 and yp == 0:
                xp, yp = x1, y1

            cv2.line(img, (xp, yp), (x1, y1), drawColor, brushThickness)
            xp, yp = x1, y1
            if drawColor == (0, 0, 0):
                cv2.line(img, (xp, yp), (x1, y1), drawColor, eraserThickness)
                cv2.line(imgCanvas, (xp, yp), (x1, y1), drawColor, eraserThickness)

            else:
                cv2.line(img, (xp, yp), (x1, y1), drawColor, brushThickness)
                cv2.line(imgCanvas, (xp, yp), (x1, y1), drawColor, brushThickness)


        if all (x >= 1 for x in fingers):
            imgCanvas = np.zeros((720, 1280, 3), np.uint8)

    imgGray = cv2.cvtColor(imgCanvas, cv2.COLOR_BGR2GRAY)
    _, imgInv = cv2.threshold(imgGray, 50, 255, cv2.THRESH_BINARY_INV)
    imgInv = cv2.cvtColor(imgInv,cv2.COLOR_GRAY2BGR)
    img = cv2.bitwise_and(img,imgInv)
    img = cv2.bitwise_or(img,imgCanvas)

    # Setting the header image
    img[0:150, 0:1280] = header
    #img = cv2.addWeighted(img,0.5,imgCanvas,0.5,0)
    cv2.imshow("Image", img)
    #cv2.imshow("Canvas", imgCanvas)
    #cv2.imshow("Inv", imgInv)
    cv2.waitKey(1)