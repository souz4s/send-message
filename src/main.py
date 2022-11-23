from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

phoneNumber = input("Enter phone number: ")
message = input("Enter the message you want to send: ")


def browserStart(phoneNumber, message):
    driver = webdriver.Edge(executable_path="../../drivers/msedgedriver.exe")
    driver.get("https://wa.me/" + phoneNumber)


browserStart(phoneNumber, message)
