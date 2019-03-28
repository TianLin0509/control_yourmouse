import win32gui
import win32api
import win32con
import time
for i in range(10):
    time.sleep(1)
    win32api.SetCursorPos([30 * (i+1), 150])

