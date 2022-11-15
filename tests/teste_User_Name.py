import os
import getpass as gt

print(os.getlogin())



# using path.expanduser() getting username
print(os.path.expanduser('~'))
print(os.environ.get('USERNAME'))
print(gt.getuser())