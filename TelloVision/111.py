import cv2
import time
from djitellopy import tello
import numpy as np
w, h = 360, 240
fly = tello.Tello()
fly.connect()
print(fly.get_battery())
cv2.namedWindow("TB")

def eee(n):
    a = 1

cv2.createTrackbar("h max","TB",179,179,eee)
cv2.createTrackbar("h min","TB",0,179,eee)
cv2.createTrackbar("s max","TB",255,255,eee)
cv2.createTrackbar("s min","TB",0,255,eee)
cv2.createTrackbar("v max","TB",255,255,eee)
cv2.createTrackbar("v min","TB",0,255,eee)
#cap = cv2.VideoCapture(1)

while 1:
    #s, img = cap.read()
    #img = cv2.imread("114.jpg")
    #img = cv2.resize(img, (500, 750))
    img = fly.get_frame_read().frame
    img = cv2.resize(img, (w, h))
    imghsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    ha =cv2.getTrackbarPos("h max","TB")
    hi =cv2.getTrackbarPos("h min","TB")
    sa =cv2.getTrackbarPos("s max","TB")
    si =cv2.getTrackbarPos("s min","TB")
    va =cv2.getTrackbarPos("v max","TB")
    vi =cv2.getTrackbarPos("v min","TB")
    low = np.array([hi,si,vi])
    hig = np.array([ha,sa,va])
    print(low)
    mask = cv2.inRange(imghsv,low,hig)
    imgg = cv2.bitwise_and(img,img,mask=mask)
    print(ha,vi)
    imgs = np.hstack((imgg,img))
    cv2.imshow("aaa",imgs)
    cv2.waitKey(1)