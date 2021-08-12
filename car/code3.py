import pygame
import time
pygame.init()
dissco = [1200,400]
display = pygame.display.set_mode((dissco))
road = pygame.image.load('road1.png')
car = pygame.image.load('tesla.png')
car = pygame.transform.scale(car,(50,75))
#samne = 255
truefal = True
car_x = 140
car_y = 255
while truefal:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            truefal = False
    #time.sleep(2)
    cam_x = car_x + 30
    cam_y = car_y +20
    #dissco = dissco[0] - 1
    #dissco[0] = dissco[0] + 1
    #print(dissco)
    display.blit(road,(0,0))
    display.blit(car,(car_x,car_y))
    pygame.draw.circle(display,(0,255,0),(cam_x,cam_y),5,5)
    #samne = samne - .1
    pygame.display.update()


#dissco[0], dissco[1] = dissco[0]+1, dissco[1]+1