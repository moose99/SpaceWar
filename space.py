# contains code for the space (background) object
__author__ = 'Mus'

# initialize variables to hold the space rectangle and image
spaceRect = None
spaceImage = None

# func to create the space
def SetupSpace(game):
    # use 'global' to indicate that we are changing the spaceRect/spaceImage vars declared outside the function
    global spaceRect
    global spaceImage
    SPACE_WIDTH = 1280
    SPACE_HEIGHT = 796
    spaceRect = game.Rect(0, 0, SPACE_WIDTH, SPACE_HEIGHT)
    spaceImage = game.image.load('assets/B1_stars.png')

def DrawSpace(surface):
    surface.blit(spaceImage, spaceRect)