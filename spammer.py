import keyboard as kb
import time

def send_str(string):
    for c in string:
        kb.press(c)
    kb.press('enter')
    time.sleep(0.85)


while True:
    if kb.is_pressed('p'):
        time.sleep(1)
        while not kb.is_pressed('o'):
            send_str('spam')
        break



