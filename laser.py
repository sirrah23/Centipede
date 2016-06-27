import pygame, sys

class Laser:

    def __init__(self, speed, image, pos, width, height):
        self.speed = speed
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.screenWidth = width
        self.screenHeight = height

    def move(self):
        self.rect = self.rect.move(self.speed)
