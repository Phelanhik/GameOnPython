import pygame
from character1 import MainCharacter


screen = None
fighter1 = MainCharacter(screen,0,True)
fighter2 = MainCharacter(screen,800,False)

class Boi:
    def fighting():
        fighter1.moving()
        fighter2.moving()
      
        if fighter1.xp > fighter2.heart[1]-5 and fighter1.xp < fighter2.heart[1]+5:
            fighter2.health -= fighter1.damage
            print('попал')
        if fighter2.xp > fighter1.heart[1]-5 and fighter2.xp < fighter1.heart[1]+5:
            fighter1.health -= fighter2.damage
            print('попал')
        if fighter1.health <= 0 or fighter2.health <= 0:
            fighter1.screen.blit(fighter1.galery[1], (fighter1.x, fighter1.y))
            print('deapth')