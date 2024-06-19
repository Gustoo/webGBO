import cv2

img = cv2.imread("123.png", 1)
cv2.imshow("aaa", img)
p = img[300,600]
print(p)
img[300:400,600:650]=[0,255,0]
cv2.imshow("aaaa", img)
cv2.waitKey(0)
cv2.destroyAllWindows()