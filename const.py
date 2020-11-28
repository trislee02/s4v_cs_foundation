import pygame as pg 
import os

FPS = 60
WIDTH, HEIGHT = 1200, 670
PLAYER_WIDTH, PLAYER_HEIGHT = 70, 146
DOOR_CLOSED_WIDTH, DOOR_CLOSED_HEIGHT = 90, 155
DOOR_OPENED_WIDTH, DOOR_OPENED_HEIGHT = 150, 175
GROUND1_WIDTH, GROUND1_HEIGHT = WIDTH, 20
GROUND2_WIDTH, GROUND2_HEIGHT = 120, 20

GROUND_COLOR_DARK_BLUE = (90,112,158)
GROUND_COLOR_GRAY = (74,90,113)

BG0 = pg.transform.scale(pg.image.load(os.path.join("assets","background.png")),(WIDTH,HEIGHT))
BG1 = pg.transform.scale(pg.image.load(os.path.join("assets","background1.png")),(WIDTH,HEIGHT))
PLAYER_IMG = pg.transform.scale(pg.image.load(os.path.join("assets","trau.png")),(PLAYER_WIDTH, PLAYER_HEIGHT))
PLAYER_VELOCITY = 5

OPEN_DOOR_IMG = pg.transform.scale(pg.image.load(os.path.join("assets","opened_door.png")), (DOOR_OPENED_WIDTH, DOOR_OPENED_HEIGHT))
CLOSE_DOOR_IMG = pg.transform.scale(pg.image.load(os.path.join("assets","closed_door.png")), (DOOR_CLOSED_WIDTH, DOOR_CLOSED_HEIGHT))

GROUND1 = pg.transform.scale(pg.image.load(os.path.join("assets","ground1.png")),(GROUND1_WIDTH, GROUND1_HEIGHT))
GROUND2 = pg.transform.scale(pg.image.load(os.path.join("assets","ground2.png")),(GROUND2_WIDTH, GROUND2_HEIGHT))

#Touch ground states
TOUCH_GROUND_ABOVE = 1
TOUCH_GROUND_BELOW = 2
TOUCH_GROUND_LEFT = 3
TOUCH_GROUND_RIGHT = 4

CONVERSATION_STATE = 0
RUN_CHALLENGE_STATE = 1
FINISH_STATE = 2
#initialize pygame
pg.init()
font = pg.font.SysFont("comicsans", 50)