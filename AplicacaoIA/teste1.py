import cv2

# Testar acesso à câmera
cap = cv2.VideoCapture(0)  # /dev/video0 é o índice 0
if not cap.isOpened():
    print("Erro: Não foi possível acessar a câmera.")
    exit()

print("Câmera inicializada com sucesso!")

ret, frame = cap.read()
if ret:
    print("Frame capturado com sucesso!")
else:
    print("Erro: Não foi possível capturar o frame.")

cap.release()
