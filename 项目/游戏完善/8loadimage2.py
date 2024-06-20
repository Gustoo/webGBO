import pygame
import time
from random import random

pygame.init()

attackimg = pygame.image.load("wani/Attack.png").convert_alpha()
animation =[]
attack = []
for i in range(13):
    imga = attackimg.subsurface(i*140,0,140,140)
    attack.append(imga)
animation.append(attack)
