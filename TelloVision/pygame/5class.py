import pygame
import time
from random import random

pygame.init()
width = 1000
height = 600
title = "game"
x1=100
y1=500
x2=500
y2=500
a=5

clock = pygame.time.Clock()
FPS = 60

screen = pygame.display.set_mode((width,height))
pygame.display.set_caption(title)
bg = pygame.image.load("backg.jpg")

def draw_bg(a):
    bgg = pygame.transform.scale(a, (width, height))
    screen.blit(bgg, (0, 0))

class character():
    def __init__(self, x, y,):
        self.x = x
        self.y = y
        self.ver_y = 0
        self.jump =0

    def draw(self,screen):
        pygame.draw.ellipse(screen, (0, 255, 100), (self.x, self.y, 50, 50))

    def move(self,width,height):
        dx = 0
        dy = 0
        SPEED = 10
        GF = 2

        key = pygame.key.get_pressed()
        #pygame.key.set_repeat(100, 150)
        if key[pygame.K_LEFT]:
            dx = -SPEED
        if key[pygame.K_RIGHT]:
            dx = SPEED
        if key[pygame.K_TAB] and self.jump == 1:
            self.jump += 1
            self.ver_y = -20
        if key[pygame.K_UP] and self.jump == 0:
            self.jump = 1
            self.ver_y = -30

        self.ver_y += GF
        dy += self.ver_y
        #print("self.jump")
        if self.x + dx < 0:
            dx = -self.x
        if self.x + 50 + dx > width:
            dx = width - self.x - 50
        if self.y + dy > 450:
            self.vel_y = 0
            dy = 450 - self.y
            self.jump = 0

        self.x += dx
        self.y += dy

player1 = character(x1,y1)
player2 = character(x2,y2)
run = True
while run:
    clock.tick(FPS)
    draw_bg(bg)
    player1.move(width,height)
    player1.draw(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()
pygame.quit()