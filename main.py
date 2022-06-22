#!/usr/bin/python
import os
import subprocess
import keyboard
import pyautogui
import schedule
import time


def exit():
    os.system('start /d "C:\\Program Files\\obs-studio\\bin\\64bit\\" obs64.exe --stoprecording')
    #os.system('shutdown /s')
    #pyautogui.press('enter')


def job():
    subprocess.Popen("C:\\Users\\Administrator\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe")
    time.sleep(5)
    x = 0
    y = 0

    x,y = pyautogui.locateCenterOnScreen('join.png',confidence = 0.9)

    pyautogui.click(x,y)
    time.sleep(2)

    keyboard.write("937 8544 2270")
    pyautogui.press('enter')
    time.sleep(2)

    keyboard.write("329208")
    pyautogui.press('enter')
    time.sleep(2)

    os.system('start /d "c:\\program files\\obs-studio\\bin\\64bit\\" obs64.exe --startrecording --minimize-to-tray')


schedule.every().tuesday.at("19:32").do(job)
schedule.every().tuesday.at("21:15").do(exit)

while True:
    schedule.run_pending()
    time.sleep(2)
