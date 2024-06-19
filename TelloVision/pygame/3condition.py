import pygame
import time
from random import random

pygame.init()
width = 1000
height = 600
title = "game"
x=100
y=100
a=5

clock = pygame.time.Clock()
FPS = 60

screen = pygame.display.set_mode((width,height))
pygame.display.set_caption(title)
bg = pygame.image.load("backg.jpg")

def draw_bg(a):
    bgg = pygame.transform.scale(a, (width, height))
    screen.blit(bgg, (0, 0))

run = True
while run:
    clock.tick(FPS)
    draw_bg(bg)
    pygame.draw.ellipse(screen,(0,255,100),(x,y,50,50))
    x = x+a
    if(x>width-50):
        a = -5
    if(x<0):
        a = 5

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()
pygame.quit()