import pygame
import random

class II():
 
    def __init__(self,screen,x,right):
        self.a = 0
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
        self.health = 100
        self.damage = 5
        self.heart_position = [self.x, self.y - 50]
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
        self.actions = {
            'rght': [0, 1, 2, 7, 8, 9],
            'lft': [3, 4, 5, 10, 11, 12],
            'up': [6, 13],
            'x': [9, 13, 14, 15, 6, 11, 3, 7, 16, 17, 18, 19, 20]
        }
        self.amax = 100

    def creating_a(self):
        self.aa = random.randint(0,30)
        return self.aa

    def get_punch_position(self):
        if self.right:
            return self.x + 220
        elif not self.right:
            return self.x - 20

    def punching(self):
        self.a = self.creating_a()
        if self.a in self.actions['x']:
            if self.y < self.dno:
                if self.right:
                    self.cadr += 1
                    if self.cadr%10 == 0:
                        self.hit = True
                        self.xp = self.x + 220
                        self.yp = self.y + 200
                        self.screen.blit(self.punch_image, (self.xp, self.yp))
                    else:
                        self.hit = False
                else:
                    self.cadr += 1
                    if self.cadr%10 == 0:
                        self.hit = True
                        self.xp = self.x - 20
                        self.yp = self.y + 200
                        self.screen.blit(self.punch_image, (self.xp, self.yp))
                    else:
                        self.hit = False
            elif self.y >= self.dno:
                if self.right:
                    self.cadr += 1
                    if self.cadr%3 == 0:
                        self.hit = True
                        self.xp = self.x + 220
                        self.yp = self.y + 130
                        self.screen.blit(self.punch_image, (self.xp, self.yp))
                    else:
                        self.hit = False
                else:
                    self.cadr += 1
                    if self.cadr%3 == 0:
                        self.hit = True
                        self.xp = self.x - 20
                        self.yp = self.y + 130
                        self.screen.blit(self.punch_image, (self.xp, self.yp))
                    else:
                        self.hit = False
    
    def output(self, n):
        self.k = n
        self.screen.blit(self.galery[self.k], (self.x, self.y))
        
    def moving(self):
        b = random.randint(0,self.amax)
        if b != self.actions['x'] or self.y < self.dno:
            if b in self.actions['lft']:
                self.x -= self.speed
                if not self.right:
                    None
                else:
                    self.right = False
                if self.x < 0:
                    self.x = 0
            elif b in self.actions['rght']: 
                self.x += self.speed
                if self.right:
                    None
                else:
                    self.right = True
                if self.x > 1000:
                    self.x = 1000
        if b in self.actions['up']:
            self.y -= self.speedD
            self.speedD -= 3.5
            if self.y < 0:
                self.y = 0
            if self.y > self.dno:
                self.y = self.dno
        if b not in self.actions['up'] and self.y >= self.dno and (b in self.actions['lft'] or b in self.actions['rght']):
            self.move = True
        else:
            self.move = False
        if self.y < self.dno and b != self.actions['up']:                        
            self.speedD -= 6
            self.y -= self.speedD
        if self.y >= self.dno:
            self.y = self.dno
            self.speedD = 30

        self.heart_position = [self.x, self.y - 50]

        if b in self.actions['x']:
            self.punching()
        

    
