import os
import getpass as gt

# print(os.getlogin())
#
#
#
# # using path.expanduser() getting username
# print(os.path.expanduser('~'))
# print(os.environ.get('USERNAME'))
# print(gt.getuser())


download_path = r'C:\Users\Usuário\OneDrive\Documentos\GitHub\RoboSior\autos'
os.chdir(download_path)
atual = os.listdir()

print(len(atual))