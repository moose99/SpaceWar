# This is the main code for the spacewar sample game.
__author__ = 'Mus'
import pygame, sys
from pygame.locals import *

# bring in my code from other python files
import space, ship, asteroid, bullet

# set up pygame
pygame.mixer.pre_init(22050, -16, 2, 512)
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
turnCCW = False
turnCW = False
thruster = False

# set up other objects (sprites)
ship.SetupShip(pygame)
space.SetupSpace(pygame)
bullet.SetupBullet(pygame)

# run game loop
while (True):
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        # check input
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == K_LEFT or event.key == ord('a'):
                turnCW = False
                turnCCW = True
            if event.key == K_RIGHT or event.key == ord('d'):
                turnCCW = False
                turnCW = True
            if event.key == K_UP or event.key == ord('w'):
                thruster = True
                ship.engineSound.play(-1)
            if event.key == K_RETURN:
                bullet.FireBullet(pygame, ship.shipPosX, ship.shipPosY, ship.shipRotation)

        if event.type == KEYUP:
            if event.key == K_LEFT or event.key == ord('a'):
                turnCCW = False
            if event.key == K_RIGHT or event.key == ord('d'):
                turnCW = False
            if event.key == K_UP or event.key == ord('w'):
                thruster = False
                ship.engineSound.stop()

    # send motion variables to ship, so it can turn or move
    ship.TransformShip(windowSurface, turnCCW, turnCW, thruster)

    # draw background
    space.DrawSpace(windowSurface)

    # draw ship
    ship.DrawShip(windowSurface, pygame)

    # draw bullets
    bullet.DrawBullet(windowSurface)

    # draw the window onto the screen
    pygame.display.update()

    #set framerate to 60fps
    mainClock.tick(60)