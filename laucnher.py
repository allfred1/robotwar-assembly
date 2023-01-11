import dload
import getpass
import os
import shutil
import time
import subprocess

userdata = "C:\\Users\\"
minedata = "\\AppData\\Roaming\\.minecraft\\versions"
userfiles = getpass.getuser()
typefiles = userdata + userfiles + minedata
path = "robotwar-assembly\\robotwar-assembly-allfred1"
dpath = "\\robotwar-assembly"
print('Powerd by I_Anigo_I\n \nСделано спецально для проекта RobotWar \n \n ver0.1 \n \n Не обрщайете время на ошибки')

def cleargit():
    time.sleep(10)
    shutil.rmtree(dpath, ignore_errors=True)

def movefiles():
    source = "robotwar-assembly\\robotwar-assembly-allfred1"
    sm = shutil.move(source, typefiles)
    print('Файлы перещены в', sm)
    cleargit()

def check():
    if os.path.isdir(path):
        print("Папка есть")
        movefiles()
    else:
        print('Папки нет идет установка.')
        dload.git_clone("https://github.com/allfred1/robotwar-assembly.git") 
        time.sleep(5)
        check()

time.sleep(7)
check()




#dload.git_clone("https://github.com/allfred1/installer-interface.git")
