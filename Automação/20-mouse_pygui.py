import pyautogui
import time

# 1- Tamanho da tela
print(pyautogui.size())

# 2- Pegar a posição atual do cursor
print(pyautogui.position())
time.sleep(2)

# 3 - App para vê a posição do mouse em tempo real
# python
# from pyautogui import mouseInfo
# mouseInfo()

# 4 - Mover o cursor do Mouse
pyautogui.moveTo(1842,14)
time.sleep(2)
pyautogui.click()

# 5 - Scroll
time.sleep(2)
pyautogui.moveTo(1060,461)
pyautogui.click()
time.sleep(2)
pyautogui.scroll(900)