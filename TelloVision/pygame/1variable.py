#grammar
import pygame
import time

pygame.init()
#variable
width = 1000
height = 600
title = "game"

screen = pygame.display.set_mode((width,height))
pygame.display.set_caption(title)
time.sleep(6)


'''
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
pygame.quit()
'''