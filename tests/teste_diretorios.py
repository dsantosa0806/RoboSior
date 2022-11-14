import os

diretorio = 'teste_Pasta'
if not os.path.exists(diretorio):
    os.mkdir(diretorio)



diretorio_atual = r'C:\Users\Usuário\OneDrive\Documentos\GitHub\RoboSior\tests\teste_Pasta'
diretorio_destino = r'C:\Autos'

print(diretorio_atual)

for i in os.listdir():
    os.rename(diretorio_atual,diretorio_destino + diretorio)


