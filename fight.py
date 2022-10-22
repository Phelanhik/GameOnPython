import pygame
from character1 import MainCharacter


class Fight:
    def __init__(self, fighter1, fighter2):
        self.fighter1 = fighter1
        self.fighter2 = fighter2

    def is_colliding(self, x1, x2, step):
        return x1 > x2 - step and x1 < x2 + step

    def fighting(self):
        f1 = self.fighter1
        f2 = self.fighter2
    
        keys = pygame.key.get_pressed()
        if keys[pygame.K_x]:
            if self.is_colliding(f1.xp, f2.heart_position[0], 30):
                f2.health -= f1.damage
                print('попал')
            if self.is_colliding(f2.xp, f1.heart_position[0], 30):
                f1.health -= f2.damage
                print('другой попал')
            if f1.health <= 0 or f2.health <= 0:
                f1.screen.blit(f1.galery[1], (f1.x, f1.y))
                print('deapth')