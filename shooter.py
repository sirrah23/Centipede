from laser import Laser
import pygame,sys

class Shooter(pygame.sprite.Sprite):

    def __init__(self, speed, image, pos, width, height):
        super(Shooter,self).__init__()
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
        # Stop shooter from moving off of the screen
        if self.rect.left <= 0:
            self.rect.left = 0

        if self.rect.right >= self.screenWidth:
            self.rect.right = self.screenWidth

        if self.rect.top <= 0:
            self.rect.top = 0

        if self.rect.bottom >= self.screenHeight:
            self.rect.bottom = self.screenHeight

        self.updateSpeed(newSpeed)

    # Creates a new laser object that will fly across the screen
    def shoot(self):
        laserSpeed = [0,-1] #fly vertically up the screen
        laserImage = "./images/laser.png"
        laserPos = [self.rect.x,self.rect.y]
        laser = Laser(laserSpeed, laserImage, laserPos, self.screenWidth, self.screenHeight)
        return laser

    def withinScreen(self):
        return True
