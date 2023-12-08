from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con


# X:  742 Y:  679 RGB: (146, 200, 254)
# X:  890 Y:  685 RGB: (156, 214, 255)
# X: 1023 Y:  694 RGB: ( 54, 159, 198)
# X: 1157 Y:  706 RGB: (148, 180, 251)


def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.01)  # This pauses the script for 0.01 seconds
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


def test():
    pass


while not keyboard.is_pressed('q'):

    if pyautogui.pixel(742, 500)[0] == 0:
        click(742, 590)
    if pyautogui.pixel(890, 500)[0] == 0:
        click(890, 590)
    if pyautogui.pixel(1023, 500)[0] == 0:
        click(1023, 590)
    if pyautogui.pixel(1157, 500)[0] == 0:
        click(1157, 590)
