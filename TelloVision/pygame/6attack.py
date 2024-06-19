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
        self.ver_y = 0
        self.jump = 0
        self.rect = pygame.Rect(x,y,50,50)
        self.attacking = False
        self.attack_type = 0

    def draw(self,screen):
        pygame.draw.rect(screen, (0, 255, 100), self.rect)

    def attack(self,screen,otherone):
        self.attacking = True
        arect = pygame.Rect(self.rect.centerx,self.rect.y,self.rect.width,self.rect.height)
        if arect.colliderect(otherone.rect):
            print("AAA")
        #self.attacking = False


        pygame.draw.rect(screen,(155,50,0),arect)



    def move(self,width,height,screen,otherone):
        dx = 0
        dy = 0
        SPEED = 10
        GF = 2

        key = pygame.key.get_pressed()
        #pygame.key.set_repeat(100, 150)
        if self.attacking == False:
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

            if key[pygame.K_r] or key[pygame.K_t]:
                self.attack(screen,otherone)
                if key[pygame.K_r]:
                    self.attack_type = 1
                if key[pygame.K_t]:
                    self.attack_type = 2




        self.ver_y += GF
        dy += self.ver_y

        if self.rect.x + dx < 0:
            dx = -self.rect.x
        if self.rect.right + dx > width:
            dx = width - self.rect.x - 50
        if self.rect.bottom + dy > 550:
            self.vel_y = 0
            dy = 550 - self.rect.bottom
            self.jump = 0

        self.rect.x += dx
        self.rect.y += dy

player1 = character(x1,y1)
player2 = character(x2,y2)
run = True
while run:
    clock.tick(FPS)
    draw_bg(bg)
    player1.move(width,height,screen,player2)
    player1.draw(screen)
    player2.draw(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()
pygame.quit()