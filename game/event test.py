'''
import pygame
pygame.init()

dispaly = pygame.display.set_mode((50,50))
image = pygame.image.load('img_1.png')
while True:
    #pygame.get.event()
    pygame.event.get()
    keys = pygame.key.get_pressed()
    dispaly.blit(image,(0,0))

    if keys[pygame.K_SPACE]:
        print("You are pressed space button.")

    pygame.dispaly.update()
'''
import pygame
import time
pygame.init()
display = pygame.display.set_mode((320,568))
image = pygame.image.load('img.png')
bird = pygame.image.load('img_1.png')
bird_x = 0
while True:
    pygame.event.get()
    keys = pygame.key.get_pressed()
    '''
    if keys[pygame.K_SPACE]:
        print("Space")
    elif keys[pygame.K_LEFT]:
        
        print("Left")#bam
    '''

    move = 'Right'

    if move=='Right':
        bird_x = bird_x + 1
        time.sleep(.01)
        print(bird_x)
        if bird_x==269:
            move='Left'
    else:
        bird_x = bird_x - 1


    display.blit(image,(0,0))
    display.blit(bird,(bird_x,0))
    pygame.display.update()