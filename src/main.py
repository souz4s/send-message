from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By


def browserStart(phone):
    driver = webdriver.Edge(executable_path="../../drivers/msedgedriver.exe")
    driver.get("https://wa.me/" + phone)


browserStart(input("Enter phone number: "))
