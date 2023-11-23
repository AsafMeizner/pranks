import subprocess
import os
from random import randint
from time import sleep
import sys
from time import sleep
from threading import Thread


# this is a program that plays outro music while playing a countdown, in the end of the countdown it starts a fake blue screen


# bat_pip_path = str(f"{os.path.dirname(__file__)}/pip.bat")
# subprocess.call([bat_pip_path])


import keyboard
keyboard.press('f11')

def changeVolume(arg):
    # batch_volume_file_path = str(f"{os.path.dirname(__file__)}/bat/volume.bat")
    # subprocess.call([batch_volume_file_path])
    while True:
        batch_volume_file_path = str(f"{os.path.dirname(__file__)}/volume.vbs")
        subprocess.call([batch_volume_file_path])
        sleep(1)

volumeThread = Thread(target = changeVolume, args = (10, ))
volumeThread.start()

def musicThreading(arg):
    batch_vbs_file_path = str(f"{os.path.dirname(__file__)}/vbs.bat")
    subprocess.call([batch_vbs_file_path])

musicThread = Thread(target = musicThreading, args = (10, ))
musicThread.start()

sleep(0.1)

i = 15

while i > 0:
    print("Deleting system 32 in ", i)
    sleep(1)
    i = i - 1

print("Goodbye :)")

sleep(0.5)


#bsod section \/
if sys.platform == "win32":
    os.chdir(os.path.dirname(__file__))

    # pip_file_path = str(f"{os.path.dirname(__file__)}/bat/pip.bat")
    # subprocess.call([pip_file_path])

    try:
        import keyboard  # pip install keyboard
        range_repeat = randint(1, 3)
        for i in range(range_repeat):
            print("ERROR CANT FIND CURRENT WORKING DIRECTORY")
            keyboard.press_and_release("F11")
            keyboard.press_and_release("F11")
            keyboard.press_and_release("F11")
            keyboard.press_and_release("F11")
            keyboard.press_and_release("F11")
            sleep(0.01)
            keyboard.press_and_release("F11")
            keyboard.press_and_release("F11")
            keyboard.press_and_release("F11")
            keyboard.press_and_release("F11")


        bat_file_path = str(f"{os.path.dirname(__file__)}/bsod.bat")
        subprocess.call([bat_file_path])

    except:
        input("Sorry something went wrong in the installation process. Please turn on internet and try again.")

else:
    input("Sorry, this program is only compatible with Windows.")
