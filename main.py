import cv2
import numpy as np

video_path = 'video_estacionamento.mp4'
cap = cv2.VideoCapture(video_path)

ret, frame = cap.read()
if not ret:
    print("Erro ao ler o vídeo. Verifique se o nome está correto.")
    exit()

frame = cv2.resize(frame, (1024, 768))
clone_frame = frame.copy()
ROIs = []
pontos_temp = []
desenhando = False

def desenhar_retangulo(event, x, y, flags, param):
    global pontos_temp, ROIs, clone_frame, frame, desenhando
    
    if event == cv2.EVENT_LBUTTONDOWN:
        pontos_temp = [(x, y)]
        desenhando = True
        
    elif event == cv2.EVENT_MOUSEMOVE:
        if desenhando:
            frame_temp = clone_frame.copy()
            cv2.rectangle(frame_temp, pontos_temp[0], (x, y), (0, 255, 0), 2)
            cv2.imshow("Selecione as Vagas", frame_temp)
            
    elif event == cv2.EVENT_LBUTTONUP:
        desenhando = False
        pontos_temp.append((x, y))
        x1, y1 = pontos_temp[0]
        x2, y2 = pontos_temp[1]
        
        if abs(x2 - x1) > 10 and abs(y2 - y1) > 10:
            w = abs(x2 - x1)
            h = abs(y2 - y1)
            x_min, y_min = min(x1, x2), min(y1, y2)
            ROIs.append((x_min, y_min, w, h))
            cv2.rectangle(clone_frame, (x_min, y_min), (x_min + w, y_min + h), (255, 0, 0), 2)
            cv2.imshow("Selecione as Vagas", clone_frame)

cv2.namedWindow("Selecione as Vagas")
cv2.setMouseCallback("Selecione as Vagas", desenhar_retangulo)

print("--- INSTRUÇÕES DE MARCAÇÃO ---")
print("1. Clique, SEGURE e ARRASTE para desenhar a vaga.")
print("2. Solte o clique para confirmar.")
print("3. Aperte a tecla 'c' para limpar tudo se errar.")
print("4. Aperte ENTER para começar o monitoramento.")

while True:
    cv2.imshow("Selecione as Vagas", clone_frame)
    key = cv2.waitKey(1) & 0xFF
    if key == ord("c"):  
        clone_frame = frame.copy()
        ROIs = []
    elif key == 13 or key == 27:  
        break

cv2.destroyWindow("Selecione as Vagas")

THRESHOLD_OCUPADO = 300 

while True:
    ret, frame = cap.read()
    if not ret:
        break
        
    frame = cv2.resize(frame, (1024, 768))
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    blur = cv2.GaussianBlur(gray, (5, 5), 1) 
    
    img_canny = cv2.Canny(blur, 50, 150)
    
    kernel = np.ones((3, 3), np.uint8)
    img_dilatada = cv2.dilate(img_canny, kernel, iterations=1) 

    for i, (x, y, w, h) in enumerate(ROIs):
        vaga_recorte = img_dilatada[y:y+h, x:x+w]
        contagem_pixels = cv2.countNonZero(vaga_recorte)
        
        print(f"Vaga {i} tem {contagem_pixels} pixels.")

        if contagem_pixels > THRESHOLD_OCUPADO:
            color = (0, 0, 255) 
            label = "Ocupada"
        else:
            color = (0, 255, 0) 
            label = "Livre"

        cv2.rectangle(frame, (x, y), (x+w, y+h), color, 2)
        cv2.putText(frame, f"{label}: {contagem_pixels}", (x, y-10), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

    cv2.imshow("Monitor (Resultado Final)", frame)
    
    cv2.imshow("Debug (Canny Edge + Dilatacao)", img_dilatada)
    
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()