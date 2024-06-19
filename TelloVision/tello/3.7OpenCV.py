#滤波(高通、低通、带通、带阻)、模糊、去噪、平滑等。
import cv2
import random
img = cv2.imread('123.png')
img = cv2.resize(img, None, fx=0.4, fy=0.4,
                  interpolation=cv2.INTER_CUBIC)#调整图片大小

for i in range(1000):
    img[random.randint(0,img.shape[0]-1),random.randint(0,img.shape[1]-1)]=[0,0,0]
cv2.imshow('Original', img)
blur_image = cv2.GaussianBlur(img, (5, 5), 3.5)#(5, 5)表示高斯矩阵的长与宽都是5，标准差取0
cv2.imshow('Blurred Image', blur_image)
dst = cv2.medianBlur(img, 5)
cv2.imshow("median_blur_demo", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()