import pygame

class Camera():
    def __init__(self, f1, f2, bg, width):
        self.f1 = f1
        self.f2 = f2
        self.bg = bg
        self.width = width
        self.bg_x = -1200
        self.bg_xleft = 0
        self.bg_xright = -1000 * 2


    def apply(self):
        keys = pygame.key.get_pressed()
        if self.f1.x < 1 and keys[pygame.K_LEFT] and self.bg_x < self.bg_xleft and not (keys[pygame.K_x] and self.f1.y >= self.f1.dno):
            self.f2.x += self.f1.speed
            self.bg_x += self.f1.speed
        elif self.f1.x > self.width - 401 and keys[pygame.K_RIGHT] and self.bg_x > self.bg_xright and not (keys[pygame.K_x] and self.f1.y >= self.f1.dno):
            self.f2.x -= self.f1.speed
            self.bg_x -= self.f1.speed