import pygame, sys

class Laser(pygame.sprite.Sprite):

    def __init__(self, speed, image, pos, width, height):
        super(Laser,self).__init__()
        self.speed = speed
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.screenWidth = width
        self.screenHeight = height

    def move(self):
        self.rect = self.rect.move(self.speed)

    def withinScreen(self):
        return self.rect.x >= 0 and self.rect.x <= self.screenWidth and self.rect.y >= 0 and self.rect.y <= self.screenHeight
