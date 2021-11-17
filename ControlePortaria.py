import face_recognition
import cv2
import numpy as np
import os
import glob

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
                    umdois = 0
                    matches = face_recognition.compare_faces(
                        faces_encodings, face_encoding)
                    name = "Acesso Negado"
                    face_distances = face_recognition.face_distance(
                        faces_encodings, face_encoding)
                    best_macth_index = np.argmin(face_distances)
                    if matches[best_macth_index]:
                        name = faces_names[best_macth_index]+" mostre seu token!"
                    face_names.append(name)
            process_this_frame = not process_this_frame

            for (top, right, bottom, left), name in zip(face_locations, face_names):
                top *= 4
                right *= 4
                bottom *= 4
                left *= 4
                cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
                font = cv2.FONT_HERSHEY_DUPLEX
                cv2.putText(frame, name, (left+6, bottom-6),
                            font, 1, (255, 255, 255), 1)

            # encerrando a detecção
            cv2.imshow("Camera", frame)
            k = cv2.waitKey(60)
            if k == 27:
                cv2.destroyAllWindows()
                video_capture.release()
                break
        
        

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
                cv2.imwrite('Cadastros/'+str(name)+'.png', image)
                camera.release()
                cv2.destroyAllWindows()
                break

    elif (entrada == 3):
        cv2.destroyAllWindows()
        break