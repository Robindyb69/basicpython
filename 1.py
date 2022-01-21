import pygame
import random

# Intialisere moduleene i pygame
pygame.init()

SCREEN = pygame.display.set_mode((500, 750))  # Setting the display

# background
BACKGROUND_IMAGE = pygame.image.load('background.jpg')

#  BIRD
BIRD_IMAGE = pygame.image.load('bird1.png')
bird_x = 50
bird_y = 300
bird_y_change = 0

def display_bird(x, y):
    SCREEN.blit(BIRD_IMAGE, (x, y))

# OBSTACLES
OBSTACLE_WIDTH = 70
OBSTACLE_HEIGHT = random.randint(150,450)
OBSTACLE_COLOR = (211, 253, 117)
OBSTACE_X_CHANGE = -4
obstacle_x = 500
