import math
import random
import pygame
SCREEN_WIDTH=800
SCREEN_HEIGHT=500
PLAYER_START_X=370
PLAYER_START_Y=380
ENEMY_START_Y_MIN=50
ENEMY_START_Y_MAX=150
ENEMY_SPEED_X=4
ENEMY_SPEED_Y=40
BULLET_SPEED_Y=10
COLLISION_DISTANCE=27
pygame.init()
screen=pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
background=pygame.image.load("C:\\Users\\EWEME ONUWA FAITH\\OneDrive\\Documents\\python codingal\\lesson 25\\lesson 29\\lesson 30\\lesson 33\\lesson 34\\bg.png")
pygame.display.set_caption("Space Invader")
icon=pygame.image.load("C:\\Users\\EWEME ONUWA FAITH\\OneDrive\\Documents\\python codingal\\lesson 25\\lesson 29\\lesson 30\\lesson 33\\lesson 34\\ufo.png")
pygame.display.set_icon(icon)
playerImg=pygame.image.load("C:\\Users\\EWEME ONUWA FAITH\\OneDrive\\Documents\\python codingal\\lesson 25\\lesson 29\\lesson 30\\lesson 33\\lesson 34\\player.png")
playerx=PLAYER_START_X
playery=PLAYER_START_Y
playerx_change=0

enemyImg=[]
enemyx=[]
enemyy=[]
enemyx_change=[]
enemyy_change=[]
enemyx_change=[]
enemyy_change=[]
num_of_enemies=6

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load("C:\Users\EWEME ONUWA FAITH\OneDrive\Documents\python codingal\lesson 25\lesson 29\lesson 30\lesson 33\lesson 34\enemy.png"))
    enemyx.append(random.randint(0, SCREEN_WIDTH - 64))
    enemyy.append(random.randint(ENEMY_START_Y_MIN,ENEMY_START_Y_MAX))
    enemyx_change.append(ENEMY_SPEED_X)
    enemyy_change.append(ENEMY_SPEED_Y)