import pygame
import math
from Simulation import *
from Ball import *


pygame.init()
clock = pygame.time.Clock()

win_width = 1200
win_height = 600
factor = 10
run = True
temp = True
WHITE = (255, 255, 255) 
BLACK = (0, 0, 0) 
RED = (255, 0, 0) 
GREEN = (0, 255, 0) 
BLUE = (0, 0, 255) 
YELLOW = (255, 255, 0) 
LIGHTBLUE = (0, 155, 155) 
BROWN = (139,76,57) 
ORANGE = (255,128,0) 
DARKGREEN = (0,100,0)



sim.input()  
ball.calculations()



font = pygame.font.SysFont('comicsans', 50)
answer_time = font.render(f"Time in the air: {round(ball.time, 3)} seconds", 1, ORANGE)
answer_dist = font.render(f"Horizontal distance: {round(ball.h_distance, 3)} meters", 1, ORANGE)


    
table = pygame.Rect(0,(win_height-10*ball.height+10),200,win_height)
rDraw = pygame.draw.rect
lDraw = pygame.draw.line
win=pygame.display.set_mode((win_width,win_height))
while run:
    keys = pygame.key.get_pressed()
    pygame.time.delay(10)
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                

    
    
    pygame.draw.circle(win, DARKGREEN, (195,int(win_height-10*ball.height)), 10)
    rDraw(win, RED, table)
    
    font = pygame.font.SysFont('comicsans', 25)
    
    win.blit(font.render("0", 1, WHITE), (200,525))
    lDraw(win, BLUE, (200,600), (200,550))
    win.blit(font.render("10", 1, WHITE), (300,525))
    lDraw(win, BLUE, (300,600), (300,550))
    win.blit(font.render("20", 1, WHITE), (400,525))
    lDraw(win, BLUE, (400,600), (400,550))
    win.blit(font.render("30", 1, WHITE), (500,525))
    lDraw(win, BLUE, (500,600), (500,550))
    win.blit(font.render("40", 1, WHITE), (600,525))
    lDraw(win, BLUE, (600,600), (600,550))
    win.blit(font.render("50", 1, WHITE), (700,525))
    lDraw(win, BLUE, (700,600), (700,550))
    win.blit(font.render("60", 1, WHITE), (800,525))
    lDraw(win, BLUE, (800,600), (800,550))
    win.blit(font.render("70", 1, WHITE), (900,525))
    lDraw(win, BLUE, (900,600), (900,550))
    win.blit(font.render("80", 1, WHITE), (1000,525))
    lDraw(win, BLUE, (1000,600), (1000,550))
    win.blit(font.render("90", 1, WHITE), (1100,525))
    lDraw(win, BLUE, (1100,600), (1100,550))
    win.blit(font.render("100", 1, WHITE), (1175,525))
    lDraw(win, BLUE, (1199,600), (1199,550))
    
    win.blit(answer_time, (600,0))
    win.blit(answer_dist, (600,50))
    

    pygame.display.update()
    if temp:
        pygame.time.delay(2000)
        temp = False
    if (sim.val > 0) and not(sim.pause):         
        sim.equation(sim.counter)
        pygame.draw.rect(win, GREEN, (sim.counter, 600- sim.val, 1,1))
        sim.counter += 1
    if keys[pygame.K_a] and not(sim.pause):
        sim.pause = True
    if keys[pygame.K_d] and (sim.pause):
        sim.pause = False
        
        
    
    
    font = pygame.font.SysFont('comicsans', 50)
    
    if sim.val <= 0:
        Y = font.render(f"Y: 0", 1, ORANGE)
        X = font.render(f"X: {round(ball.h_distance,3)}", 1, ORANGE)
    else:
        Y = font.render(f"Y: {round(sim.val/10,3)}", 1, ORANGE)
        X = font.render(f"X: {(sim.counter-200)/10}", 1, ORANGE)
    
    win.fill(BLACK, (900,150,200,100))
    
    win.blit(X, (900,150))
    win.blit(Y, (900,200))
    
    
       
    
        
    
    
    
pygame.quit()
    
    
