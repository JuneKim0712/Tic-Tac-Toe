import numpy as np
import pygame


#converting player input to refinable coordinate value
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


#function that check is the current player have won
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


#nextmove for AI
def nextmove(_1, _0):
    stm=cas(_1+_0)
    li=[]
    for i in stm:
        inax=minimax(_1.copy(), (_0+[i]).copy())
        if inax==1:
            return  i
        li.append((inax, i))
    li.sort()
    print(li)
    return li[-1][-1]


#1=win, -1=lost, draw=0, returns coordinate, (win, lose or draw)
def minimax(_1, _0):
    if is3(_0): return 1
    elif is3(_1): return -1
    elif len(_1+_0)==9: return 0
    stm=cas(_1+_0)
    list_wld=[]
    for i in stm:
        result=minimax2((_1+[i]).copy(), _0.copy())
        list_wld.append(result)
    list_wld.sort()
    return list_wld[0]

def minimax2(_1, _0):
    if is3(_0): return 1
    elif is3(_1): return -1
    elif len(_1+_0)==9: return 0
    stm=cas(_1+_0)
    list_wld=[]
    for i in stm:
        result=minimax(_1.copy(), (_0+[i]).copy())
        list_wld.append(result)
    list_wld.sort()
    return list_wld[-1]


#function that shows avaible space for next move
def cas(list_):
    avsp=[]
    for i in [(5, 5), (205, 5), (405, 5), (5, 205), (205, 205), (405, 205), (5, 405), (205, 405), (405, 405)]:
        if not i in list_: avsp.append(i)
        else: pass
    return avsp.copy()


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
    player=1
    _0=[(205, 205)]
    _1=[]
    while open:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if player==1:
                    po=placement(pygame.mouse.get_pos())
                    if not po in _0 and not po in _1:
                        player=0
                        _1.append(po)
        if player == 0:
            po=nextmove(_1.copy(), _0.copy())
            player=1
            _0.append(po)
        if is3(_0):
            print('cross won')
            open=False           
        if is3(_1):
            print('circle won')
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
