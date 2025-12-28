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
num_of_enemies=6

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load("C:\\Users\\EWEME ONUWA FAITH\\OneDrive\\Documents\\python codingal\\lesson 25\\lesson 29\\lesson 30\\lesson 33\\lesson 34\\enemy.png"))
    enemyx.append(random.randint(0, SCREEN_WIDTH - 64))
    enemyy.append(random.randint(ENEMY_START_Y_MIN,ENEMY_START_Y_MAX))
    enemyx_change.append(ENEMY_SPEED_X)
    enemyy_change.append(ENEMY_SPEED_Y)
    
bulletImg=pygame.image.load("C:\\Users\\EWEME ONUWA FAITH\\OneDrive\\Documents\\python codingal\\lesson 25\\lesson 29\\lesson 30\\lesson 33\\lesson 34\\bullet.png")
bulletx=0
bullety=PLAYER_START_Y
bulletx_change=0
bullety_change=BULLET_SPEED_Y
bullet_state="ready"

score_value=0
font=pygame.font.Font("freesansbold.ttf",32)
textx=10
texty=10
over_font=pygame.font.Font("freesansbold.ttf",64)

def show_score(x,y):
    score=font.render("Score: "+str(score_value),True,(255,255,255))
    screen.blit(score,(x,y))
    
    def game_over_text():
        over_text=over_font.render("GAME OVER",True,(255,255,255))
        screen.blit(over_text,(200,250))
        def game_over_text():
            over_text=over_font.render("GAME OVER",True,(255,255,255))
            screen.blit(over_text,(200,250))
            
def player(x,y):
    screen.blit(playerImg,(x,y))
    def enemy(x,y):
        screen.blit(enemyImg[i],(x,y))
        
def fire_bullet(x,y):
    global bullet_state
    bullet_state="fire"
    screen.blit(bulletImg,(x+16,y+10))
    
    def is_Collision(enemyx,enemyy,bulletx,bullety):
        distance=math.sqrt((math.pow(enemyx-bulletx,2))+(math.pow(enemyy-bullety,2)))
        distance<COLLISION_DISTANCE
    running= True
    while running:
        screen.fill((0,0,0))
        screen.blit(background,(0,0))
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    playerx_change=-5
                if event.key==pygame.K_RIGHT:
                    playerx_change=5
                if event.key==pygame.K_SPACE:
                    if bullet_state=="ready":
                        bulletx=playerx
                        fire_bullet(bulletx,bullety)
            if event.type==pygame.KEYUP:
                if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                    playerx_change=0
        playerx+=playerx_change
        playerx=max(0,min(playerx,SCREEN_WIDTH-64))
        if bullety<=0:
            bullety=PLAYER_START_Y
            bullet_state="ready"