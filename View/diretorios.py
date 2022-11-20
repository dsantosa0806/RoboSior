import os
import shutil
from View.alertas import alert


def diretorios_exec(auto):
    caminho_destino_padrao = r'C:\Users\Usuário\OneDrive\Documentos\GitHub\RoboSior'  # PROBLEMA
    pasta_final = 'Arquivos'
    os.chdir(caminho_destino_padrao)
    try:
        if not os.path.exists(pasta_final):
            os.mkdir(pasta_final)  # Cria a pasta AIT do Loop
    except ValueError:
        alert('Erro', f'{ValueError}')

    pasta_loop = auto
    caminho_padrao = r'C:\Users\Usuário\OneDrive\Documentos\GitHub\RoboSior\autos' # PROBLEMA
    os.chdir(caminho_padrao)
    try:
        if not os.path.exists(pasta_loop):
            os.mkdir(pasta_loop)  # Cria a pasta AIT do Loop

    except ValueError:
        shutil.rmtree(pasta_loop)
        alert('Erro','A Pasta já existe e será deletada. Tente novamente!')
        os.mkdir(pasta_loop)
    try:
        for arquivo in os.listdir():
            if arquivo != pasta_loop:
                shutil.move(arquivo, pasta_loop)  # move todos arquivos baixados para a pasta do ait do Loop
    except ValueError:
        alert('erro', f'Erro ao mover os arquivos para a pasta final{ValueError}')

    try:
        if os.path.exists(caminho_destino_padrao + '\\' + pasta_final + '\\' + pasta_loop):
            shutil.rmtree(caminho_destino_padrao + '\\' + pasta_final + '\\' + pasta_loop)
            shutil.move(caminho_padrao + '\\' + pasta_loop, caminho_destino_padrao + '\\' + pasta_final)
        else:
            shutil.move(caminho_padrao + '\\' + pasta_loop, caminho_destino_padrao + '\\' + pasta_final)
    except ValueError:
        alert('erro', f'Erro {ValueError}')



