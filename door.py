from s4vobject import s4vObject
from const import *
class Door(s4vObject):
    isOpened = False
    challengeId = 0
    def __init__(self,x,y,img,challenge):
        #construction
        super().__init__(x,y,img)
        self.isOpened = False
        self.challengeId = challenge
    
    def openIt(self):
        self.changeAppearance(OPEN_DOOR_IMG)
        self.isOpened = True
    
    def closeIt(self):
        self.changeAppearance(CLOSE_DOOR_IMG)
        self.isOpened = False
