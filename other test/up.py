
import pygame
truef = False
pygame.init()
display2 = pygame.display.set_mode((216,233))
blast  = pygame.image.load('blast.png')#216 233
while True:
    pygame.event.get()
    keys = pygame.key.get_pressed()
    display2.blit(blast,(0,0))
    if keys[pygame.K_UP]:
        truef = True
        if truef:
            print("Ismail Mazumder")
    pygame.display.update()