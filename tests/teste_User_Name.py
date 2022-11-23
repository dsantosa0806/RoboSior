import os
import getpass as gt
import shutil


# def clean_diretorio_autos():
#
#     os.chdir(download_path)
#     try:
#         for arquivo in os.listdir():
#             print(arquivo)
#             os.remove(arquivo)
#     except ValueError:
#         print(f'erro Erro ao Apagar os arquivos para a pasta final{ValueError}')
#
# clean_diretorio_autos()
#
# print(os.getcwd())
#
# download_path = r'C:\Users\Usuário\OneDrive\Documentos\GitHub\RoboSior\autos'
# print(os.listdir(download_path))
# print(len(os.listdir(download_path)))
#
# values = {0: None, 'Auto de Infração': True,
#           'Relatório Financeiro': True,
#           'Relatório Resumido': False,
#           'Notificação de autuação': False,
#           'Notificação de Penalidade': False,
#           'PastasSim': False,
#           'PastasNão': False,
#           'auto': ''}
#
# Qutde = str(values).count('True')-1
#
# print(Qutde)
#
# while True:
#     if len(os.listdir(download_path)) < str(values).count('True')-1:
#         print('A quantidade é menor')
#     else:
#         print('A quantidade é maior')
#         break


download_path = r'C:\Users\Usuário\OneDrive\Documentos\GitHub\RoboSior\autos'


print((os.listdir(download_path)))
if '.crdownload' or '.tmp' in str(os.listdir(download_path)):
    print('Elemento Loc')




