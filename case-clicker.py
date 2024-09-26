import undetected_chromedriver as uc
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time
import random


options = uc.ChromeOptions()

#DRIVER_PATH = 'C:/Users/Impor/auto_clicker/chromedriver-win64/chromedriver.exe'

#service = Service(DRIVER_PATH)
#driver = webdriver.Chrome(service=service, options=options)

driver = uc.Chrome(options=options)
driver.maximize_window()

buttons = {
    'vault' : '//*[@id="__next"]/div/main/div[2]/div[4]',
    'money_autoclick_button' : '//*[@id="__next"]/div/main/div[2]/div[2]/div/div/div/div/div[3]/div/span[1]',
    'case_autoclick_button' : '//*[@id="__next"]/div/main/div[2]/div[3]/div/div/div/div/div[3]/div/span[1]',
    'money' : '//*[@id="__next"]/div/main/div[2]/div[2]/div/div',
    'case' : '//*[@id="__next"]/div/main/div[2]/div[3]/div/div',
    'cookies' : '//*[@id="CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll"]',
    'terms_con' : '//*[@id="__next"]/div/div/div/div[1]/div/div[5]/div/div/div/div/div/div[1]',
    'google_login' : '//*[@id="__next"]/div/div/div/div[1]/div/div[3]/div/div/div/button',
    'discord_login' : '//*[@id="__next"]/div/div/div/div[1]/div/div[4]/div/div/div/button',

}

def open_case_clicker():
    driver.get('https://case-clicker.com/auth/login?callbackUrl=https%3A%2F%2Fcase-clicker.com%2F')

    page_state = driver.execute_script('return document.readyState;')
    while page_state != 'complete':
        page_state = driver.execute_script('return document.readyState;')
    
def click(xpath):
    button = driver.find_element(By.XPATH, xpath)
    button.click()
    
def login(login_type):
    time.sleep(1) #sleep time depending in page loading speed
    page_state = driver.execute_script('return document.readyState;')
    while page_state != 'complete':
        page_state = driver.execute_script('return document.readyState;')
    
    click(buttons['cookies'])
    click(buttons['terms_con'])

    click(buttons[login_type])

def looper():
    click(buttons['case_autoclick_button'])
    counter = 0
    sleep_constant = 0.08
    pause_amt = int((60 + random.uniform(0, 30)))
    click(buttons['vault'])

    while True:
        if counter > pause_amt: 
            click(buttons['vault'])
            print('button clicked')
            counter = 0
            pause_amt = int((60 + random.uniform(0, 30)))
            print(pause_amt)
            time.sleep(40 + random.uniform(1, 5)) 
        
        click(buttons['case'])
        
        sleep_amt = sleep_constant + random.uniform(0.01, 0.1)
        time.sleep(sleep_amt)
        counter += sleep_amt


open_case_clicker()
login('discord_login')
input()

click(buttons['case'])
looper()