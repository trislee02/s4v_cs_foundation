from s4vsprite import s4vSprite

class s4vObject(s4vSprite):
    def __init__(self,x,y,img):
        #construction
        super().__init__(x,y,img)
    
    def changeAppearance(self,img):
        self.img = img
    
    def show(self,window):
        self.draw(window)
        
    
        