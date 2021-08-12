'''
import pygame
pygame.init()
# 1200 400
display  = pygame.display.set_mode((1200,400))
road = pygame.image.load('road1.png')
car = pygame.image.load('tesla.png')
car = pygame.transform.scale(car,(30,50))
win = pygame.image.load('last.jpg')
#50
poss = 300
while True:
    #pygame.event.get()
    keys = pygame.key.get_pressed()
    display.blit(road, (0,0))
    display.blit(car,(140,poss))
    pygame.event.get()
    keys = pygame.key.get_pressed()

    pygame.display.update()
'''

import pygame
