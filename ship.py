# contains code for the ship object
__author__ = 'Mus'

# initialize variables to hold the ships rectangle and image
shipRect = None
shipImage = None

# ship size
SHIP_WIDTH = 30
SHIP_HEIGHT = 30

# init vars to hold velocity, speed, position and rotation
SHIP_ROTATION_AMOUNT = 2
shipRotation = 0    # goes from 0 to 360
shipPosX = 250
shipPosY = 250

# func to create the ship
def SetupShip(game):
    # use 'global' to indicate that we are changing the shipRect/shipImage vars declared outside the function
    global shipRect
    global shipImage
    shipRect = game.Rect(shipPosX-(SHIP_WIDTH/2), shipPosY-(SHIP_HEIGHT/2), SHIP_WIDTH, SHIP_HEIGHT)
    shipImage = game.image.load('assets/rocketship.png')

# draws the ship on the surface provided
def DrawShip(surface, game):
    #first apply ship rotation
    oldCenter = shipRect.center
    rotatedShipImage = game.transform.rotate(shipImage, shipRotation)
    rotatedRect = rotatedShipImage.get_rect()
    rotatedRect.center = oldCenter
    # now draw it on screen
    surface.blit(rotatedShipImage, rotatedRect)

def RotateShipCW():
    global shipRotation
    shipRotation = shipRotation + SHIP_ROTATION_AMOUNT
    # handle wrapping of rotation value
    if (shipRotation > 360):
        shipRotation = 360 - shipRotation


def RotateShipCCW():
    global shipRotation
    shipRotation = shipRotation - SHIP_ROTATION_AMOUNT
    # handle wrapping of rotation value
    if (shipRotation < 0):
        shipRotation = 360 + shipRotation
