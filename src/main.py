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
    WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.CLASS_NAME, "fd365im1"))).send_keys(message, Keys.ENTER)
    disconnect(driver)


def xpathList():
    return ["//*[@id='app']/div/div/div[3]/header/div[2]/div/span/div[3]/div",
            "//*[@id='app']/div/div/div[3]/header/div[2]/div/span/div[3]/span/div/ul/li[4]/div",
            "//*[@id='app']/div/span[2]/div/div/div/div/div/div/div[3]/div/div[2]/div/div"]


def disconnect(driver):
    for path in xpathList():
        sleep(0.5)
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, path))).click()


getInput()
