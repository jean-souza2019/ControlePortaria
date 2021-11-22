# ControlePortaria
Controle de portaria Python

Ferramentas necessárias:
-Python 3;
-Numpy;
-OpenCV;
-CMake;
-Face-recognition;
-datetime;
-time
-glob
-os

Comandos para executar: 
-pip install numpy
-pip install opencv-python
-pip install cmake
-pip install face-recognition

Opções do menu principal:
1) Entrar com seu login facil e token: o sistema fará o reconhecimento da face do usuário e buscará na base de cadastro, o nome do usuário relacionado, caso o mesmo exista o sistema solicitará  o token de autenticação para concluir o acesso; 
2) Realizar novo cadastro: ao escolher esta opção, o usuário irá inserir seu nome, após abrirá a câmera de seu dispositivo e pressionar a tecla de "Espaço" para tirar a foto e o sistema armanezará no servidor;
3) Sair