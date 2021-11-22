# ControlePortaria
Criamos um algoritmo de controle de portaria utilizando a autenticação de duplo fator, o reconhecimento facial e um token. Cada acesso ao sistema gera um log referente ao usuário e a data e hora que houve o acesso.


# Ferramentas necessárias:
-Python 3;
-Numpy;
-OpenCV;
-CMake;
-Face-recognition;
-datetime;
-time
-glob
-os

# Comandos necessários para executar: 
-pip install numpy
-pip install opencv-python
-pip install cmake
-pip install face-recognition

# Funcionamento:
Opções do menu principal:
1) Entrar com seu login facil e token: o sistema fará o reconhecimento da face do usuário e buscará na base de cadastro, o nome do usuário relacionado, caso o mesmo exista o sistema solicitará  o token de autenticação para concluir o acesso; 
2) Realizar novo cadastro: ao escolher esta opção, o usuário irá inserir seu nome, após abrirá a câmera de seu dispositivo e pressionar a tecla de "Espaço" para tirar a foto e o sistema armanezará no servidor;
3) Sair
