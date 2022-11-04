import pygame as pg
import time

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (142, 142, 142)
SILVER = (192, 192, 192)
LIGHT = (252, 204, 116)
DARK = (87, 58, 46)
GREEN = (0, 255, 0)
RED = (215, 0, 0)
ORANGE = (255, 165, 0)
BLUE = (0, 0, 215)

w = 500
h = 500
margin = 50
blocks = 5
size = w // blocks

def draw_squares(screen):
    for row in range(blocks):
        for square in range(blocks):
            pg.draw.rect(screen, WHITE, 
                ((margin + row * size, margin + square * size),
                (size, size)))

            pg.draw.rect(screen, BLACK, 
                ((margin + row * size, margin + square * size),
                (size, size)), width=1)

def drawCrosses(screen) :
    for X in Crosses :
        x, y = X[0], X[1]
        centerx = margin + x * size + size // 2
        centery = margin + y * size + size // 2
        offset = size * 3 // 10
        pg.draw.line(screen, RED, 
            (centerx - offset, centery - offset),
            (centerx + offset, centery + offset), width=10)

        pg.draw.line(screen, RED, 
            (centerx - offset, centery + offset),
            (centerx + offset, centery - offset), width=10)

def drawCircles(screen) :
    for X in Circles :
        x, y = X[0], X[1]
        centerx = margin + x * size + size // 2
        centery = margin + y * size + size // 2
        r = size * 3.5 // 10
        pg.draw.circle(screen, BLUE, 
            (centerx, centery),
             r, width=6)



screen = pg.display.set_mode((w + 2 * margin, h + 2 * margin))
pg.init()
ix, iy = 0, 0

Crosses = list()
Circles = list()
enable = True
while(True) :
    
    screen.fill(GREY)
    draw_squares(screen)
    drawCrosses(screen)
    drawCircles(screen)
    pg.display.update()
    refresh = False
    while enable :
        event = pg.event.wait()
        if event.type == pg.MOUSEBUTTONDOWN :
            ix = (event.pos[0] - margin) // size
            iy = (event.pos[1] - margin) // size
            coord = (ix, iy)
            if coord in Crosses or coord in Circles :
                continue
            Circles.append(coord)
            enable = False
            refresh = True
            
    if refresh :
        continue

    if not enable:
        print(enable)
        print('开始计算')
        time.sleep(5)
        print('结束计算')
        pg.event.clear()
        enable = True
            
   