import os
import shutil
import requests
from colorama import init, Fore, Style

init()

print(Fore.RED + Style.BRIGHT +
'''
Überschrift
''')

path = os.getcwd()
oldfilespath = path + r'\\old-files'
print('Backing up old files')
if not os.path.isdir(oldfilespath):
    os.mkdir(oldfilespath)
if os.path.isfile(path + '\\exefile.exe'):
    shutil.move(path + '\\exefile.exe', oldfilespath + '\\exefile.exe')
print('Backing up complete')
print('Beginning download of new files')
exeurl = 'https://domain.xyz/exefile.exe'
exe = requests.get(exeurl, allow_redirects=True)
open(path + '\\exefile.exe', 'wb').write(exe.content)
print('Download complete')
