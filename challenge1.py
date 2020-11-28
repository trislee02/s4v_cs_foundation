import pygame as pg
import time
from challenge import Challenge
from playernpc import PlayerNPC
from ainpc import AiNPC
from const import *
red = (255,0,0)
white = (255,255,255)
class Challenge1(Challenge):    
    def __init__(self):
        super().__init__()
        self.count = 0
        self.current_count = 0
        self.count_down = 20
        self.state = CONVERSATION_STATE
        self.player_npc = PlayerNPC()
        self.ai = AiNPC()
        self.turn = 0
        

    def doChallenge(self, window):
        if self.state == CONVERSATION_STATE:
            if self.player_npc.isFinishedTalking() and self.ai.isFinishedTalking():
                
                self.state = RUN_CHALLENGE_STATE
            elif self.turn == 0:
                if self.ai.talk(window):
                    self.turn = 1
    
            else:
                if self.player_npc.talk(window):
                    self.turn = 0
                
        elif self.state == RUN_CHALLENGE_STATE:
            output = self.student_implementation(5)
            self.count = 25
            self.drawOutput(window,output)

    def drawOutput(self, window,output):
        width = 650
        height = 400
        x_a = 450
        y_a = 20
        level = len(output)
        margin = 5
        cube_size = (height - 20)//(level+margin)
        cube_initial_x = x_a + width//2-level*(cube_size+margin)-cube_size//2
        cube_initial_y = y_a + height-level*(cube_size+margin)-10
        pg.draw.rect(window, white, (450, 20, width, height))
        count = 0
        for row in range(len(output)):
            for col in range(len(output[row])):
                if output[row][col] == "*":
                    if self.current_count == self.count:
                        pg.draw.rect(window, red, (cube_initial_x+col*(cube_size+margin), cube_initial_y+row*(cube_size+margin), cube_size, cube_size))
                        self.ai.congrat(window)

                    elif self.current_count < self.count:
                        if count == self.current_count:
                            break
                        pg.draw.rect(window, red, (cube_initial_x+col*(cube_size+margin), cube_initial_y+row*(cube_size+margin), cube_size, cube_size))
                        count += 1

            if count == self.current_count:
                if self.count_down == 0:
                    self.current_count += 1
                    self.count_down = 20
                self.countDown()
                break

    def countDown(self):
        if self.count_down != 0:
            self.count_down -= 1


    #Hoc Sinh Implement 
    def student_implementation(self, level):
        result = []
        for i in range(level):
            row = ""
            for j in range(level-i):
                row += " "
            for j in range(i*1+1):
                row += "*"
            result.append(row)
        return result
                