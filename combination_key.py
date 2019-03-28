from pynput import keyboard
current = 0
def on_press(key):
    #print(str(key))
    if key == keyboard.Key.ctrl_l:
        global  current
        current = 1
    if key == keyboard.Key.esc:
        listener.stop()
    if current == 1 and key == keyboard.KeyCode(char=';'):
        print('get')


def on_release(key):
    try:
        if key == keyboard.Key.ctrl_l:
            global current
            current = 0
    except KeyError:
        pass


with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()