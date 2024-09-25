from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time
import random


options = Options()
options.headless = True
DRIVER_PATH = 'C:/Users/Impor/auto_clicker/chromedriver-win64/chromedriver.exe'

service = Service(DRIVER_PATH)
driver = webdriver.Chrome(service=service, options=options)

buttons = {
    'vault' : '//*[@id="__next"]/div/main/div[2]/div[4]',
    'money_autoclick_button' : '//*[@id="__next"]/div/main/div[2]/div[2]/div/div/div/div/div[1]/div[2]/div/span[1]/button', #doesnt work
    'case_autoclick_button' : '//*[@id="__next"]/div/main/div[2]/div[3]/div/div/div/div/div[1]/div[2]/div/span[1]/button', #doesnt work
    'money' : '//*[@id="__next"]/div/main/div[2]/div[2]/div/div',
    'case' : '//*[@id="__next"]/div/main/div[2]/div[3]/div/div'
}

def open_case_clicker():
    driver.get('https://case-clicker.com/')
    
def click(xpath):
    button = driver.find_element(By.XPATH, xpath)
    button.click()
    
def looper():
    counter = 0
    sleep_constant = 0.08
    pause_amt = int((60 + random.uniform(0, 30)))

    while True:
        pause_amt = int((60 + random.uniform(0, 30)))
        print(pause_amt)
        if counter > pause_amt: 
            click(buttons['vault'])
            print('button clicked')
            counter = 0
            pause_amt = int((60 + random.uniform(0, 30)))

            time.sleep(40 + random.uniform(1, 5)) 
        
        click(buttons['case'])
        
        sleep_amt = sleep_constant + random.uniform(0.01, 0.1)
        time.sleep(sleep_amt)
        counter += sleep_amt
        # print(counter)


open_case_clicker()

for i in range(30):
    time.sleep(1)
    print(i)

#click(buttons['case_autoclick_button'])
looper()
