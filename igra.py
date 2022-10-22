import pygame
from character1 import MainCharacter
from fight import Fight

def run():
    pygame.init()
    screen = pygame.display.set_mode((1200, 700))
    pygame.display.set_caption("Cum")
    running = True
    bg_color = pygame.image.load('sprites/bg1.jpg')
    bg_color = pygame.transform.scale(bg_color, (1200, 800))
    mycharacter = MainCharacter(screen,0,True)
    hischaracter = MainCharacter(screen,600,False)
    fight = Fight(mycharacter, hischaracter)

       

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
        fight.fighting()

        pygame.display.flip()
clock = pygame.time.Clock()
run()