from s4vsprite import s4vSprite

class Player(s4vSprite):
    def __init__(self,x,y,img):
        #construction
        super().__init__(x,y,img)
        #set states
        self.isJump = False
        self.isOnGround = True
        #set jump count
        self.jumpCount = 20
    
    def move(self,window):
        if self.isJump: #Checking for jumping
            self.isOnGround = False
            if self.jumpCount >= -20:
                neg = 1
                if self.jumpCount < 0:
                    neg = -1
                self.y -= 0.07*(self.jumpCount ** 2) * 1.3 * neg
                self.jumpCount -= 1
            else:
                self.isJump = False
                self.jumpCount = 20
                
        self.draw(window)
        
        
    def isTouch(self, _object):     #Return True if player touches AN object
        s_width, s_height = self.img.get_width(), self.img.get_height()
        o_x1, o_y1 = _object.x, _object.y        
        o_x2, o_y2 = o_x1 + _object.img.get_width(), o_y1 + _object.img.get_height()
        if ((self.x >= o_x1) and (self.y >= o_y1) and (self.x <= o_x2) and (self.y <= o_y2)):
            return True
        if ((self.x + s_width >= o_x1) and (self.y >= o_y1) and (self.x + s_width <= o_x2) and (self.y <= o_y2)):
            return True
        if ((self.x >= o_x1) and (self.y + s_height >= o_y1) and (self.x <= o_x2) and (self.y + s_height <= o_y2)):
            return True
        if ((self.x + s_width >= o_x1) and (self.y + s_height >= o_y1) and (self.x + s_width <= o_x2) and (self.y + s_height <= o_y2)):
            return True
        if (((self.x >= o_x1) and (self.x <= o_x2)) or ((self.x + s_width>= o_x1) and (self.x + s_width <= o_x2))) and ((self.y <= o_y1) and (self.y + s_height >= o_y2)):
            return True
        if (self.x <= o_x1) and (self.x + s_width >= o_x2) and (self.y <= o_y1) and (self.y + s_height >= o_y2):
            return True
        return False
    
    def isTouchObjects(self, _objects):  #Return Object, differentiate of Object and self in 4 aspects
        
        for obj in _objects:
            if self.isTouch(obj):
                return (obj, self.y - obj.y - obj.img.get_height(), obj.y - self.y - self.img.get_height(), obj.x - self.x - self.img.get_width(), self.x - obj.x - obj.img.get_width())
        return (None, 0,0,0,0)
        
    def jump(self):
        if self.isOnGround: #Player need to be on grounds to jump 
            self.isJump = True
    
        
