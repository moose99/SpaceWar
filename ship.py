# contains code for the ship object
__author__ = 'Mus'

# initialize variables to hold the ships rectangle and image
shipRect = None
shipImage = None

# func to create the ship
def SetupShip(game):
    # use 'global' to indicate that we are changing the shipRect/shipImage vars declared outside the function
    global shipRect
    global shipImage
    SHIP_WIDTH = 30
    SHIP_HEIGHT = 30
    shipRect = game.Rect(250, 250, SHIP_WIDTH, SHIP_HEIGHT)
    shipImage = game.image.load('assets/rocketship.png')

# draws the ship on the surface provided
def DrawShip(surface):
    surface.blit(shipImage, shipRect)

