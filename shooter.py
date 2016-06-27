import pygame,sys

class Shooter:

    def __init__(self, speed, image, pos):
        self.speed = speed
        self.image = pygame.image.load(image)
        print self.image
        self.rect = self.image.get_rect()

    def updateSpeed(self, speed):
        self.speed = speed

    def moveRect(self):
        print self.speed
        self.rect = self.rect.move(self.speed)
