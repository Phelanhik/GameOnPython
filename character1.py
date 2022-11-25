import pygame
from choice_of_cadr import ChoiceOfCadrs

class MainCharacter():
    
    def __init__(self,screen,x,right):
        self.screen = screen
        self.x = x
        self.dno = 350
        self.y = self.dno
        self.speed = 30
        self.speedD = 30
        self.right = right
        self.move = False
        self.hit = False
        self.cadr = 0
        self.cadr_jump = 0
        self.health = 100
        self.damage = 5
        self.heart_position = [self.x + 125, self.y - 50]
        self.xp = 0
        self.yp = 0
        self.galery = []
        for n in range(73):
            path = 'sprites/'
            character_image_link = (path + str(n+1) + '.png')
            character_image = pygame.image.load(character_image_link)
            character_image = pygame.transform.scale(character_image, (250,300))
            self.galery.append(character_image)
        punch_image_link = (path + 'punch.png')
        punch_image = pygame.image.load(punch_image_link)
        self.punch_image = pygame.transform.scale(punch_image, (20,20))

    def punching(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_x]:
            if self.y < self.dno:
                if self.right:
                    self.cadr_jump += 1
                    self.xp = self.x + 220
                    self.yp = self.y + 200
                    if (self.cadr_jump + 9) %10  == 0:
                        self.hit = True
                        self.screen.blit(self.punch_image, (self.xp, self.yp))
                    else:
                        self.hit = False
                else:
                    self.cadr_jump += 1
                    self.xp = self.x - 20
                    self.yp = self.y + 200
                    if (self.cadr_jump + 9) %10 == 0:
                        self.hit = True
                        self.screen.blit(self.punch_image, (self.xp, self.yp))
                    else:
                        self.hit = False
            elif self.y >= self.dno:
                if self.right:
                    self.cadr += 1
                    self.xp = self.x + 220
                    self.yp = self.y + 130
                    if (self.cadr+2) %3 == 0:
                        self.hit = True
                        self.screen.blit(self.punch_image, (self.xp, self.yp))
                    else:
                        self.hit = False
                else:
                    self.cadr += 1
                    self.xp = self.x - 20
                    self.yp = self.y + 130
                    if (self.cadr+2) %3 == 0:
                        self.hit = True
                        self.screen.blit(self.punch_image, (self.xp, self.yp))
                    else:
                        self.hit = False
 
    
    def output(self, n):
        self.k = n
        self.screen.blit(self.galery[self.k], (self.x, self.y))
        
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
                if self.x > 1000:
                    self.x = 1000
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

        self.heart_position = [self.x + 125, self.y - 50]

        if keys[pygame.K_x]:
            self.punching()
        elif keys[pygame.K_z]:
            self.punching()
        