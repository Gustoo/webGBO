import cv2
import numpy as np
import time
import os


fPath ="pic"
myList = os.listdir(fPath)
print(myList)
overlayList = []
for imPath in myList:
    img = cv2.imread(f"{fPath}/{imPath}")
    overlayList.append(img)

head = overlayList[1]
cap = cv2.VideoCapture(1)
cap.set(3, 1280)
cap.set(4, 720)

while True:
    s, img = cap.read()
    img = cv2.flip(img, 1)
#    img[0:150, 0:1280] = head
    cv2.imshow("aaa", img)
    cv2.waitKey(1)