import os
import shutil
import time

from View.alertas import alert, alert_notify

diretorio = r'C:'
pasta_arquivos = '\Robot Arquivos'
pasta_autos = '\Robot autos'
pasta_relatorios = '\Robot Relatorios'
past_banco = '\Robot Banco de dados'
caminho_padrao = diretorio + pasta_autos
caminho_destino_padrao = diretorio + pasta_arquivos


def create_diretorios_arquivos():
    try:
        if not os.path.exists(diretorio + pasta_arquivos):
            os.mkdir(diretorio + pasta_arquivos)
        if not os.path.exists(diretorio + pasta_autos):
            os.mkdir(diretorio + pasta_autos)
        if not os.path.exists(diretorio + pasta_relatorios):
            os.mkdir(diretorio + pasta_relatorios)
        if not os.path.exists(diretorio + past_banco):
            os.mkdir(diretorio + past_banco)
    except ValueError:
        alert('Erro', f'{ValueError}')


def diretorios_exec(auto):
    pasta_loop = auto
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
        if os.path.exists(caminho_destino_padrao + '\\' + pasta_loop):
            shutil.rmtree(caminho_destino_padrao + '\\' + pasta_loop)
            shutil.move(caminho_padrao + '\\' + pasta_loop, caminho_destino_padrao)
        else:
            shutil.move(caminho_padrao + '\\' + pasta_loop, caminho_destino_padrao)
    except ValueError:
        alert('erro', f'Erro {ValueError}')


def no_diretorio_exec():
    os.chdir(caminho_padrao)
    try:
        for arquivo in os.listdir():
            if os.path.exists(caminho_destino_padrao + '\\' + arquivo):
                os.remove(caminho_destino_padrao + '\\' + arquivo)
                shutil.move(arquivo, caminho_destino_padrao)
            else:
                shutil.move(arquivo, caminho_destino_padrao)  # move todos arquivos baixados para a pasta do ait do Loop
    except ValueError:
        alert('erro', f'Erro ao mover os arquivos para a pasta final{ValueError}')


def clean_diretorio_autos():
    os.chdir(caminho_padrao)
    try:
        for arquivo in os.listdir():
            os.remove(arquivo)
    except ValueError:
        alert('erro', f'Erro ao Apagar os arquivos para a pasta final{ValueError}')


def verify_downloads(values):
    contador = 60
    while True:
        if contador == 0:
            return 1
        else:
            if len(os.listdir(caminho_padrao)) < str(values).count('True')-1 or\
                    '.crdownload' in str(os.listdir(caminho_padrao)) or\
                    '.tmp' in str(os.listdir(caminho_padrao)):  # Não conta o True de criar pasta
                alert_notify('Aviso',f'Estamos tentando realizar o download. Tentativas - ({contador})')
                time.sleep(0.5)
                contador -= 1
            else:
                break

        # else:
        #     break
