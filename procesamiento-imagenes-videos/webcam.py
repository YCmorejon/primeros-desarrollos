
import cv2  # Librería para procesamiento de imágenes y video
from datetime import datetime
import pandas as pd

# Variable que almacenará el primer frame (fondo inicial)
first_frame = None
status_list = [None, None]
times = []
df = pd.DataFrame(columns=["Start", "End"])

# Accediendo a la cámara de la laptop
video = cv2.VideoCapture(0)

while True:
    check, frame = video.read()  # Capturando un frame de la webcam
    
    status = 0

    # Convertir el frame a escala de grises
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Aplicar desenfoque gaussiano para reducir ruido
    gray = cv2.GaussianBlur(gray, (21, 21), 0)

    # Guardar el primer frame de referencia (fondo inicial)
    if first_frame is None:
        first_frame = gray
        continue  # Salta al siguiente ciclo para capturar el siguiente frame

    # Calcular la diferencia absoluta entre el primer frame y el actual
    delta_frame = cv2.absdiff(first_frame, gray)
    
    umbral_otsu, imagen_binaria = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    imagen_binaria = cv2.dilate(imagen_binaria, None, iterations=2)  # Dilatando la imagen para rellenar agujeros
    
    (cnts, _) = cv2.findContours(imagen_binaria.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    for contour in cnts:
        if cv2.contourArea(contour) < 1000:
            continue
        status = 1
        (x, y, w, h) = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)
        
    status_list.append(status)
    
    if status_list[-1] == 1 and status_list[-2] == 0:
        times.append(datetime.now())        
    if status_list[-1] == 0 and status_list[-2] == 1:
        times.append(datetime.now())          

    # Mostrar los resultados en diferentes ventanas
    #cv2.imshow("Gray Frame", gray)
    #cv2.imshow("Delta Frame", delta_frame)
    #cv2.imshow("Threshold Frame", imagen_binaria)
    cv2.imshow("Panel Principal", frame)

    # Esperar 1 milisegundo para ver si el usuario presiona 'q'
    key = cv2.waitKey(1)

    if key == ord("q"):  # Si se presiona 'q', salir del bucle
        if status == 1:
            times.append(datetime.now())
        break

# Añadiendo tiempos al df 
for i in range(0, len(times), 2):
    df = pd.concat([df, pd.DataFrame({"Start": [times[i]], "End": [times[i + 1]]})], ignore_index=True)
    
# Creando el csv con el df
df.to_csv("Times.csv", index=False)

# Liberar el recurso de la cámara
video.release()

# Cerrar todas las ventanas de OpenCV
cv2.destroyAllWindows()
