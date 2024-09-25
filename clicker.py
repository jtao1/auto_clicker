import keyboard 
import time
import mouse 

clicks = 0

start = time.time()

SLEEP_TIME = 0.038
while True:
    if keyboard.is_pressed('p'):
        while not keyboard.is_pressed('o'):
            time.sleep(SLEEP_TIME)
            mouse.click()
            clicks += 1
            #print(f'clicked {clicks}')
        break

end = time.time()
print(f'{SLEEP_TIME} | {end-start}: {clicks} | average: {clicks / (end-start)}')