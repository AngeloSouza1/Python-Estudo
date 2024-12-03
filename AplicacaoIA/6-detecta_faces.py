import cv2
import dlib
import numpy as np

# Inicializar a câmera frontal no índice 2
cap = cv2.VideoCapture(2)

if not cap.isOpened():
    print("Erro: Não foi possível acessar a câmera frontal.")
    exit()

# Criar a janela para exibição com configuração manual
cv2.namedWindow("Câmera Frontal - Detecção e Contagem de Faces", cv2.WINDOW_NORMAL)

# Inicializar o detector de faces do dlib
detector = dlib.get_frontal_face_detector()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Erro: Não foi possível capturar o frame.")
        break

    # Espelhar o frame (opcional)
    frame = cv2.flip(frame, 1)

    # Converter o frame para escala de cinza
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detectar faces no frame
    faces = detector(gray_frame)
    num_faces = len(faces)

    # Desenhar retângulos ao redor das faces detectadas
    for i, face in enumerate(faces):
        x, y = face.left(), face.top()
        x1, y1 = face.right(), face.bottom()
        cv2.rectangle(frame, (x, y), (x1, y1), (0, 255, 0), 2)

        # Exibir o número da face detectada acima do retângulo
        cv2.putText(
            frame,
            f"Face {i + 1}",
            (x - 10, y - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (0, 0, 255),
            2
        )

    # Exibir a contagem total de faces detectadas no topo da janela
    cv2.putText(
        frame,
        f"Total de Faces: {num_faces}",
        (10, 30),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (255, 255, 0),
        2
    )

    # Exibir o feed de vídeo
    cv2.imshow("Câmera Frontal - Detecção e Contagem de Faces", frame)

    # Sair com a tecla ESC
    if cv2.waitKey(30) & 0xFF == 27:
        break

# Liberar a câmera e destruir janelas
cap.release()
cv2.destroyAllWindows()
