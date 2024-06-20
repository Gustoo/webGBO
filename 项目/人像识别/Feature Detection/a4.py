import numpy as np
import cv2

img1 = cv2.imread("112.jpeg", 0)  # 导入灰度图像
img2 = cv2.imread("112.jpeg", 0)
img2 = img2[:300,100:500]

def drawMatches(img1, kp1, img2, kp2, matches):
    rows1 = img1.shape[0]
    cols1 = img1.shape[1]
    rows2 = img2.shape[0]
    cols2 = img2.shape[1]

    out = np.zeros((max([rows1, rows2]), cols1 + cols2, 3), dtype='uint8')
    # 拼接图像
    out[:rows1, :cols1] = np.dstack([img1, img1, img1])
    out[:rows2, cols1:] = np.dstack([img2, img2, img2])

    for mat in matches:
        img1_idx = mat.queryIdx
        img2_idx = mat.trainIdx

        (x1, y1) = kp1[img1_idx].pt
        (x2, y2) = kp2[img2_idx].pt
        # 绘制匹配点
        cv2.circle(out, (int(x1), int(y1)), 4, (255, 255, 0), 1)
        cv2.circle(out, (int(x2) + cols1, int(y2)), 4, (0, 255, 255), 1)

        cv2.line(out, (int(x1), int(y1)), (int(x2) + cols1, int(y2)), (255, 0, 0), 1)

    return out


detector = cv2.ORB_create()

kp1 = detector.detect(img1, None)
kp2 = detector.detect(img2, None)
kp1, des1 = detector.compute(img1, kp1)
kp2, des2 = detector.compute(img2, kp2)

bf = cv2.BFMatcher(cv2.NORM_HAMMING)
matches = bf.match(des1, des2)
img3 = drawMatches(img1, kp1, img2, kp2, matches[:50])
#img3 = cv2.drawKeypoints(img1,kp1,None,color = (0,255,0),flags = 0)

cv2.imwrite("orbTest.jpg", img3)
cv2.imshow('orbTest', img3)
cv2.waitKey(0)