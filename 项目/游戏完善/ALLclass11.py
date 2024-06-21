import pygame
import time

class character():
    def __init__(self, x, y,animation,player,flip):
        self.update_time = pygame.time.get_ticks()
        self.animation = animation
        self.atype = 3  #idle
        self.aframe = 0
        self.image = self.animation[self.atype][self.aframe]
        self.flip = flip
        self.ver_y = 0
        self.running = False
        self.jump = 0
        self.rect = pygame.Rect(x,y,50,50)
        self.attacking = False
        self.attackcooldown = 0
        self.hit = False
        self.attack_type = 0
        self.health = 10
        self.alive = True
        self.player = player

    def ani(self):
        # attack =[];die =[];hit =[];idle =[];jump =[];run=[]
        if self.running:
            self.aniupdate(5)
        elif self.health <= 0:
            self.health = 0
            self.alive = False
            self.aniupdate(1)
        elif self.jump == 1 or self.jump == 2:
            self.aniupdate(4)
        elif self.attacking:
            self.aniupdate(0)
        elif self.hit:
            self.aniupdate(2)
        else:
            self.aniupdate(3)
        anitime = 50
        self.image = self.animation[self.atype][self.aframe]
        if pygame.time.get_ticks() - self.update_time > anitime:
            self.aframe += 1
            self.update_time = pygame.time.get_ticks()
        if self.aframe >= len(self.animation[self.atype]):
            if self.alive == False:
                self.aframe = len(self.animation[self.atype]) - 1
            else:
                self.aframe = 0
                if self.atype == 0:
                    self.attacking = False
                    self.attackcooldown = 50
                if self.atype == 2:
                    self.hit = False
                    self.attacking = False
                    self.attackcooldown = 50

    def aniupdate(self,newatype):
        if newatype != self.atype:
            self.atype = newatype
            self.aframe = 0
            self.update_time = pygame.time.get_ticks()

    def draw(self,screen):
        imgflip = pygame.transform.flip(self.image,self.flip,False)
        #pygame.draw.rect(screen, (0, 255, 100), self.rect)
        screen.blit(imgflip,(self.rect.x-110,self.rect.y-150))

    def attack(self,screen,otherone):
        if self.attackcooldown == 0:
            self.attacking = True
            arect = pygame.Rect(self.rect.centerx-(self.rect.width*self.flip),self.rect.y,self.rect.width,self.rect.height)
            if arect.colliderect(otherone.rect):
                otherone.health -= 10
                otherone.hit = True
            #pygame.draw.rect(screen,(155,50,0),arect)

    def move(self,width,height,screen,otherone):
        dx = 0
        dy = 0
        SPEED = 10
        GF = 2
        self.running = False
        key = pygame.key.get_pressed()

        if self.attacking == False and self.alive:
            if self.player == 1:
                if key[pygame.K_LEFT]:
                    dx = -SPEED
                    self.running = True
                if key[pygame.K_RIGHT]:
                    dx = SPEED
                    self.running = True
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

            if self.player ==2:
                if key[pygame.K_a]:
                    dx = -SPEED
                    self.running = True
                if key[pygame.K_d]:
                    dx = SPEED
                    self.running = True
                if key[pygame.K_KP7] and self.jump == 1:
                    self.jump += 1
                    self.ver_y = -20
                if key[pygame.K_w] and self.jump == 0:
                    self.jump = 1
                    self.ver_y = -30
                if key[pygame.K_c] or key[pygame.K_v]:
                    self.attack(screen,otherone)
                    if key[pygame.K_c]:
                        self.attack_type = 1
                    if key[pygame.K_v]:
                        self.attack_type = 2

        self.ver_y += GF
        dy += self.ver_y
        if self.attackcooldown>0:
            self.attackcooldown -= 1

        if self.rect.x + dx < 0:
            dx = -self.rect.x
        if self.rect.right + dx > width:
            dx = width - self.rect.x - 50
        if self.rect.bottom + dy > 550:
            self.vel_y = 0
            dy = 550 - self.rect.bottom
            self.jump = 0

        if otherone.rect.centerx > self.rect.centerx and self.alive:
            self.flip = False
        else:
            self.flip = True

        self.rect.x += dx
        self.rect.y += dy