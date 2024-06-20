import  cv2
import os
import numpy as np
flist = os.listdir("imgs")
#print(flist)
imgs =[]
imgname =[]
orb = cv2.ORB_create(2000)
for i in flist:
    imgc = cv2.imread(f'{"imgs"}/{i}',0)
    imgs.append(imgc)
    imgname.append(os.path.splitext(i)[0])
    print(imgname)

def f(imgs):
    fflist = []
    for i in imgs:
        kp,de = orb.detectAndCompute(i,None)
        fflist.append(de)
        print(fflist)
    return fflist

def FF(img,Flist):
    kp2, des2 = orb.detectAndCompute(img, None)
    bf = cv2.BFMatcher()
    mlist = []
    FV = -1
    try:
        for des in Flist:
            mat = bf.knnMatch(des,des2,k=2)
            good = []
            for x,y in mat:
                if x.distance < 0.75*y.distance:
                    good.append([x])
            mlist.append(len(good))
    except:
        pass
    #print(len(good))
    if len(mlist) !=0:
        if max(mlist) > 13:
            FV = mlist.index(max(mlist))
    return FV


Flist = f(imgs)
#print(len(Flist))
cap = cv2.VideoCapture(1)
while True:
    s,img2 = cap.read()
    imgcolor = img2.copy()
    img2 = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
    a = FF(img2,Flist)
    if a!= -1:
        cv2.putText(imgcolor,imgname[a],(50,50),cv2.FONT_HERSHEY_COMPLEX_SMALL,2,(0,0,255),2)
    cv2.imshow("aaaa",imgcolor)
    cv2.waitKey(1)