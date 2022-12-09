import pygame
from Rak_code.Rak_gamer1 import RakGamer1                               #Рэк как первый игрок
from Rak_code.cadrs_choise_Rak_gamer import ChoiceOfCadrsRak            #Выбор кадров Рэка как игрока
from Rumble_code.Rumble_II import RumbleII                              #Рамбл как ИИ
from Rumble_code.cadr_choise_Rumble_II import ChoiceOfCadrsRumbleII     #Выбор кадров Рамбла как ИИ
from camera import Camera                                               #Камера
from fight import Fight                                                 #Бой


def run():
    global mycharacter, hischaracter, fighting, choise1, choise2, camera, current
    pygame.init()
    width = 1200
    screen = pygame.display.set_mode((width, 800))
    pygame.display.set_caption("Cum")
    running = True
    bg_for_fight = pygame.transform.scale(pygame.image.load('sprites/bg1.jpg'), (3600, 800))
    bg_for_menu = pygame.transform.scale(pygame.image.load('sprites/bg2.jpg'), (1600, 800))
    bg_for_choising = pygame.transform.scale(pygame.image.load('sprites/bg3.jpg'), (1600, 800))

    mycharacter = RakGamer1(screen,0,True, width)
    hischaracter = RumbleII(screen,width - 300,False,mycharacter, width)
    fighting = Fight(mycharacter, hischaracter, screen)
    choise1 = ChoiceOfCadrsRak(mycharacter)
    choise2 = ChoiceOfCadrsRumbleII(hischaracter)
    camera = Camera(mycharacter, hischaracter, bg_for_fight, width)
    current = 0

    def choising_of_character(bg):
        global mycharacter, hischaracter, fighting, choise1, choise2, camera, current
        screen.blit(bg, (0, 0))
        screen.blit(mycharacter.galery[0], (100, 100))
        screen.blit(hischaracter.galery[0], (600, 200))
        keys = pygame.key.get_pressed()
        if keys[pygame.K_1]:
            mycharacter = RakGamer1(screen,0,True, width) 
            choise1 = ChoiceOfCadrsRak(mycharacter)
            hischaracter = RumbleII(screen,width - 300,False,mycharacter, width)
            choise2 = ChoiceOfCadrsRumbleII(hischaracter)
            fighting = Fight(mycharacter, hischaracter, screen)
            camera = Camera(mycharacter, hischaracter, bg_for_fight, width)
            print('поменяли')
            print(mycharacter.health)
        pygame.display.flip()
        if keys[pygame.K_5]:
            current = 1

    def fight(bg):
        global mycharacter, hischaracter, fighting, choise1, choise2, camera, current
        screen.blit(bg, (camera.bg_x, 0))
        if fighting.hitted1:
            screen.blit(fighting.hit_image, (200, 100))
        if fighting.hitted2:
            screen.blit(fighting.hit_image, (800, 100))
        mycharacter.moving() 
        hischaracter.moving()
        mycharacter.output(choise1.choising())
        hischaracter.output(choise2.choising())
        camera.apply()
        fighting.fighting()
        print(choise2.n)
        pygame.display.flip()
        global current
        if mycharacter.health <= 0 or hischaracter.health <= 0:
            current = 0

    def main_menu(bg):
        global current
        screen.blit(bg, (0,0))
        keys = pygame.mouse.get_pressed()
        if keys[0]:
            current = 1
        elif keys[2]:
            current = 2    
        pygame.display.flip()
        
    while running:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        if current == 1:
            fight(bg_for_fight)
        elif current == 0:
            main_menu(bg_for_menu)
        elif current == 2:
            choising_of_character(bg_for_choising)
        mouse_potition = pygame.mouse.get_pos()

clock = pygame.time.Clock()
run()