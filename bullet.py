# holds the code for bullets, bullets are kept in a list
__author__ = 'Mus'

# need math library functions
import math

# bullet constant values
BULLET_SPEED = 2

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
    bulletPosX.insert(0, x)
    bulletPosY.insert(0, y)
    rect = game.Rect(x-(BULLET_WIDTH/2), y-(BULLET_HEIGHT/2), BULLET_WIDTH, BULLET_HEIGHT)
    bulletRect.insert(0, rect)

    bulletDirX.insert(0, math.cos(math.radians(rotation)))
    bulletDirY.insert(0, -math.sin(math.radians(rotation)))    # flip Y
    bulletSound.play()

def MoveBullets():
    global bulletRect, bulletPosX, bulletPosY
    for i in range(numBullets):
        bulletPosX[i] += bulletDirX[i] * BULLET_SPEED
        bulletPosY[i] += bulletDirY[i] * BULLET_SPEED
        bulletRect[i].center = (bulletPosX[i], bulletPosY[i])

def DrawBullet(surface):
    MoveBullets()
    for rect in bulletRect:
        surface.blit(bulletImage, rect)
