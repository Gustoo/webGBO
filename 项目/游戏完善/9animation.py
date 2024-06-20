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
bg = pygame.image.load("backg.jpg").convert_alpha()

#animation load
attackimg = pygame.image.load("wani/Attack.png").convert_alpha()
dieimg = pygame.image.load("wani/Death.png").convert_alpha()
hitimg = pygame.image.load("wani/Get hit.png").convert_alpha()
idleimg = pygame.image.load("wani/Idle.png").convert_alpha()
jumpimg = pygame.image.load("wani/Jump.png").convert_alpha()
runimg = pygame.image.load("wani/Run.png").convert_alpha()
animation =[]
attack =[];die =[];hit =[];idle =[];jump =[];run=[]
for i in range(13):
    imga = attackimg.subsurface(i*140,0,140,140)
    imga = pygame.transform.scale(imga, (280, 280))
    attack.append(imga)
animation.append(attack)
for i in range(18):
    imga = dieimg.subsurface(i*140,0,140,140)
    imga = pygame.transform.scale(imga, (280, 280))
    die.append(imga)
animation.append(die)
for i in range(3):
    imga = hitimg.subsurface(i*140,0,140,140)
    imga = pygame.transform.scale(imga, (280, 280))
    hit.append(imga)
animation.append(hit)
for i in range(10):
    imga = idleimg.subsurface(i*140,0,140,140)
    imga = pygame.transform.scale(imga, (280, 280))
    idle.append(imga)
animation.append(idle)
for i in range(3):
    imga = jumpimg.subsurface(i*140,0,140,140)
    imga = pygame.transform.scale(imga, (280, 280))
    jump.append(imga)
animation.append(jump)
for i in range(8):
    imga = runimg.subsurface(i*140,0,140,140)
    imga = pygame.transform.scale(imga, (280, 280))
    run.append(imga)
animation.append(run)

def draw_bg(a):
    bgg = pygame.transform.scale(a, (width, height))
    screen.blit(bgg, (0, 0))

def draw_health(health, x, y):
    ratio = health / 100
    pygame.draw.rect(screen, (0,0,0), (x - 2, y - 2, 404, 34))
    pygame.draw.rect(screen, (255,0,0), (x, y, 400, 30))
    pygame.draw.rect(screen, (255,255,0), (x, y, 400 * ratio, 30))

class character():
    def __init__(self, x, y,animation):
        self.update_time = pygame.time.get_ticks()
        self.animation = animation
        self.atype = 0
        self.aframe = 0
        self.image = self.animation[self.atype][self.aframe]
        self.flip = False
        self.ver_y = 0
        self.jump = 0
        self.rect = pygame.Rect(x,y,50,50)
        self.attacking = False
        self.attack_type = 0
        self.health = 100

    def ani(self):
        anitime = 50
        self.image = self.animation[self.atype][self.aframe]
        if pygame.time.get_ticks() - self.update_time > anitime:
            self.aframe += 1
            self.update_time = pygame.time.get_ticks()
        if self.aframe >= len(self.animation[self.atype]):
            self.aframe = 0




    def draw(self,screen):
        imgflip = pygame.transform.flip(self.image,self.flip,False)
        pygame.draw.rect(screen, (0, 255, 100), self.rect)
        screen.blit(imgflip,(self.rect.x-110,self.rect.y-150))

    def attack(self,screen,otherone):
        self.attacking = True
        arect = pygame.Rect(self.rect.centerx-(self.rect.width*self.flip),self.rect.y,self.rect.width,self.rect.height)
        if arect.colliderect(otherone.rect):
            otherone.health -= 10
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

        if otherone.rect.centerx > self.rect.centerx:
            self.flip = False
        else:
            self.flip = True



        self.rect.x += dx
        self.rect.y += dy

player1 = character(x1,y1,animation)
player2 = character(x2,y2,animation)
run = True
while run:
    clock.tick(FPS)
    draw_bg(bg)
    draw_health(player1.health, 20, 20)
    draw_health(player2.health, 580, 20)
    player1.move(width,height,screen,player2)
    player1.draw(screen)
    player2.draw(screen)
    player1.ani()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()
pygame.quit()
