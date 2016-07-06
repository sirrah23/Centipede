from segment import Segment
import pygame,sys

class CentipedeHead(Segment):

    def __init__(self,speed, pos, width, height):
        image = "./images/centipede_head.png"
        Segment.__init__(self,speed,image,pos,width,height)
