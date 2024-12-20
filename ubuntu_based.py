import os
import time

#  Надоело устанавливать софт каждый раз вручную для Рабочей машины
#  ведь это можно сделать при помощи этого скрипта


os.system('clear')
os.system('sudo apt update -y && sudo apt upgrade -y')
os.system('echo "\033[43mUPDATE and UPGRADE SYSTEM\033[0m"')
time.sleep(2)


apt = [
    'snapd', 
    'mc', 
    'htop', 
    'visidata', 
    'nano', 
    'libfuse2t64', 
    'gufw', 
    'remmina', 
    'gnome-tweak-tool',
    'vlc',
    'gimp',
    'wireshark'
    ]
for index, value in enumerate(apt):
    os.system('clear')
    os.system(f'echo "\033[43mInstall {value}\033[0m"')
    time.sleep(2)
    os.system(f'sudo apt-get install {value} -y')


os.system('cd ~/Downloads && wget https://github.com/obsidianmd/obsidian-releases/releases/download/v1.7.7/obsidian_1.7.7_amd64.deb && sudo dpkg -i obsidian_1.7.7_amd64.deb')
os.system('cd ~/Downloads && wget https://launchpad.net/veracrypt/trunk/1.26.14/+download/veracrypt-1.26.14-Ubuntu-24.04-amd64.deb && sudo dpkg -i veracrypt-1.26.14-Ubuntu-24.04-amd64.deb')


snap = ['chromium',
        'code --classic',
        'sublime-text --classic',
        'libreoffice',
        ]
for index, value in enumerate(snap):
    os.system('clear')
    os.system(f'echo "\033[43mInstall {value}\033[0m"')
    time.sleep(2)
    os.system(f'sudo snap install {value}')
