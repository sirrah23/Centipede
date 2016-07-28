import pygame, sys

class Mushroom(pygame.sprite.Sprite):

    def __init__(self, pos):
        super(Mushroom,self).__init__()
        self.image = pygame.image.load("./images/mushroom.png")
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]

    def update(self):
        pass
