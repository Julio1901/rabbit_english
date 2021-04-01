#Rabbit English
##This is a simple web application to assist in the study of the English language
###Key features
-Cadastro de usuário
  -Cadastro a partir de um endereço de e-mail com formato válido, porém, o mesmo não é verificado
-Criação de dicionário pessoal de inglês:
  -Fetuare para adicionar palavras com suas respectivas traduções à base do usuário logado, criando, assim, um dicionário pessoal de "Palavras aprendidas" em inglês.
  -Feature para exibir todas as palavras que o usuário salvou em seu dicionário pessoal
- Word Game
  -Um pequeno jogo que sorteia palavras dentro do dicionário pessoal do usuário, exibe na tela e espera receber uma resposta com a tradução da palavra exibida. O mesmo contabiliza pontos positivos toda vez que o usuário acerta uma tradução.

>Status do Projeto: Em desenvolvimento :warning:

<img link='https://github.com/Julio1901/rabbit_english/blob/cleaning_project/readme_images/rabbit_01.png'>
<img link='https://github.com/Julio1901/rabbit_english/blob/cleaning_project/readme_images/rabbit02.png'>
<img link='https://github.com/Julio1901/rabbit_english/blob/cleaning_project/readme_images/rabbit03.png'>
<img link='https://github.com/Julio1901/rabbit_english/blob/cleaning_project/readme_images/rabbit3.png'>
<img link='https://github.com/Julio1901/rabbit_english/blob/cleaning_project/readme_images/rabbit5.png'>

####How to run the project
-Steps to run the project
  -No terminal, clone o projeto:
    -https://github.com/Julio1901/rabbit_english.git
  -Tenha o Python 3 e o Pip3 instalados em sua máquina linux:
    -sudo dnf install python3 python3-pip
  -Certifique-se de ter o Django instalado na versão 3.1.2:
    - pip install Django==3.1.2
  -Entre na pasta do projeto:
    - cd rabbit_english
  -Start um servidor local no diretório onde se encontra o "manage.py":
    - python manage.py run server
    -Por padrão, o servidor irá iniciar na porta 8000
    -Pegue o link do servidor local que apareceu no terminal, algo como "http://127.0.0.1:8000/" e cole no navegador

#####Backend User exemple:

|id| user_name |     email     |   password  |
|--| ----------|---------------|-------------|
|1 |Julio Cesar|julio@gmail.com|minhaSenha@123

######Backend word exemple:

|id| user_name |  word  |translate|
|--| ----------|--------|---------|
|1 |Julio Cesar|  tree  |  árvore |





