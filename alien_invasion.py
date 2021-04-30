import pygame
import math
import random
from pygame import mixer

## initialize the pygame
pygame.init()

## set screen
screen = pygame.display.set_mode((801,601))
### background
background = pygame.image.load("background 601.jpg")
### background music
mixer.music.load("background.wav")
mixer.music.play(-1)

pygame.display.set_caption("Space Invadar")

icon  = pygame.image.load("C:\\Users\\Md Mahadi hassan\\Downloads\\ufo.png")
pygame.display.set_icon(icon)

### player
playerImg = pygame.image.load("C:\\Users\\Md Mahadi hassan\\Downloads\\ufo.png")
playerX = 370
playerY = 480
playerX_change = 0
#enemy
## then add [] for multiple enemies
enemyImg =[]
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
number_of_enemy = 6
for i in range(number_of_enemy):
    enemyImg.append(pygame.image.load("C:\\Users\\Md Mahadi hassan\\Downloads\\mh.png"))
    enemyX.append(random.randint(0, 800))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(0.3)
    enemyY_change.append(10)



#bullet
### ready _i can not see the bullet is moving in screen
##fire the bullet is corently moving
bulletImg = pygame.image.load("bullet.png")
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change =1
bullet_state = "ready"





#collosion
def Iscollosion(enemyX,enemyY,bulletX,bulletY):
    distance = math.sqrt(math.pow(enemyX-bulletX,2)) + (math.pow(enemyY-bulletY,2))
    if distance < 27:
        return True
    else:
        return False
##Score
score_value =  int(0)
font = pygame.font.Font("freesansbold.ttf",33)
textX=10
textY=10
## gameover
over_list = pygame.font.Font("freesansbold.ttf",64)


def game_over_text ():
    over_text = over_list.render("Game Over",True,[255,255,255])
    screen.blit(over_text, (200,250))


def show_score(x,y):
    score =font.render("Score: " + str(score_value),True,[255,255,255])
    screen.blit(score,(x,y))




## blit means draw
def player(x,y):
    screen.blit(playerImg,(x,y))
def enemy(x,y,i):
    screen.blit(enemyImg[i],(x,y))
def fire_bullet(x,y):
    global bullet_state
    bullet_state = "Fire"
    screen.blit(bulletImg,(x+16,y+10))


### game loop
### kichu likte ba diplay te show korte caile while loop ar moddhai korte hobe
running = True
while running:
    ## RGB red green blue
    screen.fill((0, 0, 0))
    screen.blit(background,(0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        ## if key strok is pressed check it in right or left
        ####  keydown mane kono buttom a press korle
        ### keyup pres charar porer obosta
        if event.type == pygame.KEYDOWN:


            if event.key == pygame.K_LEFT:
                playerX_change = -0.5

            if event.key == pygame.K_RIGHT:
                playerX_change = 0.5

            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    bullet_sound = mixer.Sound("laser.wav")
                    bullet_sound.play()
                    bulletX = playerX
                    fire_bullet(bulletX, playerY)



        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0


   ### PLAYER MOVING LIMIT
    playerX += playerX_change
    if playerX <= 0 :
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    ### ENEMY MOVING LIMIT
    for i in range(number_of_enemy):
        ## game over
        if enemyY[i]>200:
            for j in range(number_of_enemy):
                enemyY[j] >2000
            game_over_text()
            break


        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = 0.2
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736:
            enemyX_change[i] = -0.2
            enemyY[i] += enemyY_change[i]
        ## collision
        collosion = Iscollosion(enemyX[i], enemyY[i], bulletX, bulletY)
        if collosion:
            explotion_sound = mixer.Sound("explosion.wav")
            explotion_sound.play()
            bulletY = 480
            bullet_state = "ready"
            score_value += 1
            enemyX[i] = random.randint(0, 735)
            enemyY[i] = random.randint(50, 150)
        enemy(enemyX[i], enemyY[i], i) 


    # bullet movement

    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"
    if bullet_state is "Fire":
        fire_bullet(bulletX,bulletY)
        bulletY -= bulletY_change





    player(playerX,playerY)
    show_score(textX,textY)

    pygame.display.update()