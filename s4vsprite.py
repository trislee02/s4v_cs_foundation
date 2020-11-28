import pygame as pg 
import os
from math import sin, cos, radians
from const import *

#create collision function
def collide(obj1, obj2):
    offset_x = int(obj2.x - obj1.x)
    offset_y = int(obj2.y - obj1.y)
    return obj1.mask.overlap(obj2.mask, (offset_x, offset_y)) != None


class s4vSprite:
    def __init__(self,x,y,img=None):
        self.x = x
        self.y = y
        self.img = img 
        self.angle = 0
        self.mask = pg.mask.from_surface(self.img)

    def draw(self, window):
        window.blit(self.img,(self.x,self.y))

    def getAngle(self):
        return self.angle

    def setAngle(self,angle):
        self.angle = angle
        self.img = pg.transform.rotate(self.img,360-self.angle)

    def moveTo(self,x,y):
        self.x = x
        self.y = y 
    
    def moveForward(self,unit=5):
        self.x += sin(radians(self.angle))*unit 
        self.y -= cos(radians(self.angle))*unit

    def isCollidedWith(self, second_object):
        return collide(self, second_object)