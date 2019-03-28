import win32gui
import win32api
import win32con
import time
from pynput.keyboard import Key, Listener

from pynput import keyboard
current = 0
def on_press(key):
    print( win32api.GetCursorPos())
    #print(str(key))
    if key == keyboard.Key.ctrl_l:
        global  current
        current = 1
    if key == keyboard.Key.esc:
        listener.stop()
    if current == 1 and key == keyboard.KeyCode(char=';'):
        #print('get')
        x, y = win32api.GetCursorPos()
        win32api.SetCursorPos([x - 15, y])

    if current == 1 and key == keyboard.KeyCode(char="'"):
        #print('get2')
        x, y = win32api.GetCursorPos()
        win32api.SetCursorPos([x + 15, y])

    if current == 1 and key == keyboard.KeyCode(char='['):
        # print('get')
        x, y = win32api.GetCursorPos()
        win32api.SetCursorPos([x , y - 15])

    if current == 1 and key == keyboard.KeyCode(char="/"):
        # print('get2')
        x, y = win32api.GetCursorPos()
        win32api.SetCursorPos([x, y + 15])


def on_release(key):
    try:
        if key == keyboard.Key.ctrl_l:
            global current
            current = 0
    except KeyError:
        pass


with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()


