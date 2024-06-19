import cv2
import numpy as np
import os
path = "imgs"
orb = cv2.ORB_create(1000)
immlist = os.listdir(path)
print(immlist)
imgname=[]
imgss =[]
for i in immlist:
    imgc = cv2.imread(f'{path}/{i}',0)
    imgss.append(imgc)
    imgname.append(os.path.splitext(i)[0])
#print(imgname)
def f(imgss):
    ylist =[]
    for i in imgss:
        kp,de = orb.detectAndCompute(i, None)
        ylist.append(de)
    return ylist

def ff(img,ylist):
    mzh = -1
    kp2,de2 = orb.detectAndCompute(img, None)
    bf = cv2.BFMatcher(cv2.NORM_HAMMING)
    goodlist =[]
    for i in ylist:
        #mat = bf.Match(i,de2)
        mat = bf.knnMatch(i, de2,k=2)
        good=[]
        for x,y in mat:
                if x.distance < 0.75*y.distance:
                    good.append([x])
        goodlist.append(len(good))

    if len(goodlist) !=0:
        if max(goodlist) >20:
            mzh = goodlist.index(max(goodlist))
    return mzh

Flist = f(imgss)
#print(len(Flist))
cap = cv2.VideoCapture(1)
while True:
    s,img2 = cap.read()
    imgcolor = img2.copy()
    img2 = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
    mzh = ff(img2,Flist)
    if mzh!= -1:
        cv2.putText(imgcolor,imgname[mzh],(50,50),cv2.FONT_HERSHEY_COMPLEX_SMALL,2,(0,0,255),2)
    cv2.imshow("aaaa",imgcolor)
    cv2.waitKey(1)