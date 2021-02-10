import pygame


def placement(coordinate):
    x=coordinate[0]
    y=coordinate[1]
    if x <= 200:
        if y <= 200:
            return (5, 0)
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
                    _0.append(placement(pygame.mouse.get_pos()))
                    player=1
                else:
                    _1.append(placement(pygame.mouse.get_pos()))
                    player=0
        for i in _0: DISPLAY.blit(o, i)
        for i in _1: DISPLAY.blit(x, i)
        pygame.display.update()
        continue
    return

if __name__ == '__main__':
    for i in range(100):
        ttt()