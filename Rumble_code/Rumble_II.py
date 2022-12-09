import pygame
import random
from Rumble_code.loading_of_picters_Rumble import Galery

class RumbleII():
 
    def __init__(self, screen, x, right, notII, width):
        self.a = 6
        self.aa = 6
        self.press = 0
        self.screen = screen
        self.x = x
        self.dno = 350
        self.y = self.dno
        self.speed = 30
        self.speedD = 100
        self.right = right
        self.move = False
        self.hit = False
        self.cadr = 0
        self.cadr_jump = 0
        self.health = 100
        self.damage = 10
        self.heart_position = [self.x, self.y - 50]
        self.xp = 0
        self.yp = 0
        self.imba = 0
        self.galery = []
        self.galery = Galery.galery
        self.punch_image = Galery.punch_image
        self.hitbox_image = Galery.hitbox_image
        self.health_image = Galery.health_image
        self.actions = {
            'rght': [0, 1, 2, 7, 8, 9, 20],
            'lft': [3, 4, 5, 10, 11, 12, 13],
            'up': [7, 11, 13, 20],
            'x': [13, 14, 15, 16, 17, 18, 19, 20],
            'state': [6]
        }
        self.notII = notII
        self.width = width

    def creating_a(self):
        in_range = 300
        
        if self.press == 7:
            if self.x - self.notII.x > in_range and self.aa not in self.actions['up']:
                self.aa = random.randint(3,6)
                self.press = 0
            elif self.notII.x - self.x > in_range:
                self.aa = random.randint(6,9)
                self.press = 0
            elif self.x - self.notII.x <= in_range or self.notII.x - self.x <= in_range:
                act = [14, 7, 11, 13, 15, 20]
                self.aa = act[random.randint(0, len(act) - 1)]
                while self.aa in self.actions['up']:
                    self.aa += 1
                self.press = 0
        if self.aa in self.actions['up']: 
            self.press += 1
        else:
            self.press += 1
        return self.aa

    def punching(self):
        if self.a in self.actions['x']:
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
                    if (self.cadr_jump + 9) %10  == 0:
                        self.hit = True
                        self.screen.blit(self.punch_image, (self.xp, self.yp))
                    else:
                        self.hit = False
            elif self.y >= self.dno:
                if self.right:
                    self.cadr += 1
                    self.xp = self.x + 220
                    self.yp = self.y + 130
                    if (self.cadr+3) %4 == 0:
                        self.hit = True
                        self.screen.blit(self.punch_image, (self.xp, self.yp))
                    else:
                        self.hit = False
                else:
                    self.cadr += 1
                    self.xp = self.x - 20
                    self.yp = self.y + 130
                    if (self.cadr+3) %4 == 0:
                        self.hit = True
                        self.screen.blit(self.punch_image, (self.xp, self.yp))
                    else:
                        self.hit = False
    
    def output(self, n):
        self.k = n
        self.screen.blit(self.galery[self.k], (self.x, self.y))
        self.screen.blit(self.hitbox_image, (self.heart_position[0] - 12, self.heart_position[1] - 12))
        self.health_image = pygame.transform.scale(self.health_image, (self.health * 2,50))
        self.screen.blit(self.health_image, (self.width - 300, 50))
        
    def moving(self):
        self.a = self.creating_a()
        if self.a != self.actions['x'] or self.y < self.dno:
            if self.a in self.actions['lft']:
                self.x -= self.speed
                if not self.right:
                    None
                else:
                    self.right = False
            elif self.a in self.actions['rght']: 
                self.x += self.speed
                if self.right:
                    None
                else:
                    self.right = True
        if self.a in self.actions['up']:
            self.y -= self.speedD
            self.speedD -= 0.1
            if self.y < 0:
                self.y = 0
            if self.y > self.dno:
                self.y = self.dno
        if self.a not in self.actions['up'] and self.y >= self.dno and (self.a in self.actions['lft'] or self.a in self.actions['rght']):
            self.move = True
        else:
            self.move = False
        if self.y < self.dno and self.a != self.actions['up']:                        
            self.speedD -= 6
            self.y -= self.speedD
        if self.y >= self.dno:
            self.y = self.dno
            self.speedD = 30

        self.heart_position = [self.x + 125, self.y + 100]

        if not self.a in self.actions['x']:
            self.cadr = 0
            self.hit = False
        if self.a in self.actions['x']:
            self.punching()
        

    
