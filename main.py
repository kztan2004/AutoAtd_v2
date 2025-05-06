import cv2
import numpy as np
import pyautogui
import keyboard

from selenium import webdriver
from selenium.webdriver.common.by import By

import configparser

import time

keyword = "https://osc.mmu.edu.my/psc/csprd/EMPLOYEE/SA/c/"
detector = cv2.QRCodeDetector()

config = configparser.ConfigParser()
config.read('config.ini')
ID = config['info']['id']
PASSWORD = config['info']['password']

def login(PATH):
    driver = webdriver.Chrome()
    driver.get(PATH)
    try:
        username = driver.find_element(By.ID, "N_QRCODE_DRV_USERID")
        username.send_keys(ID)

        password = driver.find_element(By.ID, "N_QRCODE_DRV_PASSWORD")
        password.send_keys(PASSWORD)

        signin_button = driver.find_element(By.ID, "N_QRCODE_DRV_BUTTON1")
        signin_button.click()
        
        print("Captured!")
    except:
        print("Capture Failed...")

    time.sleep(2)
    driver.quit()

print("Service Started...")
print("Looking for QR... (hold 'q' to stop the service)")
while (True):
    if keyboard.is_pressed('q'):
        print('Exiting...')
        break

    screenshot = pyautogui.screenshot()
    screenshot = np.array(screenshot)
    value, points, qrcode = detector.detectAndDecode(screenshot)

    if keyword in value:
       print(value)
       login(value)
       break

    time.sleep(1)

print('Service Ended')