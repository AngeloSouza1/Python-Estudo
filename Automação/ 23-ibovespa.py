import pyautogui
import time
import webbrowser



# Garantir que o Firefox esteja em foco
pyautogui.press('winleft')  # Abre o menu Iniciar
time.sleep(1)
pyautogui.write('firefox')  # Digita "firefox" para focar
time.sleep(1)
pyautogui.press('enter')    # Pressiona Enter
time.sleep(2)

# Pesquisar "ibovespa hoje" no Google
pyautogui.write('ibovespa hoje')  # Escreve a consulta
time.sleep(1)
pyautogui.press('enter')  # Pressiona Enter para pesquisar

# Aguarda a página carregar
time.sleep(5)  # Ajuste conforme necessário

# Tirar screenshot
pyautogui.screenshot('ibovespa.png')
print("Screenshot salva como 'ibovespa.png'")
