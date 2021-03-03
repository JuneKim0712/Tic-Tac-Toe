import pyautogui
import time
from PIL import Image
from PIL import ImageChops
from PIL import ImageGrab


#function that check is the current player have won
def is3(c):
    if (390, 520) in c:
        if (160, 290) in c and (620, 750) in c:
            return 1
        elif (620, 290) in c and (160, 750) in c:
            return 1
        elif (390, 290) in c and (390, 750) in c:
            return 1
        elif (160, 520) in c and (620, 520) in c:
            return 1
    if (620, 290) in c:
        if (160, 290) in c and (390, 290) in c:
            return 1
        elif (620, 520) in c and (620, 750) in c:
            return 1
    if (160, 750) in c:
        if (160, 290) in c and (160, 520) in c:
            return 1
        elif (390, 750) in c and (620, 750) in c:
            return 1
    return 0


#function that shows avaible space for next move
def cas(list_):
    avsp=[]
    for i in [(160, 290), (390, 290), (620, 290), (160, 520), (390, 520), (620, 520), (160, 750), (390, 750), (620, 750)]:
        if not i in list_: avsp.append(i)
        else: pass
    return avsp.copy()


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


def check(list_=[]):
    rang=cas(list_)
    avsp=[]
    cp=Image.open('image/cp.png')
    for i in rang:
        im=ImageGrab.grab((i[0], i[1], i[0]+150, i[1]+150))
        diff = ImageChops.difference(im, cp)
        if diff.getbbox(): avsp.append(i)
    return avsp.copy()


#_1 player, _0 AI
def game():
    _0=[]
    _1=[]
    t=time.time()
    if not check():
        pyautogui.moveTo(160, 290)
        cp=Image.open('image/cp.png')
        im=ImageGrab.grab((200, 400, 250, 450))
        diff = ImageChops.difference(im, cp)
        if diff.getbbox():
            _0=[(390, 520)]
            pyautogui.click(390, 520)
    while True:
        if time.time()-t>16: return
        cc=check(_0+_1)
        if cc:
            if is3(_0) or is3(_1): return
            _1=check(_0)
            stm=cas(_1+_0)
            li=[]
            for i in stm:
                inax=minimax(_1.copy(), (_0+[i]).copy())
                li.append((inax, i))
            li.sort()
            if not li: return
            _0.append(li[-1][-1])
            pyautogui.click(li[-1][-1])
            if is3(_0) or is3(_1): return
        time.sleep(0.1)
    return

for i in range(1, 99999):
    time.sleep(3)
    game()
    pyautogui.moveTo(20, 20)
    print(i)
    time.sleep(2)
    while True:
        time.sleep(0.1)
        pl=pyautogui.locateOnScreen('image/play again.png')
        print(pl)
        if type(pl) != type(None):
            pyautogui.click(pl[0]+5, pl[1]+5)
            pyautogui.moveTo(20, 20)
            break