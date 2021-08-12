'''
import pygame
pygame.init()
display = pygame.display.set_mode((320,568))
bac = pygame.image.load('img.png')
bird = pygame.image.load('img_1.png')
bird_x = 0
truefal =True
while truefal:
    display.blit(bac,(0,0))
    display.blit(bird,(bird_x,100))
    way = 'Right'
    if (way == 'Right'):
        bird_x = bird_x  + 1
        print(bird_x)
        if bird_x == 266:
            way = 'Left'
    else:
        bird_x = bird_x - 1
        if bird_x==0:
            way = 'Right'
    pygame.display.update()
'''
