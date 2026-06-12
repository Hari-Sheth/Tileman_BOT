import time
import pyautogui

# Initialising the javascript console
# All in one line so it can typewrite properly

initial_JS = "const up = new KeyboardEvent('keydown', { key: 'ArrowUp', code: 'ArrowUp', bubbles: true, cancelable: true, }); const down = new KeyboardEvent('keydown', { key: 'ArrowDown', code: 'ArrowDown', bubbles: true, cancelable: true, }); const left = new KeyboardEvent('keydown', { key: 'ArrowLeft', code: 'ArrowLeft', bubbles: true, cancelable: true, }); const right = new KeyboardEvent('keydown', { key: 'ArrowRight', code: 'ArrowRight', bubbles: true, cancelable: true, }); function u() { document.dispatchEvent(up); } function d() { document.dispatchEvent(down); } function l() { document.dispatchEvent(left); } function r() { document.dispatchEvent(right); }\n"

# initialising functions to change directions (types the function in console)

def up():
    pyautogui.typewrite("u();\n")

def down():
    pyautogui.typewrite("d();\n")

def left():
    pyautogui.typewrite("l();\n")

def right():
    pyautogui.typewrite("r();\n")

# delay to focus on console

time.sleep(5)

# type in the initialising command

pyautogui.typewrite(initial_JS)

# small delay so no error (idk why this is needed but it is)

time.sleep(1)

# bot is ready to move now

while True:
    up()
    time.sleep(1)
    left()
    time.sleep(1)
    down()
    time.sleep(1)
    right()
    time.sleep(1)