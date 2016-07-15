import pygame, sys
from centipedehead import CentipedeHead
from centipedebody import CentipedeBody

segmentDistance = 20

class Centipede(pygame.sprite.Group):

    centipedeSegmentList = []

    def __init__(self, speed, pos, width, height, length):
        self.centipedeSegmentList.append(CentipedeHead(speed, pos, width, height))

        nextX, nextY = pos
        deltaPos = -1*speed[0]*segmentDistance
        nextX += deltaPos

        for i in range(1, length+1):
            self.centipedeSegmentList.append(CentipedeBody(speed, [nextX, nextY], width, height))
            nextX += deltaPos

        super(Centipede,self).__init__(self.centipedeSegmentList)
