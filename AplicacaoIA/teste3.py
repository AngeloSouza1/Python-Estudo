import cv2

for index in [0, 2]:  # Índices de câmeras funcionais identificados
    print(f"Testando câmera no índice {index}...")
    cap = cv2.VideoCapture(index)

    if not cap.isOpened():
        print(f"Erro: Não foi possível acessar a câmera no índice {index}.")
        continue

    print(f"Câmera no índice {index} está funcionando. Pressione ESC para sair.")
   while True:
    ret, frame2 = cap.read()
    if not ret:
        print("Erro: Não foi possível capturar o frame.")
        break

    # Exibir o feed de vídeo
    cv2.imshow("Câmera Frontal - Detecção de Movimentação", frame2)

    # Sair com a tecla ESC
    if cv2.waitKey(30) & 0xFF == 27:
        break


    cap.release()
    cv2.destroyAllWindows()
