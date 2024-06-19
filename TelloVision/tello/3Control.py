from djitellopy import tello
from time import sleep
import pygame
import cv2

pygame.init()
screen = pygame.display.set_mode((360, 240))

fly = tello.Tello()
fly.connect()
print(fly.get_battery())
fly.streamon()

def getkey():
    a,b,c,d = 0,0,0,0
    speed = 40
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT]:
        a = -speed
    elif key[pygame.K_RIGHT]:
        a = speed
    if key[pygame.K_UP]:
        b = speed
    elif key[pygame.K_DOWN]:
        b = -speed
    if key[pygame.K_w]:
        c = speed
    elif key[pygame.K_s]:
        c = -speed
    if key[pygame.K_a]:
        d = -speed
    elif key[pygame.K_d]:
        d = speed
    if key[pygame.K_q]:
        fly.land()
        sleep(1)
    if key[pygame.K_e]:
        fly.takeoff()
    return [a,b,c,d]


run = True
while run:
    img = fly.get_frame_read().frame
    img = cv2.resize(img, (360, 240))
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGRA2RGB)
    #screen.blit(img, (0, 0))
    pygame_image = pygame.image.frombuffer(imgRGB.tobytes(), img.shape[:2][::-1], "RGB")
    screen.blit(pygame_image, (0, 0))
    vals = getkey()
    fly.send_rc_control(vals[0], vals[1], vals[2], vals[3])
    sleep(0.05)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()
pygame.quit()