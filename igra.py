import pygame
import random
from character1 import MainCharacter
from fight import Fight
from choice_of_cadr import ChoiceOfCadrs
from II import II
from choice_of_cadr_for_II import ChoiceOfCadrsII


def run():
    pygame.init()
    screen = pygame.display.set_mode((1200, 700))
    pygame.display.set_caption("Cum")
    running = True
    bg_color = pygame.image.load('sprites/bg1.jpg')
    bg_color = pygame.transform.scale(bg_color, (1200, 800))
    mycharacter = MainCharacter(screen,0,True)
    hischaracter = II(screen,600,False)
    fight = Fight(mycharacter, hischaracter)
    choise1 = ChoiceOfCadrs(mycharacter)
    choise2 = ChoiceOfCadrsII(hischaracter)

    while running:
        clock.tick(20)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.blit(bg_color, (0, 0))
        mycharacter.moving() 
        hischaracter.moving()
        mycharacter.output(choise1.choising())
        hischaracter.output(choise2.choising())
        
        fight.fighting()

        pygame.display.flip()
clock = pygame.time.Clock()
run()