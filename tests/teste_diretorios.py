import os
import shutil

# auto_criado = 'Auto_Do_Loop'
# download_path = fr'C:\Users\Usuário\OneDrive\Documentos\GitHub\RoboSior\autos\{auto_criado}'
#
#
# if not os.path.exists(auto_criado):
#     os.mkdir(auto_criado)
#
# diretorio_atual = download_path
# diretorio_destino = r'C:\autos'
#
# for i in os.listdir(download_path):
#     print(i)


# shutil.move(diretorio_atual,diretorio_destino) # Usar Shutil para mover a pasta


# for i in os.listdir():
#     print(i)


# Testes

caminho_atual = os.getcwd()
print(caminho_atual)


novo_caminho = r'C:\Users\Usuário\OneDrive\Documentos\GitHub\RoboSior\autos'
os.chdir(novo_caminho)
print(os.getcwd())

for i in os.listdir():
    print(i)



