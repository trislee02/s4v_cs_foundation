import pygame as pg 
import os
import time
import random
from const import *
from player import Player
from door import Door
from ground import Ground
from challenge1 import Challenge1
from challenge2 import Challenge2

#create screen
WIN = pg.display.set_mode((WIDTH,HEIGHT))
pg.display.set_caption("Kim Tu Thap")

# def isTouchGround(_player):
#     for ground in Ground.grounds:
#         if _player.isTouch(ground):
#             return (ground, _player.y - ground.y - ground.img.get_height(), ground.y - _player.y - _player.img.get_height(), ground.x - _player.x - _player.img.get_width(), _player.x - ground.x - ground.img.get_width())
#     return (ground, 0,0,0,0)

#main function
def main():
    run = True
    clock = pg.time.Clock()
    #set score
    score = 0
    #background position
    bg_x = 0
    #challenge number
    challenge_num = 0
    #create player
    player = Player(20,20,PLAYER_IMG)
    #create doors
    door1 = Door(250,400,CLOSE_DOOR_IMG,1)
    door2 = Door(500,400,CLOSE_DOOR_IMG,2)
    door3 = Door(750,400,CLOSE_DOOR_IMG,3)
    door4 = Door(1000,400,CLOSE_DOOR_IMG,4)
    door5 = Door(375,200,CLOSE_DOOR_IMG,5)
    door6 = Door(625,200,CLOSE_DOOR_IMG,6)
    door7 = Door(875,200,CLOSE_DOOR_IMG,7)
    ground1 = Ground(0,560,GROUND1)
    ground2 = Ground(355,355,GROUND2)
    ground3 = Ground(605,355,GROUND2)
    ground4 = Ground(855,355,GROUND2)
    # add random an enemy
    challenges = []
    challenges.append(Challenge1())
    challenges.append(Challenge2())
    
    grounds = []
    grounds.append(ground1)
    grounds.append(ground2)
    grounds.append(ground3)
    grounds.append(ground4)
    
    doors = []
    doors.append(door1)
    doors.append(door2)
    doors.append(door3)
    doors.append(door4)
    doors.append(door5)
    doors.append(door6)
    doors.append(door7)
    isReturnPressed = False
    # clean all enemy out of window
    def cleanEnemy(): # NO NEED FOR THIS
        pass
        #nonlocal enemies
        #enemies = list(filter(lambda enemy: enemy.y < HEIGHT,enemies))

    # main function to redraw all objects
    def redraw_window():
        if challenge_num == 0:
            WIN.blit(BG0,(bg_x,0))
            for ground in grounds:
                ground.move(WIN)
            for door in doors:
                door.show(WIN)
            player.move(WIN)
        
        elif challenge_num == 1:
            WIN.blit(BG1,(0,0))
            challenges[0].doChallenge(WIN)
            
        elif challenge_num == 2:
            WIN.blit(BG1,(0,0))
            challenges[1].doChallenge(WIN)
    #
    #
    # ADD MORE CHALLENGE HERE
    #
    #
    #     addEnemy()
    #     #draw score and health
    #     score_text = main_font.render(f"score: {score}", 1, (255, 255, 255))
    #     hp_text = main_font.render(f"health: {player.health}", 1, (255, 255, 255))

    #     WIN.blit(score_text, (10, 10))
    #     WIN.blit(hp_text, (WIDTH - hp_text.get_width() - 10, 10))

    #     for enemy in enemies:
    #         enemy.move(WIN)
    #     #cleanEnemy()
        pg.display.update()

    while run:
        clock.tick(FPS)

        redraw_window()
        pre_x = player.x
        pre_y = player.y
        
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
        keys = pg.key.get_pressed()
        if challenge_num == 0:
            if keys[pg.K_LEFT] and player.x - PLAYER_VELOCITY > 0:
                player.x -= PLAYER_VELOCITY
            if keys[pg.K_RIGHT] and player.x + PLAYER_VELOCITY < WIDTH-PLAYER_WIDTH:
                player.x += PLAYER_VELOCITY
                #bg_x -= 10
            if keys[pg.K_SPACE]:
                player.jump()
            if keys[pg.K_RETURN]:            
                if not(isReturnPressed):
                    _door, tAbove, tBelow, tLeft, tRight = player.isTouchObjects(doors)
                    if (abs(tAbove - tBelow) <= 100) and (abs(tLeft - tRight) <= 100):
                        print('Door',tAbove, tBelow, tLeft, tRight)
                        if (_door.isOpened):
                            _door.closeIt()
                        else:
                            _door.openIt()
                            challenge_num = _door.challengeId #Update challenge_num when player enter a room
                isReturnPressed = True
            else:
                isReturnPressed = False            
        
        #Check player touches grounds
        _ground, tAbove, tBelow, tLeft, tRight = player.isTouchObjects(grounds)
        print(tAbove, tBelow, tLeft, tRight)
        if not((tAbove, tBelow, tLeft, tRight) == (0,0,0,0)):        
            _g_x1, _g_y1 = _ground.x, _ground.y
            _g_x2, _g_y2 = _ground.x + _ground.img.get_width(), _ground.y + _ground.img.get_height()
            p_width, p_height = player.img.get_width(), player.img.get_height()
                                
            if ((pre_x >= _g_x1) and (pre_x <= _g_x2)) or ((pre_x + p_width >= _g_x1) and (pre_x + p_width >= _g_x1)):
                if (tAbove > tBelow): #Touch a ground above
                    player.y = _g_y2 + 2
                    player.jumpCount = 0
                else:                 #Touch a ground below
                    player.y = _g_y1 - p_height - 2
                    player.isJump = False
                    player.jumpCount = 20
                    player.isOnGround = True
            else:
                if (tLeft > tRight):  #Touch a ground to the right
                    player.x = _g_x1 - p_width - 2
                else:                 #Touch a ground to the left
                    player.x = _g_x2 + 2
        elif not(player.isJump):
            player.y += 30
            temp, a, b, c, d = player.isTouchObjects(grounds)
            if not(a > b or b == 0):
                player.y -= 30
                player.y += temp.y - player.y - player.img.get_height() - 2
                player.isOnGround = True
                
main()
