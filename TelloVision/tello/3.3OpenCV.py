#分割 合并
import cv2
import numpy as np
#cv2.split()和cv2.merge()
img = cv2.imread("123.png",1)
img = cv2.resize(img,(590,860))
cv2.imshow("aaa", img)
b,g,r = cv2.split(img)
#img2 = cv2.merge((g,r,b))
#cv2.imshow("aaaa", img2)
#print(b)

img3 = img.copy()
b2 = img3[:, :, 0]
#img3 = cv2.merge((b2,b2,b2))
g2 = img3[:, :,  1]
r2 = img3[:, :,  2]
#灰度算法
gray = r2*0.299+g2*0.587+b2*0.114
print(gray.dtype)
out = gray.astype(np.uint8)
img3 = cv2.merge((b,b,b))
img4 = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("aaaaa", img3)
cv2.waitKey(0)
cv2.destroyAllWindows()




'''
import cv2
import numpy as np
img = cv2.imread("112.jpeg",0)
print(img<120)
img[img<120] =0
img[img>120] =255
cv2.imshow("aaa",img)
cv2.waitKey(0)
'''