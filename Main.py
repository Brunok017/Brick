import pygame
import sys
import os
from pygame.locals import *
import asyncio

pygame.init()

#Score
Score = 0
game_font = pygame.font.Font("freesansbold.ttf", 15)
Big_font = pygame.font.Font("freesansbold.ttf", 60)
#Colors
back = (40,19,13)
red = (255, 51, 51)
white = (255,255,255)
orange = (255,102,51)
yellow = (255,192,51)
green = (151,255,51)
teal = (51,255,137)
ballcol = white

x = 5
y = 20
spacer = 20
lose = False
win = False
if Score == 60:
    win = True
#window
clock = pygame.time.Clock()
winw, winh = 605, 400
win = pygame.display.set_mode((winw,winh))
pygame.display.set_caption("Brick Breaker")

bricks = []
class brick:
    
    def __init__(self, color, pos, size, Broken):
        self.color = color
        self.pos = pos
        self.size = size
        self.Broken = Broken
    
    def draw(self):
        self.rect=pygame.draw.rect(win, self.color,(self.pos,self.size))
    def ballcol(self):
        global ballspy
        




    
#Row 1
for count in range(10):
    rectcol = red
    rectpos = (x, y)
    rectsize = (55,15)
    rectbroken = False
    bricks.append(brick(rectcol, rectpos, rectsize, rectbroken))
    x +=60
x = 5
y += spacer
#row 2
for count in range (10):
    rectcol = orange
    rectpos= (x,y)
    rectsize = (55,15)
    rectbroken = False
    bricks.append(brick(rectcol, rectpos, rectsize, rectbroken))
    x +=60

#row 3
x = 5
y += spacer
for count in range (10):
    rectcol = yellow
    rectpos= (x,y)
    rectsize = (55,15)
    rectbroken = False
    bricks.append(brick(rectcol, rectpos, rectsize, rectbroken))
    x +=60
#row 4
x = 5
y += spacer
for count in range (10):
    rectcol = green
    rectpos= (x,y)
    rectsize = (55,15)
    rectbroken = False
    bricks.append(brick(rectcol, rectpos, rectsize, rectbroken))
    x +=60   
#row 5
x = 5
y += spacer
for count in range (10):
    rectcol = teal
    rectpos= (x,y)
    rectsize = (55,15)
    rectbroken = False
    bricks.append(brick(rectcol, rectpos, rectsize, rectbroken))
    x +=60
#row 6
x = 5
y += spacer
for count in range (10):
    rectcol = white
    rectpos= (x,y)
    rectsize = (55,15)
    rectbroken = False
    bricks.append(brick(rectcol, rectpos, rectsize, rectbroken))
    x +=60
def ballmove():
    global ballspx
    global ballspy
    global speedchange
    global brickbroken
    global Score
    global lose
    ball.x += ballspx
    ball.y += ballspy
    if ball.right >= winw or ball.left <= 0:
        ballspx *= -1
    if ball.top <= 0:
        ballspy *= -1
    if ball.bottom >= winh:
        lose = True
    if ball.colliderect(player):
        ballspy *= speedchange
    
        
        
    

#Vars
ballspx = 2
ballspy = 2
px = 260
py = 390
playervel = 0
speedchange = -1.015
brickbroken = False
#Shapes
player = pygame.Rect(px, py, 80, 10)
ball = pygame.Rect(280, 200, 13, 13)




#main loop
run = True

async def main():
    global run
    global playervel
    global Score
    global ballcol
    global ballspy
    global ballspx
    while run:
        
        pygame.time.delay(10)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    playervel += 5
                if event.key == pygame.K_LEFT:
                    playervel -= 5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    playervel -= 5    
                if event.key == pygame.K_LEFT:
                    playervel += 5  
        player.x += playervel
        if player.right >= winw:
            player.right = winw
        if player.left <= 0:
            player.left = 0
        
        
        for brick in bricks:
            brick.draw()
        for brick in bricks[:]:
            if ball.colliderect(brick):
                bricks.remove(brick)
                ballspy *= speedchange
                Score += 1
        #fonts
        scory = game_font.render("SCORE:", True, white)
        playscore = game_font.render(f"{Score}",True, yellow)
        YouLose = Big_font.render("YOU LOSE",True,red)
        YouWin = Big_font.render("YOU WIN", True, yellow)
        if lose == True:
            win.blit(YouLose,(150,200))
        if Score == 60:
            win.blit(YouWin,(175,200))
            ballspy = 0
            ballspx = 0
            ballcol = back
        win.blit(scory,(250,3))
        win.blit(playscore,(315,3))
        ballmove()
        pygame.draw.ellipse(win, ballcol, ball)
        pygame.draw.rect(win, white, player)
        pygame.display.update()
        clock.tick(60)
        win.fill(back)
        await asyncio.sleep(0)

asyncio.run(main())