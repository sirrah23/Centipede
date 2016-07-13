import pygame,sys

class Segment(pygame.sprite.Sprite):

    def __init__(self, speed, image, pos, width, height):
        super(Segment,self).__init__()
        self.speed = speed
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.screenWidth = width
        self.screenHeight = height
        # Start with moving down
        self.verticalDirection = 10
        # How fast do the centipede segments move left/right
        self.horizontalSpeed = 1

    def computeNewSpeed(self):
        #If the centipede is just moved up or down then reset that
        if self.speed[1] != 0:
            return [self.speed[0],0]
        newSpeed = []
        #If centipede hits left wall, start moving right
        if self.rect.left <= 0:
            newSpeed=[self.horizontalSpeed,self.verticalDirection]
        #If centipede hits right wall, start moving left
        elif self.rect.right >= self.screenWidth:
            newSpeed=[-self.horizontalSpeed,self.verticalDirection]

        # If centipede hits top or bottom then start going the other way
        if (self.rect.top <= 0 and self.verticalDirection < 0) or (self.rect.bottom >= self.screenHeight and self.verticalDirection > 0):
            self.verticalDirection *= -1
        #Return the current speed of the centipede
        if newSpeed == []:
            return self.speed
        else:
            return newSpeed

    def updateSpeed(self, speed):
        self.speed = speed

    def move(self):
        newSpeed = self.computeNewSpeed()
        # We changed directions
        if newSpeed[0] != self.speed[0]:
            self.rotate()
        self.updateSpeed(newSpeed)
        self.rect = self.rect.move(self.speed)

    # After a centipede segment hits the wall it needs to "turn around" in order to go the other way.
    # This method rotates the rect object in the appropriate direction.
    def rotate(self):
        oldCenter = self.rect.center
        # degrees * direction
        angle = 180
        self.image = pygame.transform.rotate(self.image, angle)
        # Get new rect from rotated image
        self.rect = self.image.get_rect()
        self.rect.center = oldCenter

    def withinScreen(self):
        return True
