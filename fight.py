import pygame


class Fight:
    def __init__(self, fighter1, fighter2, screen):
        self.fighter1 = fighter1
        self.fighter2 = fighter2
        self.screen = screen
        hit_image_link = ('sprites/hit.png')
        self.hit_image = pygame.image.load(hit_image_link)
        self.hitted1 = False
        self.hitted2 = False

    def is_colliding(self, x1, x2, y1, y2, step):
        return x1 > x2 - step and x1 < x2 + step and y1 > y2 - step * 2 and y1 < y2 + step * 2                #тут нужно добавить условие для игрека
        
    def fighting(self):
        f1 = self.fighter1
        f2 = self.fighter2
        
        if self.is_colliding(f1.xp, f2.heart_position[0], f1.yp, f2.heart_position[1], 50) and f1.hit:
            f2.health -= f1.damage
            self.screen.blit(self.hit_image, (200, 100))
            print(f1.health, f2.health)
            self.hitted1 = True
        else:
            self.hitted1 = False
        if self.is_colliding(f2.xp, f1.heart_position[0], f2.yp, f1.heart_position[1], 50) and f2.hit:
            f1.health -= f2.damage
            self.screen.blit(self.hit_image, (800, 100))
            print(f1.health, f2.health)
            self.hitted2 = True
        else:
            self.hitted2 = False
        if f1.health <= 0 or f2.health <= 0:
            f1.screen.blit(f1.galery[1], (f1.x, f1.y))
            print('deapth')
            print(f1.health, f2.health)
            