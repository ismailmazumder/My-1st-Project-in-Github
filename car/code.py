import pygame
pygame.init()
# 1200 400
display  = pygame.display.set_mode((1200,400))
road = pygame.image.load('road1.png')
car = pygame.image.load('tesla.png')
car = pygame.transform.scale(car,(50,100))
win = pygame.image.load('last.jpg')
#50
poss = 300
while True:
    pygame.event.get()
    keys = pygame.key.get_pressed()
    display.blit(road, (0,0))
    display.blit(car,(140,poss))
    pygame.event.get()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        poss = poss - .1
        print(poss)
    elif keys[pygame.K_DOWN]:
        poss = poss + .1
        print(poss)

    if poss==50.9999999999965 or poss==50.09999999999656 or poss==50.19999999999655 or poss==50.29999999999654 or poss==44 or poss==45 or poss==46 or poss==47 or poss==48 or poss==49 or poss==50:
        display.blit(win,(0,0))

    pygame.display.update()