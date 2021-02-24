import pyautogui
import time

t=time.time()
while (time.time()-t)<3000:
    time.sleep(0.5)
    pyautogui.click()