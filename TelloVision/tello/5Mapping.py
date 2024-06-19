from djitellopy import tello
import numpy as np
import time
import cv2
import math
import pygame

fspeed = 120 / 10  #cm/s
aspeed = 360 / 10  #d/s
delay = 0.25
fd = fspeed * delay
ad = aspeed * delay

x, y = 500, 500
aa = 0
yaw = 0

pygame.init()
screen = pygame.display.set_mode((360, 240))

fly = tello.Tello()
fly.connect()
print(fly.get_battery())

points = [(0, 0), (0, 0)]


def getkey():
    global x,y,yaw,aa,dd
    a, b, c, d = 0, 0, 0, 0
    speed = 15
    aspeed = 50
    dd = 0
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT]:
        a = -speed
        dd = fd
        aa = 180
    elif key[pygame.K_RIGHT]:
        a = speed
        dd = fd
        aa = 0
    if key[pygame.K_UP]:
        b = speed
        dd = fd
        aa = 270
    elif key[pygame.K_DOWN]:
        b = -speed
        dd = fd
        aa = 90
    if key[pygame.K_w]:
        c = speed
    elif key[pygame.K_s]:
        c = -speed
    if key[pygame.K_a]:
        d = -speed
        yaw -= ad
    elif key[pygame.K_d]:
        d = speed
        yaw += ad
    if key[pygame.K_q]:
        fly.land()
        time.sleep(1)
    elif key[pygame.K_e]:
        fly.takeoff()
    time.sleep(delay)
    aa += yaw
    x += int(dd * math.cos(math.radians(aa)))
    y += int(dd * math.sin(math.radians(aa)))
    return [a,b,c,d,x,y]


def drawPoints(img, points):
    for point in points:
        cv2.circle(img, point, 5, (0, 0, 255), cv2.FILLED)

    cv2.circle(img, points[-1], 8, (0, 255, 0), cv2.FILLED)
    cv2.putText(img, f'({(points[-1][0] - 500) / 100},{(points[-1][1] - 500) / 100})m',
                (points[-1][0] + 10, points[-1][1] + 30), cv2.FONT_HERSHEY_PLAIN, 1,
                (255, 0, 255), 1)

while True:
    vals = getkey()
    #fly.send_rc_control(vals[0], vals[1], vals[2], vals[3])
    img = np.zeros((1000, 1000, 3), np.uint8)
    if points[-1][0] != vals[4] or points[-1][1] != vals[5]:
        points.append((vals[4], vals[5]))
    drawPoints(img, points)
    cv2.imshow("Output", img)
    cv2.waitKey(1)