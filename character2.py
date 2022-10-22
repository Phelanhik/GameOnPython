import pygame

class BadCharacter():
    
    def __init__(self,screen,x):
        self.screen = screen
        self.x = x
        self.dno = 350
        self.y = self.dno
        self.speed = 30
        self.speedD = 30
        self.right = True
        self.move = False
        self.hit = False
        self.n = 1
        self.nr = 1
        self.nl = 15
        self.nmr = 29
        self.nml = 37
        self.npr = 47
        self.npl = 61
        self.njp = 53
        self.njpl = 67
        self.cadr = 0
        self.health = 100
        self.damage = 50
        self.heart = [self.x, self.y - 50]
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
                    self.cadr += 1
                    if self.cadr%3 == 0:
                        self.hit = True
                        self.xp = self.x + 220
                        self.yp = self.y + 200
                        self.screen.blit(self.punch_image, (self.xp, self.yp))
                    else:
                        self.hit = False
                else:
                    self.cadr += 1
                    if self.cadr%3 == 0:
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
                    
    def output(self):
        keys = pygame.key.get_pressed()
        if not keys[pygame.K_x]:
            if self.y >= self.dno:
                if self.right:
                    self.n = self.nr
                    self.nr += 1
                    if self.n == 14:
                        self.n = 1
                        self.nr = 1
                elif not self.right:
                    self.n = self.nl
                    self.nl += 1
                    if self.n == 28:
                        self.n = 15
                        self.nl = 15
                if self.move:
                    if self.right:
                        self.n = self.nmr
                        self.nmr += 1
                        if self.n == 36:
                            self.n = 29
                            self.nmr = 29
                    elif not self.right:
                        self.n = self.nml
                        self.nml += 1
                        if self.n == 44:
                            self.n = 37
                            self.nml = 37
            if self.y < self.dno:
                if self.right:
                    self.n = 44
                elif not self.right:
                    self.n = 45
        elif keys[pygame.K_x] and self.y == self.dno:
            if self.right:
                self.n = self.npr
                self.npr += 1
                if self.n == 52:
                    self.n = 46
                    self.npr = 46
            elif not self.right:
                self.n = self.npl
                self.npl += 1
                if self.n == 66:
                    self.n = 60
                    self.npl = 60
        elif keys[pygame.K_x] and self.y < self.dno:
            if self.right:
                self.n = self.njp
                self.njp += 1
                if self.n == 60:
                    self.n = 53
                    self.njp = 53
            elif not self.right:
                self.n = self.njpl
                self.njpl += 1
                if self.n == 73:
                    self.n = 67
                    self.njpl = 67
        
        self.screen.blit(self.galery[self.n], (self.x, self.y))
        
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
        if keys[pygame.K_x]:
            self.punching()
        elif keys[pygame.K_z]:
            self.punching()
        