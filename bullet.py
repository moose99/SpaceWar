# holds the code for bullets, bullets are kept in a list
__author__ = 'Mus'

# need math library functions
import math

# bullet constant values
BULLET_SPEED = 8

# initialize variables to hold the bullet rectangle and image
bulletRect = []
bulletImage = None
numBullets = 0
bulletPosX = []
bulletPosY = []
bulletDirX = []
bulletDirY = []
bulletSound = None

def SetupBullet(game):
    global bulletImage, bulletSound
    bulletImage = game.image.load('assets/circle.png')
    bulletSound = game.mixer.Sound('assets/tx0_fire1.wav')

# func to create the bullet
def FireBullet(game, x, y, rotation):
    # use 'global' to indicate that we are changing the bulletRect/bulletImage vars declared outside the function
    global bulletRect, bulletImage, numBullets, bulletPosX, bulletPosY
    numBullets += 1
    BULLET_WIDTH = 8
    BULLET_HEIGHT = 8
    dirX = math.cos(math.radians(rotation))
    dirY = -math.sin(math.radians(rotation))
    x += dirX
    y += dirY
    bulletPosX.insert(0, x)
    bulletPosY.insert(0, y)
    rect = game.Rect(x-(BULLET_WIDTH/2), y-(BULLET_HEIGHT/2), BULLET_WIDTH, BULLET_HEIGHT)
    bulletRect.insert(0, rect)
    bulletDirX.insert(0, dirX)
    bulletDirY.insert(0, dirY)    # flip Y
    bulletSound.play()

def RemoveBullet(i):
    global numBullets
    del bulletPosX[i]
    del bulletPosY[i]
    del bulletRect[i]
    del bulletDirX[i]
    del bulletDirY[i]
    numBullets -= 1

def MoveBullets(surface):
    global bulletRect, bulletPosX, bulletPosY
    i = numBullets-1
    while (i>=0):
        bulletPosX[i] += bulletDirX[i] * BULLET_SPEED
        bulletPosY[i] += bulletDirY[i] * BULLET_SPEED
        bulletRect[i].center = (bulletPosX[i], bulletPosY[i])
        if (bulletPosX[i] > surface.get_width() or bulletPosY[i] > surface.get_height() or bulletPosX[i] < 0 or bulletPosY[i] < 0):
            RemoveBullet(i)
        i -= 1

def DrawBullet(surface):
    MoveBullets(surface)
    for rect in bulletRect:
        surface.blit(bulletImage, rect)
