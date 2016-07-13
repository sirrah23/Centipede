from laser import Laser
import pygame,sys

class Shooter(pygame.sprite.Sprite):

    def __init__(self, image, pos, width, height):
        super(Shooter,self).__init__()
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.screenWidth = width
        self.screenHeight = height

    def update(self, pressedKeys):

        # Move the shooter based on arrow keys were pressed
        if pressedKeys[pygame.K_UP]:
            self.rect.move_ip(0,-1)
        if pressedKeys[pygame.K_DOWN]:
            self.rect.move_ip(0,1)
        if pressedKeys[pygame.K_LEFT]:
            self.rect.move_ip(-1,0)
        if pressedKeys[pygame.K_RIGHT]:
            self.rect.move_ip(1,0)

        # Stop shooter from moving off of the screen
        if self.rect.left <= 0:
            self.rect.left = 0
        if self.rect.right >= self.screenWidth:
            self.rect.right = self.screenWidth
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= self.screenHeight:
            self.rect.bottom = self.screenHeight

    # Creates a new laser object that will fly across the screen
    def shoot(self):
        laserSpeed = [0,-1] #fly vertically up the screen
        laserImage = "./images/laser.png"
        laserPos = [self.rect.x,self.rect.y]
        laser = Laser(laserSpeed, laserImage, laserPos, self.screenWidth, self.screenHeight)
        return laser
