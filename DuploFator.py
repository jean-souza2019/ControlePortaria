import cv2
import numpy as np
from datetime import datetime

camera = cv2.VideoCapture(1, cv2.CAP_DSHOW)
tokenValido = False

def mudouValor(x):
    pass


# cv2.namedWindow("Camera")
# cv2.createTrackbar("H", "Camera", 150, 150, mudouValor)
# cv2.createTrackbar("S", "Camera", 170, 170, mudouValor)
# cv2.createTrackbar("V", "Camera", 67, 67, mudouValor)


# cv2.createTrackbar("H", "Camera", 0, 179, mudouValor)
# cv2.createTrackbar("S", "Camera", 0, 255, mudouValor)
# cv2.createTrackbar("V", "Camera", 0, 255, mudouValor)
while True:
    _, frame = camera.read()
    frameHsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    frameRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    # h = cv2.getTrackbarPos("H", "Camera")
    # s = cv2.getTrackbarPos("S", "Camera")
    # v = cv2.getTrackbarPos("V", "Camera")

    upperColor = np.array([179, 255, 255])
    # lowerColor = np.array([h, s, v])


    # Setando  cor vermelha
    
    
    # aqui abaixo está fixo para ser vemelho o token
    lowerColor = np.array([150, 131, 67])
    mascara = cv2.inRange(frameHsv, lowerColor, upperColor)
    resultado = cv2.bitwise_and(frame, frame, mask=mascara)


    # Criando borda e contorno para cor vermelha
    _, borda = cv2.threshold(cv2.cvtColor(
        resultado, cv2.COLOR_BGR2GRAY), 3, 255, cv2.THRESH_BINARY)

    contornos, _ = cv2.findContours(
        borda, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)



    for contorno in contornos:
        area = cv2.contourArea(contorno)
        x, y, w, h = cv2.boundingRect(contorno)
        if area > 500:   
            tokenValido = True
            cv2.putText(frame, "Token valido.", (x, y-10),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255))


    cv2.imshow("Camera", frame)
    
    k = cv2.waitKey(60)
    if k == 27:
        break

# Gera log caso usuário foi autenticado
if(tokenValido == True):
    with open("log.txt", "a") as arquivo:
        data_e_hora_atuais = datetime.now()
        data_e_hora_em_texto = data_e_hora_atuais.strftime('%d/%m/%Y %H:%M')
        arquivo.write("Usuario JEAN realizou login em: "+str(data_e_hora_em_texto)+"\n")
        
        



cv2.destroyAllWindows()
camera.release()
