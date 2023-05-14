# coding=utf-8
from selenium import webdriver
import random
import warnings
warnings.filterwarnings("ignore")
import time
import os
from colorama import Fore, init
init()


howmany = 20 # Avoid getting over 30, it may cause issues with your internet

import os

clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')

clearConsole()

profile = webdriver.FirefoxProfile()

profile.set_preference("dom.disable_open_during_load", False)
profile.set_preference("browser.link.open_newwindow", 3)
profile.set_preference("dom.popup_maximum", 100)

print(Fore.RED  + """
              ██ ▄█▀▄▄▄       ██░ ██  ▒█████   ▒█████  ▄▄▄█████▓    ▄▄▄▄    ▒█████  ▄▄▄█████▓
              ██▄█▒▒████▄    ▓██░ ██▒▒██▒  ██▒▒██▒  ██▒▓  ██▒ ▓▒   ▓█████▄ ▒██▒  ██▒▓  ██▒ ▓▒
             ▓███▄░▒██  ▀█▄  ▒██▀▀██░▒██░  ██▒▒██░  ██▒▒ ▓██░ ▒░   ▒██▒ ▄██▒██░  ██▒▒ ▓██░ ▒░
             ▓██ █▄░██▄▄▄▄██ ░▓█ ░██ ▒██   ██░▒██   ██░░ ▓██▓ ░    ▒██░█▀  ▒██   ██░░ ▓██▓ ░ 
             ▒██▒ █▄▓█   ▓██▒░▓█▒░██▓░ ████▓▒░░ ████▓▒░  ▒██▒ ░    ░▓█  ▀█▓░ ████▓▒░  ▒██▒ ░ 
             ▒ ▒▒ ▓▒▒▒   ▓▒█░ ▒ ░░▒░▒░ ▒░▒░▒░ ░ ▒░▒░▒░   ▒ ░░      ░▒▓███▀▒░ ▒░▒░▒░   ▒ ░░   
             ░ ░▒ ▒░ ▒   ▒▒ ░ ▒ ░▒░ ░  ░ ▒ ▒░   ░ ▒ ▒░     ░       ▒░▒   ░   ░ ▒ ▒░     ░    
             ░ ░░ ░  ░   ▒    ░  ░░ ░░ ░ ░ ▒  ░ ░ ░ ▒    ░          ░    ░ ░ ░ ░ ▒    ░      
             ░  ░        ░  ░ ░  ░  ░    ░ ░      ░ ░               ░          ░ ░           
                                                        ░                   
""")
print(Fore.GREEN + "-----------------------------------------github.com/5-30----------------------------------------------\n\n")

time.sleep(10)

clearConsole()

print(Fore.BLUE)
nom = input("Bot Name : ")
code = input("Enter Game Pin : ")


driver = webdriver.Firefox(firefox_profile=profile, executable_path='C:/Users/Clément/Desktop/kahoot bot/geckodriver.exe') # Put the path to geckodriver.exe here
driver.get("https://kahoot.it?pin="+code)
driver.implicitly_wait(500)
driver.find_element_by_id("nickname").send_keys(nom)
driver.find_element_by_xpath("/html/body/div/div[1]/div/div/div/div[3]/div[2]/main/div/form/button").click()
body = driver.find_element_by_tag_name("body")
for i in range(1,howmany):
    driver.execute_script("window.open('https://kahoot.it?pin={}')".format(code))

for i in range(1,howmany):
    print(i)
    try:
        driver.switch_to.window(driver.window_handles[i])
    except:
        break
    driver.find_element_by_id("nickname").send_keys("{} {}".format(nom, str(i)))
    driver.find_element_by_xpath("/html/body/div/div[1]/div/div/div/div[3]/div[2]/main/div/form/button").click()


while True:
    for i in range(0,howmany):
        driver.switch_to.window(driver.window_handles[i])
        try:
            driver.find_elements_by_css_selector("button")[random.randint(0,len(driver.find_elements_by_css_selector('button'))-1)].click()
        except:
            pass
