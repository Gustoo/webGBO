import cv2
import numpy as np
import os
path = "imgs"
imgss=[]
objname=[]
imglist= os.listdir(path)
orb =cv2.ORB_create(1000)
#print(imglist)
for aaa in imglist:
    imgc = cv2.imread(f'{path}/{aaa}',0)
    imgss.append(imgc)
    objname.append(os.path.splitext(aaa)[0])
    #print(objname)

def F(imgss):
    Flist = []
    for img in imgss:
        kp,des = orb.detectAndCompute(img,None)
        Flist.append(des)
    return Flist

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
        if max(mlist) > 10:
            FV = mlist.index(max(mlist))
    return FV




Flist = F(imgss)
#print(len(Flist))
cap = cv2.VideoCapture(1)
while True:
    s,img2 = cap.read()
    imgcolor = img2.copy()
    img2 = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
    a = FF(img2,Flist)
    if a!= -1:
        cv2.putText(imgcolor,objname[a],(50,50),cv2.FONT_HERSHEY_COMPLEX_SMALL,2,(0,0,255),2)
    cv2.imshow("aaaa",imgcolor)
    cv2.waitKey(1)


"""
 keypoint 是一个包含若干点的列表
 descriptor 对应每个点的描述符 是一个列表， 每一项都是检测到的特征的局部图像
 
 检测的结果是关键点
 计算的结果是描述符
 
 可以根据监测点的描述符 来比较检测点的相似之处
 
 """