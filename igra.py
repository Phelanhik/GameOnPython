import pygame
from character1 import MainCharacter


def run():
    pygame.init()
    screen = pygame.display.set_mode((1200, 700))
    pygame.display.set_caption("Cum")
    running = True
    bg_color = pygame.image.load('sprites/bg1.jpg')
    bg_color = pygame.transform.scale(bg_color, (1200, 800))
    mycharacter = MainCharacter(screen,0,True)
    hischaracter = MainCharacter(screen,800,False)

    def fighting():
        print(mycharacter.xp, hischaracter.xp, hischaracter.heart)
        if mycharacter.xp > hischaracter.heart[1]-50 and mycharacter.xp < hischaracter.heart[1]+50:
            hischaracter.health -= mycharacter.damage
            print('попал')
        if hischaracter.xp > mycharacter.heart[1]-5 and hischaracter.xp < mycharacter.heart[1]+5:
            mycharacter.health -= hischaracter.damage
            print('jqпопал')
        if mycharacter.health <= 0 or hischaracter.health <= 0:
            mycharacter.screen.blit(mycharacter.galery[1], (mycharacter.x, mycharacter.y))
            print('deapth')
            exit()

    while running:
        clock.tick(20)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.blit(bg_color, (0, 0))
        mycharacter.output()
        mycharacter.moving()
        hischaracter.output()
        hischaracter.moving()
        fighting()

        pygame.display.flip()
clock = pygame.time.Clock()
run()