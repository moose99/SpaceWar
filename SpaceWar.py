# This is the main code for the spacewar game
__author__ = 'Mus'
import pygame, sys
from pygame.locals import *

# bring in my code from other python files
import space, ship, asteroid, bullet

# set up pygame
pygame.init()

# get the clock, so we can set the framerate later
mainClock = pygame.time.Clock()

# set up the window
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500
windowSurface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), 0, 32)
pygame.display.set_caption('Space War')

# set up colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

#set up fonts
FONT_SIZE = 48
basicFont = pygame.font.SysFont(None, FONT_SIZE)

# set up movement variables
moveLeft = False
moveRight = False

# set up other objects (sprites)
ship.SetupShip(pygame)
space.SetupSpace(pygame)

# run game loop
while (True):
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        # check input
        if event.type == KEYDOWN:
            # change the keyboard variables
            if event.key == K_LEFT or event.key == ord('a'):
                moveRight = False
                moveLeft = True
            if event.key == K_RIGHT or event.key == ord('d'):
                moveLeft = False
                moveRight = True

        if event.type == KEYUP:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == K_LEFT or event.key == ord('a'):
                moveLeft = False
            if event.key == K_RIGHT or event.key == ord('d'):
                moveRight = False

    # draw the black background onto the surface
    windowSurface.fill(BLACK)

    # draw background
    space.DrawSpace(windowSurface)

    # draw ship
    ship.DrawShip(windowSurface)

    # draw the window onto the screen
    pygame.display.update()

    #set framerate to 60fps
    mainClock.tick(60)