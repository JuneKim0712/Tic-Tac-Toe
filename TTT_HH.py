import numpy as np
import pygame


def placement(coordinate):
    x=coordinate[0]
    y=coordinate[1]
    if x <= 200:
        if y <= 200:
            return (5, 5)
        elif y <= 400:
            return (5, 205)
        else:
            return (5, 405)
    elif x <= 400:
        if y <= 200:
            return (205, 5)
        elif y <= 400:
            return (205, 205)
        else:
            return (205, 405)
    else:
        if y <= 200:
            return (405, 5)
        elif y <= 400:
            return (405, 205)
        else:
            return (405, 405)


def is3(c):
    if (205, 205) in c:
        if (5, 5) in c and (405, 405) in c:
            return 1
        elif (405, 5) in c and (5, 405) in c:
            return 1
        elif (205, 5) in c and (205, 405) in c:
            return 1
        elif (5, 205) in c and (405, 205) in c:
            return 1
    elif (405, 5) in c:
        if (5, 5) in c and (205, 5) in c:
            return 1
        elif (405, 205) in c and (405, 405) in c:
            return 1
    elif (5, 405) in c:
        if (5, 5) in c and (5, 205) in c:
            return 1
        elif (205, 405) in c and (405, 405) in c:
            return 1
    return 0

def ttt():
    pygame.init()
    DISPLAY = pygame.display.set_mode([600, 600])
    pygame.display.set_caption('Tic Tac Toe')
    WHITE, RED, GREEN, BLACK = [255, 255, 255], [255, 0, 0], [0, 255, 0], [0, 0, 0]
    o=pygame.image.load('image/circle.png')
    x=pygame.image.load('image/x.jpg')
    DISPLAY.fill(WHITE)
    lines=[[(200, 0), (200, 600)], [(400, 0), (400, 600)], [(0, 200), (600, 200)], [(0, 400), (600, 400)]]
    for line in lines: pygame.draw.line(DISPLAY, BLACK, line[0], line[1])
    pygame.display.flip()
    open = True
    player=0
    _0=[]
    _1=[]
    while open:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if player == 0:
                    po=placement(pygame.mouse.get_pos())
                    if not po in _0 and not po in _1:
                        player=1
                        _0.append(po)
                    if is3(_0):
                        print('circle won')
                        open=False
                    
                else:
                    po=placement(pygame.mouse.get_pos())
                    if not po in _0 and not po in _1:
                        player=0
                        _1.append(po)
                    if is3(_1):
                        print('cross won')
                        open=False
        if len(_0)==5:
            print('draw')
            open=False
        for i in _0: DISPLAY.blit(o, i)
        for i in _1: DISPLAY.blit(x, i)
        pygame.display.update()
        continue
    return

if __name__ == '__main__':
    for i in range(1, 100):
        ttt()
