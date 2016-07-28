import pygame, sys
from centipedebody import CentipedeBody
from mushroom import Mushroom

segmentDistance = 20

class Centipede(pygame.sprite.Group):

    centipedeSegmentList = []

    def __init__(self, speed, pos, width, height, length):
        nextX, nextY = pos
        deltaPos = -1*speed[0]*segmentDistance
        nextX += deltaPos

        for i in range(length):
            self.centipedeSegmentList.append(CentipedeBody(speed, [nextX, nextY], width, height))
            nextX += deltaPos

        super(Centipede,self).__init__(self.centipedeSegmentList)

    def damage(self,segmentsHit):
        '''Detects which segment of the centipede was hit and calls split on that position in the centipede.'''
        if len(segmentsHit) <= 0:
            return None

        segmentToDetect = segmentsHit[0]

        for pos,segment in enumerate(self.centipedeSegmentList):
            if segment == segmentToDetect:
                freshMushroom = self.split(pos)
                return freshMushroom

    def split(self, pos):
        '''If the centipede was shot in the head or tail then erase that segment. If the
        centipede was shot somewhere in the middle then create a new mushroom at that
        position.
        '''
        freshMushroom = None
        segmentToDelete = self.centipedeSegmentList[pos]
        if pos > 0 and pos < len(self.centipedeSegmentList) - 1:
            freshMushroom = Mushroom(segmentToDelete.rect.center)
        self.centipedeSegmentList.remove(segmentToDelete)
        segmentToDelete.kill()
        return freshMushroom

