from segment import Segment
import pygame,sys

class CentipedeBody(Segment):

    def __init__(self,speed, pos, width, height):
        image = "./images/centipede_body.png"
        Segment.__init__(self,speed,image,pos,width,height)
