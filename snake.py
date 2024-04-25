# import modules
import pygame
from pygame.locals import *

pygame.init()

# create blank game window
screen_width = 600
screen_height = 600

# create game window
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Snake')


# setup loop with exit event handler
run = True
while run:

    # iterate through events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    
    # update the display
    pygame.display.update()


# end pygame
pygame.quit()

# create a snake and setup the snake list