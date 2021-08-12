import pygame

pygame.init()
display =  pygame.display.set_mode((320,568))
bg = pygame.image.load('img.png')
bird = pygame.image.load('img_1.png')
bird_y = 150
while True:
    pygame.event.get()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        bird_y = bird_y - .1
    elif keys[pygame.K_DOWN]:
        bird_y = bird_y + .1
    #elif keys[K_]

    display.blit(bg,(0,0))
    display.blit(bird, (100, bird_y))
    pygame.display.update()