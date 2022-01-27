import  pygame
from pygame.locals import *

pygame.init()

screen_width = 864
screen_height = 936

screen = Pygame.dislay.set_mode((screen_width, screen_height))
pygame.display.set_caption('Flappy Bird')

#game variabler
scroll_scroll = 0
scroll_speed = 4

#load images
bg = pygame.image.load('img/bg.png')
ground_img  = pygame.image.load('img/ground.png')

run = True
while run:

    screen.blit(bg, (0,0))

    screen.blit(ground_img, (ground_scroll, 768))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


    pygame.display.update()

pygame.quit()


