from laser import Laser
import pygame,sys

class Shooter:

    def __init__(self, speed, image, pos, width, height):
        self.speed = speed
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.screenWidth = width
        self.screenHeight = height

    def updateSpeed(self, speed):
        self.speed = speed

    def move(self):
        self.rect = self.rect.move(self.speed)
        newSpeed = list(self.speed)
        # Can't move off the screen
        if self.rect.left < 0 or self.rect.right > self.screenWidth:
            newSpeed[0] = 0
        if self.rect.top < 0 or self.rect.bottom > self.screenHeight:
            newSpeed[1] = 0
        self.updateSpeed(newSpeed)

    # Creates a new laser object that will fly across the screen
    def shoot(self):
        laserSpeed = [0,-1] #fly vertically up the screen
        laserImage = "./images/laser.png"
        laserPos = [self.rect.x,self.rect.y]
        laser = Laser(laserSpeed, laserImage, laserPos, self.screenWidth, self.screenHeight)
        return laser
