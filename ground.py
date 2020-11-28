from s4vobject import s4vObject
from const import *

class Ground(s4vObject):
    def __init__(self,x,y,img):
        #construction
        super().__init__(x,y,img)
    
    def move(self,window):
        self.draw(window)
