import pygame
from Rak_code.loading_of_picters_Rak import Galery

class RakGamer1():
    
    def __init__(self,screen,x,right, width):
        self.screen = screen
        self.x = x
        self.dno = 250
        self.y = self.dno
        self.speed = 25
        self.speedD = 25
        self.right = right
        self.move = False
        self.hit = False
        self.cadr = 0
        self.cadr_jump = 0
        self.health = 100
        self.damage = 5
        self.heart_position = [self.x + 200, self.y + 200]
        self.xp = 0
        self.yp = 0
        self.imba = 0
        self.galery = Galery.galery
        self.punch_image = Galery.punch_image
        self.hitbox_image = Galery.hitbox_image
        self.health_image = Galery.health_image
        self.width = width

    def punching(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_x]:
            if self.y < self.dno:
                if self.right:
                    self.cadr_jump += 1
                    self.xp = self.x + 350
                    self.yp = self.y + 250
                    if (self.cadr_jump + 6) %9  == 0:
                        self.hit = True
                        self.screen.blit(self.punch_image, (self.xp, self.yp))
                    else:
                        self.hit = False
                else:
                    self.cadr_jump += 1
                    self.xp = self.x + 50
                    self.yp = self.y + 250
                    if (self.cadr_jump + 6) %9 == 0:
                        self.hit = True
                        self.screen.blit(self.punch_image, (self.xp, self.yp))
                    else:
                        self.hit = False
            elif self.y >= self.dno:
                if self.right:
                    self.cadr += 1
                    self.xp = self.x + 350
                    self.yp = self.y + 200
                    if (self.cadr+7) %10 == 0:
                        self.hit = True
                        self.screen.blit(self.punch_image, (self.xp, self.yp))
                    else:
                        self.hit = False
                else:
                    self.cadr += 1
                    self.xp = self.x + 50
                    self.yp = self.y + 200
                    if (self.cadr+7) %10 == 0:
                        self.hit = True
                        self.screen.blit(self.punch_image, (self.xp, self.yp))
                    else:
                        self.hit = False

 
    def output(self, frame):
        self.frame = frame
        self.screen.blit(self.galery[self.frame], (self.x, self.y))
        self.screen.blit(self.hitbox_image, (self.heart_position[0] - 12, self.heart_position[1] - 12))
        self.health_image = pygame.transform.scale(self.health_image, (self.health * 2,50))
        self.screen.blit(self.health_image, (100, 50))
     
    def moving(self):
        keys = pygame.key.get_pressed()
        if not keys[pygame.K_x] or self.y < self.dno:
            if keys[pygame.K_LEFT]:
                self.x -= self.speed
                if not self.right:
                    None
                else:
                    self.right = False
                if self.x < 0:
                    self.x = 0
            elif keys[pygame.K_RIGHT]: 
                self.x += self.speed
                if self.right:
                    None
                else:
                    self.right = True
                if self.x > self.width - 400:
                    self.x = self.width - 400
        if keys[pygame.K_UP]:
            self.y -= self.speedD
            self.speedD -= 3.5
            if self.y < 0:
                self.y = 0
            if self.y > self.dno:
                self.y = self.dno
        if not keys[pygame.K_UP] and self.y >= self.dno and (keys[pygame.K_LEFT] or keys[pygame.K_RIGHT]):
            self.move = True
        else:
            self.move = False
        if self.y < self.dno and not keys[pygame.K_UP]:                        
            self.speedD -= 6
            self.y -= self.speedD
        if self.y >= self.dno:
            self.y = self.dno
            self.speedD = 30

        self.heart_position = [self.x + 200, self.y + 200]

        if not keys[pygame.K_x]:
            self.cadr = 0
            
            self.hit = False
        if keys[pygame.K_x]:
            self.punching()
        elif keys[pygame.K_z]:
            self.punching()
        