import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def get_input():
    phone_number = input("Enter phone number: ")
    message = input("Enter the message you want to send: ")
    browser_start(phone_number, message)


def browser_start(phone_number, message):
    driver = webdriver.Edge(executable_path=r"../../drivers/msedgedriver.exe")
    driver.get("https://web.whatsapp.com/send/?phone=" +
               phone_number + "&text&type=phone_number&app_absent=0")
    send_message(driver, message)


def send_message(driver, message):
    WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.CLASS_NAME, "fd365im1"))).send_keys(message, Keys.ENTER)
    disconnect(driver)


def xpath_list():
    return ["//*[@id='app']/div/div/div[3]/header/div[2]/div/span/div[3]/div",
            "//*[@id='app']/div/div/div[3]/header/div[2]/div/span/div[3]/span/div/ul/li[4]/div",
            "//*[@id='app']/div/span[2]/div/div/div/div/div/div/div[3]/div/div[2]/div/div"]


def disconnect(driver):
    for path in xpath_list():
        time.sleep(0.5)
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, path))).click()


get_input()
