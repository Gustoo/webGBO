import cv2

img = cv2.imread("123.png",-1)
cv2.imshow("aaa",img)
print(img)
print(img.shape)
print(img.size)
print(img.dtype)

cv2.waitKey(0)
cv2.destroyAllWindows()