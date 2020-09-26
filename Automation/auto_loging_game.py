import time
import pyautogui
import os
import subprocess, signal

# print(pyautogui.position())

def click():
    pyautogui.mouseDown()
    pyautogui.mouseUp()

def gf():
    time.sleep(2)
    pyautogui.moveTo(317, 873)
    click()


def entrar(y=0):
    time.sleep(1)
    for _ in range(0, 4):
        pyautogui.moveTo(573, 433+y, .2)
        click()
        gf()
        y += 38


def cojer_cofre():
    time.sleep(2)
    pyautogui.moveTo(1427, 758, .2)
    click()
    time.sleep(10)
    pyautogui.moveTo(323, 187, .2)
    click()
    time.sleep(2.7)
    pyautogui.moveTo(211, 621, .4)
    click()
    exit()


def join():
    time.sleep(.7)
    pyautogui.write("string", interval=0.1)
    time.sleep(.6)
    pyautogui.moveTo(728, 483, .4)
    click()
    pyautogui.moveTo(736, 780, .4)
    click()


def bla(x=0):
    time.sleep(10)
    for _ in range(0, 4):
        pyautogui.moveTo(611+x, 875, .4)
        x += 160
        click()
        join()


def exit():
    time.sleep(2)
    pyautogui.moveTo(1418, 6, .4)
    click()
    pyautogui.moveTo(659, 218, .4)
    click()


for _ in range(0, 20):
    entrar()
    bla()
    pyautogui.moveTo(611, 875, .4)
    click()
    time.sleep(21)
    cojer_cofre()
    pyautogui.moveTo(611, 875, .4)
    click()
    cojer_cofre()
    pyautogui.moveTo(611, 875, .4)
    click()
    cojer_cofre()
    cojer_cofre()
    time.sleep(.7)
    pyautogui.moveTo(278, 881, .4)
    click()
    pyautogui.moveTo(1081, 597, .4)
    click()
    os.system("taskkill /F /im client.exe")

#os.system("shutdown /s /t 10")
