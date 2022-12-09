import pygame

class Galery():
    galery = []
    for n in range(14):
        path = 'sprites/'
        character_image_link = (path + 'Rak/' + str(n+1) + '.png')
        character_image = pygame.image.load(character_image_link)
        character_image = pygame.transform.scale(character_image, (400,400))
        galery.append(character_image)
    for n in range(14):
        character_image = pygame.transform.flip(galery[n], True, False)
        galery.append(character_image)
    for n in range(7):
        path = 'sprites/'
        character_image_link = (path + 'Rak/' + str(n+29) + '.png')
        character_image = pygame.image.load(character_image_link)
        character_image = pygame.transform.scale(character_image, (400,400))
        galery.append(character_image)
    for n in range(7):
        character_image = pygame.transform.flip(galery[n+28], True, False)
        galery.append(character_image)  
    character_image_link = (path + 'Rak/' + str(43) + '.png')
    character_image = pygame.image.load(character_image_link)
    character_image = pygame.transform.scale(character_image, (400,400))
    galery.append(character_image)
    character_image = pygame.transform.flip(galery[42], True, False)
    galery.append(character_image)  
    for n in range(10):
        path = 'sprites/'
        character_image_link = (path + 'Rak/' + str(n+45) + '.png')
        character_image = pygame.image.load(character_image_link)
        character_image = pygame.transform.scale(character_image, (400,400))
        galery.append(character_image)
    for n in range(10):
        character_image = pygame.transform.flip(galery[n+44], True, False)
        galery.append(character_image)
    for n in range(9):
        path = 'sprites/'
        character_image_link = (path + 'Rak/' + str(n+65) + '.png')
        character_image = pygame.image.load(character_image_link)
        character_image = pygame.transform.scale(character_image, (400,400))
        galery.append(character_image)
    for n in range(10):
        character_image = pygame.transform.flip(galery[n+64], True, False)
        galery.append(character_image)    
    print(len(galery))
    punch_image_link = (path + 'punch.png')
    punch_image = pygame.image.load(punch_image_link)
    punch_image = pygame.transform.scale(punch_image, (25,25))
    hitbox_image_link = (path + 'hitbox.png')
    hitbox_image = pygame.image.load(hitbox_image_link)
    hitbox_image = pygame.transform.scale(hitbox_image, (25,25))
    healt_image_link = (path + 'health.png')
    health_image = pygame.image.load(healt_image_link)
    health_image = pygame.transform.scale(health_image, (100,50))