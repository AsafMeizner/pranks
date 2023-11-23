import os
import sys
import time
import keyboard
from threading import Thread
from random import randint, choice
from volume import change_volume
from music import play_music
from countdown import countdown
from bsod import bsod
import pygetwindow as gw

def emergency_exit():
    while True:
        if keyboard.is_pressed('ENTER'):
            os._exit(0)

exitThread = Thread(target=emergency_exit)
exitThread.start()

keyboard.press('f11')

volume = True
def changeVolume(arg):
    # change_volume(100)
    pass

volumeThread = Thread(target=changeVolume, args=(10,))
volumeThread.start()

def musicThreading(arg):
    play_music()

musicThread = Thread(target=musicThreading, args=(10,))
musicThread.start()

time.sleep(0.1)

def timerThreading():
    countdown(20)

countdownThread = Thread(target=timerThreading)
countdownThread.start()

time.sleep(10)

print("Goodbye :)")

time.sleep(0.5)

# Random error sounds for a more immersive experience
error_sounds = ["error1.wav", "error2.wav", "error3.wav"]
random_error_sound = choice(error_sounds)
os.system(f"start /min afplay {random_error_sound}")  # Assuming you're on macOS; adjust for Windows

# bsod section
if sys.platform == "win32":
    os.chdir(os.path.dirname(__file__))

    volume = False

    try:
        range_repeat = randint(1, 3)
        for i in range(range_repeat):
            print("ERROR CANT FIND CURRENT WORKING DIRECTORY")
            keyboard.press_and_release("F11")  # Simulate user trying to fix the issue
            time.sleep(0.01)
            keyboard.press_and_release("F11")
            time.sleep(0.01)
            keyboard.press_and_release("F11")
            time.sleep(0.01)
            keyboard.press_and_release("F11")

        bsod()

        # Hide taskbar
        taskbar = gw.getWindowsWithTitle('Taskbar')[0]
        taskbar.minimize()

        # Close other windows
        for window in gw.getWindows():
            if window.title != 'BSOD':
                window.close()

    except:
        input("Sorry, something went wrong in the installation process. Please turn on the internet and try again.")

# Provide a safe exit option
print("Press ENTER to exit.")
keyboard.wait('ENTER')

