import pygame
import time
from random import random

pygame.init()
width = 1000
height = 600
title = "game"
x=100
y=500
a=5
ver_y =0
jump=False

clock = pygame.time.Clock()
FPS = 60

screen = pygame.display.set_mode((width,height))
pygame.display.set_caption(title)
bg = pygame.image.load("backg.jpg")

def draw_bg(a):
    bgg = pygame.transform.scale(a, (width, height))
    screen.blit(bgg, (0, 0))

def move():
    global x,y,ver_y,jump
    dx = 0
    dy = 0
    SPEED = 10
    GF = 2

    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT]:
        dx = -SPEED
    if key[pygame.K_RIGHT]:
        dx = SPEED
    if key[pygame.K_UP] and jump==False:
        ver_y = -30
        jump = True

    ver_y += GF
    dy += ver_y

    if x +dx < 0:
        dx = -x
    if x+50 + dx > width:
        dx = width-x-50
    if y + dy > 450:
        vel_y = 0
        dy = 450-y
        jump = False

    x += dx
    y += dy

run = True
while run:
    clock.tick(FPS)
    draw_bg(bg)
    move()
    pygame.draw.ellipse(screen,(0,255,100),(x,y,50,50))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()
pygame.quit()