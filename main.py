from pynput.keyboard import Key, Listener, KeyCode
from control_funcs import *


current = 0
Hotkeys = {KeyCode(char=';'): mouse_left, KeyCode(char="'"): mouse_right,
           KeyCode(char='['): mouse_up, KeyCode(char='/'): mouse_down}
State = {Key.ctrl_l: 1, Key.shift_l: 2, Key.alt_l: 3}

def on_press(key):
    #print( win32api.GetCursorPos())
    #print(str(key))
    global current
    if key in State:
        current = State[key]
    if key == keyboard.Key.esc:
        listener.stop()

    if key in Hotkeys:
        Hotkeys[key](current)


def on_release(key):
    try:
        if key == keyboard.Key.ctrl_l:
            global current
            current = 0
    except KeyError:
        pass


with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()


