import asyncio

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


async def get_input():
    phone_number = input("Enter phone number: ")
    message = input("Enter the message you want to send: ")
    await browser_start(phone_number, message)


async def browser_start(phone_number, message):
    driver = webdriver.Edge(
        executable_path="../../drivers/msedgedriver.exe")
    driver.get("https://web.whatsapp.com/send/?phone=" +
               phone_number + "&text&type=phone_number&app_absent=0")
    await send_message(driver, message)


async def send_message(driver, message):
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "fd365im1")))
    element.send_keys(message, Keys.ENTER)
    await disconnect(driver)


async def xpath_list():
    return ["//*[@id='app']/div/div/div[3]/header/div[2]/div/span/div[3]/div",
            "//*[@id='app']/div/div/div[3]/header/div[2]/div/span/div[3]/span/div/ul/li[4]/div",
            "//*[@id='app']/div/span[2]/div/div/div/div/div/div/div[3]/div/div[2]/div/div"]


async def disconnect(driver):
    for path in await xpath_list():
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, path)))
        element.click()


asyncio.run(get_input())
