import pygame
from ALLclass11 import character
import time
from random import random

pygame.init()
width = 1000
height = 600
title = "game"

a=5

clock = pygame.time.Clock()
FPS = 60

screen = pygame.display.set_mode((width,height))
pygame.display.set_caption(title)
bg = pygame.image.load("backg.jpg").convert_alpha()

#animation1 load
attackimg = pygame.image.load("wani/Attack.png").convert_alpha()
dieimg = pygame.image.load("wani/Death.png").convert_alpha()
hitimg = pygame.image.load("wani/Get hit.png").convert_alpha()
idleimg = pygame.image.load("wani/Idle.png").convert_alpha()
jumpimg = pygame.image.load("wani/Jump.png").convert_alpha()
runimg = pygame.image.load("wani/Run.png").convert_alpha()
animation1 =[];attack =[];die =[];hit =[];idle =[];jump =[];run=[]
for i in range(13):
    imga = attackimg.subsurface(i*140,0,140,140)
    imga = pygame.transform.scale(imga, (280, 280))
    attack.append(imga)
animation1.append(attack)
for i in range(18):
    imga = dieimg.subsurface(i*140,0,140,140)
    imga = pygame.transform.scale(imga, (280, 280))
    die.append(imga)
animation1.append(die)
for i in range(3):
    imga = hitimg.subsurface(i*140,0,140,140)
    imga = pygame.transform.scale(imga, (280, 280))
    hit.append(imga)
animation1.append(hit)
for i in range(10):
    imga = idleimg.subsurface(i*140,0,140,140)
    imga = pygame.transform.scale(imga, (280, 280))
    idle.append(imga)
animation1.append(idle)
for i in range(3):
    imga = jumpimg.subsurface(i*140,0,140,140)
    imga = pygame.transform.scale(imga, (280, 280))
    jump.append(imga)
animation1.append(jump)
for i in range(8):
    imga = runimg.subsurface(i*140,0,140,140)
    imga = pygame.transform.scale(imga, (280, 280))
    run.append(imga)
animation1.append(run)

#animation2 load
attackimg = pygame.image.load("Mushroom/Attack.png").convert_alpha()
dieimg = pygame.image.load("Mushroom/Death.png").convert_alpha()
hitimg = pygame.image.load("Mushroom/Take Hit.png").convert_alpha()
idleimg = pygame.image.load("Mushroom/Idle.png").convert_alpha()
runimg = pygame.image.load("Mushroom/Run.png").convert_alpha()
# attack =[];die =[];hit =[];idle =[];jump =[];run=[]
animation2 =[[],[],[],[],[],[]]
sheet = [8,4,4,4,8,8]
imglist = []
imglist.append(attackimg);imglist.append(dieimg);imglist.append(hitimg);imglist.append(idleimg);imglist.append(runimg);imglist.append(runimg)
for y,stuff in enumerate(imglist):
    for i in range(sheet[y]):
        imga = stuff.subsurface(i * 150, 0, 150, 150)
        imga = pygame.transform.scale(imga, (300, 300))
        animation2[y].append(imga)

def draw_bg(a):
    bgg = pygame.transform.scale(a, (width, height))
    screen.blit(bgg, (0, 0))

def draw_health(health, x, y):
    ratio = health / 100
    pygame.draw.rect(screen, (0,0,0), (x - 2, y - 2, 404, 34))
    pygame.draw.rect(screen, (255,0,0), (x, y, 400, 30))
    pygame.draw.rect(screen, (255,255,0), (x, y, 400 * ratio, 30))

x1=100;y1=500;x2=500;y2=500
player1 = character(x1,y1,animation1,1,False)
player2 = character(x2,y2,animation2,2,True)
run = True
while run:
    clock.tick(FPS)
    draw_bg(bg)
    draw_health(player1.health, 20, 20)
    draw_health(player2.health, 580, 20)
    player1.move(width,height,screen,player2)
    player2.move(width,height,screen,player1)
    player1.draw(screen)
    player2.draw(screen)
    player1.ani()
    player2.ani()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()

pygame.quit()
