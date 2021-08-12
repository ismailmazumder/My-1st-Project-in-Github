import pygame
pygame.init()
# 1200 400
display  = pygame.display.set_mode((1200,400))
#road = pygame.image.load('road1.png')
road = pygame.image.load('road.png')
car = pygame.image.load('tesla.png')
car = pygame.transform.scale(car,(20,40))

#win = pygame.image.load('last.jpg')
#50
poss = 300
carposss = 150
while True:
    pygame.event.get()
    keys = pygame.key.get_pressed()
    display.blit(road, (0,0))
    display.blit(car,(carposss,poss))#155
    pygame.event.get()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        poss = poss - .1
        print(poss)
        #carposss = carposss + 1
    elif keys[pygame.K_DOWN]:
        poss = poss + .1
        print(poss)
        #carposss = carposss - 1
    elif keys[pygame.K_LEFT]:
        carposss = carposss - .1
    elif keys[pygame.K_RIGHT]:
        carposss = carposss + .1

    #elif
    #elif (event.type == pygame.QUIT):
    #elif (event.type == QUIT):
        #pygame.quit()

    pygame.display.update()
#win
'''
    if poss==50 or poss==51 or poss==52 or poss==53 or poss==54 or poss==55 or poss==56 or poss==57 or poss==12 or poss==13 or poss==14:
        display.blit(win,(0,0))

    pygame.display.update()
'''