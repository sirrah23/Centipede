import pygame,sys

class Segment:

    def __init__(self, speed, image, pos, width, height):
        self.speed = speed
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.screenWidth = width
        self.screenHeight = height
        #Start with moving down
        self.verticalDirection = 10
        #How fast do the centipede segments move left/right
        self.horizontalSpeed = 2

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
        self.updateSpeed(newSpeed)
        self.rect = self.rect.move(self.speed)

    def withinScreen(self):
        return True
