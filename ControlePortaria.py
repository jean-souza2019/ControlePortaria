import face_recognition
import cv2
import numpy as np
import os
import glob
import time
from datetime import datetime


tokenValido = False
idPessoal = False

def mudouValor(x):
    pass

while True:
    print("\n########  Bem-Vindo  ########")
    print("###  Sistema de Portaria  ### \n")
    print("   Insira a sua opção:")
    print("     1) Entrar com seu login facil e token.")
    print("     2) Realizar novo cadastro.")
    print("     3) Sair.")
    entrada = int(input(">"))

    if (entrada == 1):
        print("Aguarde, carregando módulos...")
        faces_encodings = []
        faces_names = []
        cur_direc = os.getcwd()

        path = os.path.join(cur_direc, 'Cadastros/')
        list_of_files = [f for f in glob.glob(path+"*.png")]
        number_files = len(list_of_files)
        names = list_of_files.copy()

        for i in range(0, number_files):
            presets = face_recognition.load_image_file(list_of_files[i])
            encoding = face_recognition.face_encodings(presets)[0]
            faces_encodings.append(encoding)
            names[i] = names[i].replace(cur_direc+"\\Cadastros\\", "")
            names[i] = names[i].replace(".png", "")
            faces_names.append(names[i])


        face_locations = []
        face_encodings = []
        face_names = []
        process_this_frame = True
        video_capture = cv2.VideoCapture(1,cv2.CAP_DSHOW)
        print ("\n" * 130) 
        
        
        while True:
            _, frame = video_capture.read()
            # começando a detecção
            small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)  # 100/4 = 25
            rgb_small_frame = small_frame[:, :, ::-1]
            if process_this_frame:
                face_locations = face_recognition.face_locations(rgb_small_frame)
                face_encodings = face_recognition.face_encodings(
                    rgb_small_frame, face_locations)
                face_names = []
                for face_encoding in face_encodings:
                    matches = face_recognition.compare_faces(
                        faces_encodings, face_encoding)
                    
                    name = "Acesso Negado"
                    face_distances = face_recognition.face_distance(
                        faces_encodings, face_encoding)
                    
                    # if(face_distances != []):
                    #     best_macth_index = np.argmin(face_distances)
                    #     print(best_macth_index)
                    
                    if(face_distances != []):
                        best_macth_index = np.argmin(face_distances)
                        print(best_macth_index)
                        
                    if matches[best_macth_index]:
                        idPessoal = True
                        namePessoa = faces_names[best_macth_index]
                        name = namePessoa+", mostre seu token!"
                        
                        
                        # Aqui começa tratamento para token
                        frameHsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
                        upperColor = np.array([179, 255, 255])
                        lowerColor = np.array([150, 131, 67])
                        maskToken = cv2.inRange(frameHsv, lowerColor, upperColor)
                        resultadoToken = cv2.bitwise_and(frame, frame, mask=maskToken)
    
                        _, borda = cv2.threshold(cv2.cvtColor(
                            resultadoToken, cv2.COLOR_BGR2GRAY), 3, 255, cv2.THRESH_BINARY)

                        contornos, _ = cv2.findContours(
                            borda, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)                        
                    
                        
                    face_names.append(name)
                    
            process_this_frame = not process_this_frame

                         
            for (top, right, bottom, left), name in zip(face_locations, face_names):
                top *= 4
                right *= 4
                bottom *= 4
                left *= 4
                cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 255), 1)
                font = cv2.FONT_HERSHEY_DUPLEX
                cv2.putText(frame, name, (left+6, bottom-6),
                            font, 1, (255, 255, 255), 1)

            if matches[best_macth_index]:
                for contornoToken in contornos:
                    area = cv2.contourArea(contornoToken)
                    xToken, yToken, wToken, hToken = cv2.boundingRect(contornoToken)
                    if area > 500:   
                        tokenValido = True
                        cv2.putText(frame, "Token valido.", (xToken, yToken-10),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255))
            

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            lap = cv2.Laplacian(gray, cv2.CV_64F)
            lap = np.uint8(np.absolute(lap))

            cv2.imshow("Laplaciano Simples", lap)
            
            cv2.imshow("Camera", frame)     
                
            k = cv2.waitKey(60)
            
            if (tokenValido == True & idPessoal == True):
                time.sleep(2)
                cv2.destroyAllWindows()
                video_capture.release()
                print("\n########  Bem-Vindo, "+str(namePessoa)+"  ########")
                print("###  Você acaba de logar no sistema.  ### \n")
                time.sleep(15)
                break
            
            
            elif (k == 27):
                cv2.destroyAllWindows()
                video_capture.release()
                break
        
        # Gera log caso usuário foi autenticado
        if(tokenValido == True):
            with open("log.txt", "a") as arquivo:
                data_e_hora_atuais = datetime.now()
                data_e_hora_em_texto = data_e_hora_atuais.strftime('%d/%m/%Y %H:%M')
                arquivo.write("Usuario "+str(namePessoa)+" realizou login em: "+str(data_e_hora_em_texto)+"\n")
            
        

    elif (entrada == 2):
        print("Aguarde, carregando módulos...")
        camera = cv2.VideoCapture(1,cv2.CAP_DSHOW)
        print ("\n" * 130) 
        print("Clique espaço para capturar")
        while True:
            return_value, image = camera.read()

            cv2.imshow("Novo Cadastro", image)

            k = cv2.waitKey(1)
            if k%256 == 32:
                # ESPAÇO para tirar foto
                print ("\n" * 130) 
                name = input('Informe seu nome: \n')
                name.replace(" ", "_")
                # Aqui fazer um resize da imagem reduzindo ela em algum tamanho bom que mostre somente o rosto. OBS precisa ser quadrado
                cv2.imwrite('Cadastros/'+str(name)+'.png', image)
                camera.release()
                cv2.destroyAllWindows()
                break

    elif (entrada == 3):
        cv2.destroyAllWindows()
        break