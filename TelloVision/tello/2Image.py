from djitellopy import tello
import cv2

fly = tello.Tello()
fly.connect()
print(fly.get_battery())
fly.streamon()

while True:
    img = fly.get_frame_read().frame
    img = cv2.resize(img, (360, 240))
    img = cv2.cvtColor(img,cv2.COLOR_BGRA2RGB)
    cv2.imshow("Image", img)
    cv2.waitKey(1)