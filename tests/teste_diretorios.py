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
print(caminho_atual)  # Caminho atual da aplicação

caminho_padrao = r'C:\autos'
pasta_loop = 'auto_do_loop_BXXXXXXXXX'
caminho_apos_downloads = fr'C:\autos\{pasta_loop}'
caminho_destino = r'C:\Downloads'
verifica_caminho_destino = fr'C:\Downloads\{pasta_loop}'

os.chdir(caminho_padrao)
print(os.getcwd()) # Mudança do caminho
try:
    if not os.path.exists(pasta_loop):
        os.mkdir(pasta_loop) # Cria a pasta AIT do Loop

except ValueError:
    shutil.rmtree(pasta_loop)
    print('A Pasta já existe e será deletada. Tente novamente!')

try:
    for i in os.listdir():
        if i != pasta_loop:
            print(i)
            shutil.move(i, pasta_loop)  # move todos arquivos baixados para a pasta do ait do Loop
except ValueError:
    print(f'Erro ao mover os arquivos para a pasta final{ValueError}')


if os.path.exists(verifica_caminho_destino):
    shutil.rmtree(verifica_caminho_destino)

shutil.move(caminho_apos_downloads,caminho_destino)
print('Sucesso !')








