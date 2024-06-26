# 大津二值化算法
import cv2
import numpy as np

# 这里直接将数据转换成float32了，方便后续计算
img = cv2.imread("123.png").astype(np.float32)
img = cv2.resize(img,(590,860))

# 灰度化
def bgr2gray(img):
    b = img[:, :, 0].copy()
    g = img[:, :, 1].copy()
    r = img[:, :, 2].copy()

    gray_img = 0.2126 * r + 0.7152 * g + 0.0722 * b
    gray_img = gray_img.astype(np.uint8)

    return gray_img



def otsu(gray_img):
    h = gray_img.shape[0]
    w = gray_img.shape[1]
    threshold_t = 0
    max_g = 0

    # 遍历每一个灰度层
    for t in range(255):
        # 使用numpy直接对数组进行运算
        n0 = gray_img[np.where(gray_img < t)]
        n1 = gray_img[np.where(gray_img >= t)]
        w0 = len(n0) / (h * w)
        w1 = len(n1) / (h * w)
        u0 = np.mean(n0) if len(n0) > 0 else 0.
        u1 = np.mean(n1) if len(n0) > 0 else 0.

        g = w0 * w1 * (u0 - u1) ** 2
        if g > max_g:
            max_g = g
            threshold_t = t
    print('类间方差最大阈值：', threshold_t)
    gray_img[gray_img < threshold_t] = 0
    gray_img[gray_img >= threshold_t] = 255
    return gray_img


gray_img = bgr2gray(img)
otsu_img = otsu(gray_img)
cv2.imshow('gray_img ', gray_img)

cv2.waitKey(0)
cv2.destroyAllWindows()