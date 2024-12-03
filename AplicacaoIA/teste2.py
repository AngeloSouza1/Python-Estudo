import cv2

cap = cv2.VideoCapture(2)

if not cap.isOpened():
    print("Erro: Não foi possível acessar a câmera.")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Erro: Não foi possível capturar o frame.")
        break

    # Mostrar o feed de vídeo
    cv2.imshow("Feed de Vídeo", frame)

    # Pressione 'ESC' para sair
    if cv2.waitKey(30) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
