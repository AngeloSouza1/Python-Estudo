import pyautogui
from time import sleep

with open("files/alunos.txt", "r", encoding="utf-8") as file:
    for line in file:
        aluno = line.split(',')[0]
        email = line.split(',')[1]
        pyautogui.click(279, 340, duration=0.2)
        pyautogui.write(aluno)
        pyautogui.click(279, 389, duration=0.2)
        pyautogui.write(email)
        pyautogui.click(351,417, duration=0.2)
        pyautogui.screenshot(f'files/img/{aluno}.png')
        sleep(0.3)
    
        # 279, 340
        # 279, 389