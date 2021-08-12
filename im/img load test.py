import pygame
pygame.init()
display = pygame.display.set_mode((1200, 400))
road =  pygame.image.load('road1.png')
truefal = True
while truefal:
    display.blit(road,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            truefal = False
    #window.blit(road,(0,0))
    pygame.display.update()
    #window.quit()