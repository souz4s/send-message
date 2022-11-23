from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def getInput():
    phoneNumber = input("Enter phone number: ")
    message = input("Enter the message you want to send: ")
    browserStart(phoneNumber, message)


def browserStart(phoneNumber, message):
    driver = webdriver.Edge(executable_path=r"../../drivers/msedgedriver.exe")
    driver.get("https://web.whatsapp.com/send/?phone=" +
               phoneNumber + "&text&type=phone_number&app_absent=0")
    sendMessage(driver, message)


def sendMessage(driver, message):
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CLASS_NAME, "fd365im1"))).send_keys(message, Keys.ENTER)
    sleep(1)


getInput()
