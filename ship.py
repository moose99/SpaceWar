# contains code for the ship object
__author__ = 'Mus'

# need math library functions
import math

# initialize variables to hold the ships rectangle and image and sounds
shipRect = None
shipImage = None
engineSound = None

# ship constant vars: size, rotation amount
SHIP_WIDTH = 30
SHIP_HEIGHT = 30
SHIP_ROTATION_AMOUNT = 4
SHIP_SPEED_AMOUNT = .1
SHIP_DRAG_AMOUNT = 0.005
SHIP_MAX_SPEED = 5

# init vars to hold velocity, speed, position and rotation...
shipRotation = 0    # goes from 0 to 360
shipPosX = 250
shipPosY = 250
shipVelX = 0
shipVelY = 0
shipSpeed = 0

# func to create the ship
def SetupShip(game):
    # use 'global' to indicate that we are changing the shipRect/shipImage vars declared outside the function
    global shipRect
    global shipImage
    global engineSound
    shipRect = game.Rect(shipPosX-(SHIP_WIDTH/2), shipPosY-(SHIP_HEIGHT/2), SHIP_WIDTH, SHIP_HEIGHT)
    shipImage = game.image.load('assets/rocketship.png')
    engineSound = game.mixer.Sound('assets/engine_2.wav')

# draws the ship on the surface provided
def DrawShip(surface, game):
    # first apply ship rotation
    rotatedShipImage = game.transform.rotate(shipImage, shipRotation)
    rotatedRect = rotatedShipImage.get_rect()
    rotatedRect.center = shipRect.center    # use original image center, so always rotates around the same center

    # now apply ship translation
    rotatedRect.center = (shipPosX, shipPosY)

    # now draw it on screen
    surface.blit(rotatedShipImage, rotatedRect)

# change ship rotation
def RotateShipCCW():
    global shipRotation
    shipRotation += SHIP_ROTATION_AMOUNT
    # handle wrapping of rotation value
    if (shipRotation > 360):
        shipRotation = 360 - shipRotation

# change ship rotation
def RotateShipCW():
    global shipRotation
    shipRotation -= SHIP_ROTATION_AMOUNT
    # handle wrapping of rotation value
    if (shipRotation < 0):
        shipRotation = 360 + shipRotation

# change ship speed
def MoveShip(thruster):
    global shipSpeed
    # increase speed
    if (thruster):
        shipSpeed += SHIP_SPEED_AMOUNT
        # clamp speed to maximum
        if (shipSpeed > SHIP_MAX_SPEED):
            shipSpeed = SHIP_MAX_SPEED
    # else decrease speed using drag
    else:
        shipSpeed -= SHIP_DRAG_AMOUNT
        if (shipSpeed < 0):
            shipSpeed = 0

def TransformShip(surface, turnCCW, turnCW, thruster):
    # we'll be changing these globals
    global shipVelX, shipVelY, shipPosX, shipPosY
    # handle rotation
    if (turnCCW):
        RotateShipCCW()
    elif turnCW:
        RotateShipCW()

    # handle translation
    MoveShip(thruster)

    # change velocity
    if (thruster):
        # find the current direction vector
        shipDirX = math.cos(math.radians(shipRotation))
        shipDirY = -math.sin(math.radians(shipRotation))    # flip Y

        # change velocity using current direction
        shipVelX += shipDirX
        shipVelY += shipDirY

    # normalize velocity
    length = math.sqrt(shipVelX*shipVelX + shipVelY*shipVelY)  # hypotenuse
    if (length > 0):
        shipVelX /= length
        shipVelY /= length
    else:
        shipVelX = 0
        shipVelY = 0

    # update position based on current velocity and speed
    shipPosX += shipVelX * shipSpeed
    shipPosY += shipVelY * shipSpeed

    # wrap position
    if (shipPosX >= surface.get_width()):
        shipPosX -= surface.get_width()
    if (shipPosY >= surface.get_height()):
        shipPosY -= surface.get_height()

    if (shipPosX < 0):
        shipPosX = surface.get_width() + shipPosX
    if (shipPosY < 0):
        shipPosY = surface.get_height() + shipPosY
