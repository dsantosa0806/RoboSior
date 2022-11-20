import os
import getpass as gt
import shutil


def clean_diretorio_autos():
    download_path = r'C:\Users\Usuário\OneDrive\Documentos\GitHub\RoboSior\autos'
    os.chdir(download_path)
    try:
        for arquivo in os.listdir():
            print(arquivo)
            os.remove(arquivo)
    except ValueError:
        print(f'erro Erro ao Apagar os arquivos para a pasta final{ValueError}')

clean_diretorio_autos()