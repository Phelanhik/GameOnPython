import pygame


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
            if self.is_colliding(f1.get_punch_position(), f2.heart_position[0], 50) and f1.hit:
                f2.health -= f1.damage
                print('попал')
                print(f1.health, f2.health)       
            if self.is_colliding(f2.get_punch_position(), f1.heart_position[0], 50) and f2.hit:
                f1.health -= f2.damage
                print('другой попал')
                print(f1.health, f2.health)
            if f1.health <= 0 or f2.health <= 0:
                f1.screen.blit(f1.galery[1], (f1.x, f1.y))
                print('deapth')
                print(f1.health, f2.health)
                exit()